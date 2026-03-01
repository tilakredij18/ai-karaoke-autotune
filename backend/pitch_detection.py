import librosa
import numpy as np
import matplotlib.pyplot as plt

# Load audio
y, sr = librosa.load("output.wav")

# Extract pitch (fundamental frequency)
f0, voiced_flag, voiced_probs = librosa.pyin(
    y,
    fmin=librosa.note_to_hz('C2'),
    fmax=librosa.note_to_hz('C7')
)

# Time axis
times = librosa.times_like(f0)

# Plot pitch
plt.figure(figsize=(10, 4))
plt.plot(times, f0, label='Pitch (Hz)')
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.title("Pitch Detection")
plt.legend()
plt.show()