import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 5  # Duration

print("Recording...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

write("output.wav", fs, recording)
print("Recording saved as output.wav")

print("Playing...")
sd.play(recording, fs)
sd.wait()

print("Done")