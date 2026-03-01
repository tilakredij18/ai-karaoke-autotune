import librosa
import numpy as np

# Load audio
y, sr = librosa.load("output.wav")

# Extract pitch
f0, voiced_flag, voiced_probs = librosa.pyin(
    y,
    fmin=librosa.note_to_hz('C2'),
    fmax=librosa.note_to_hz('C7')
)

# Convert frequency → MIDI notes
midi_notes = librosa.hz_to_midi(f0)

# Define a scale (C major)
scale_notes = np.array([0, 2, 4, 5, 7, 9, 11])  # C major intervals

def snap_to_scale(midi):
    if np.isnan(midi):
        return np.nan
    note = int(round(midi)) % 12
    closest = scale_notes[np.argmin(np.abs(scale_notes - note))]
    return midi - note + closest

# Apply autotune
corrected_midi = np.array([snap_to_scale(m) for m in midi_notes])

# Convert back → frequency
corrected_f0 = librosa.midi_to_hz(corrected_midi)

print("Original MIDI (first 10):", midi_notes[:10])
print("Corrected MIDI (first 10):", corrected_midi[:10])