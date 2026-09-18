
import threading
import sys
try:
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    import speech_recognition as sr
from speech_recognition import AudioData
except ImportError as e:
print(f" Missing library: {e.name}")
print("\n???? Install commands:")
print("   Windows: pip install SpeechRecognition pyaudio numpy matplotlib")
print("   macOS:   brew install portaudio && pip install SpeechRecognition pyaudio numpy matplotlib")

sys.exit(1)
top_event = threading.Event()
def wait_for_enter():
    input()
stop_event.set()
def record_audio(label):
    stop_event.clear()
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                 input=True, frames_per_buffer=1024)
frames = []
print(f"\n???? {label}")
print("   Press Enter to stop...")
threading.Thread(target=wait_for_enter, daemon=True).start()
print("???? Recording", end="", flush=True)
while not stop_event.is_set():
     frames.append(stream.read(1024, exception_on_overflow=False))
     print("." end="", flush=True)
print("✅")
stream.stop_stream()
stream.close()
width = p.get_sample_size(pyaudio.paInt16)
p.terminate()
return b''.join(frames), 16000, width

def analyze_audio(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)
return {

     'duration': len(samples) / rate,

     'avg_volume': np.mean(np.abs(samples)),

     'max_volume': np.max(np.abs(samples)),

     'samples': samples

}
def transcribe(data,rate,width):
    recogniser = sr.Recogniser()
try:
    return recogniser. recognize_google(AudioData(data,rate,width))
except:
    return "[Could not transcribe]"
def display_stats(stats,text,label):
    print(f"\n{'-' * 40}")
    print(f"????{label}")
    print(f"{'-' * 40}")
    print(f" Duration{stats['duration']:.2f} seconds")
    print(f"???? Avg ampitude:{stats['avg_volume']:.0f}")
    print(f"???? max amplitude:{stats['max_volume']:.0f}") 
    print(f"???? transcription{text}")
def compare(stats1,stats2):
    print("\n"+"=" *40)
    print("???? COMPARISION RESULTS")
    print("=" *40)
if stats1["duration"] > stats2["duration"]:
    longer = "recording 1"
    diff =((stats1['duration']- stats2['duration']) / stats2['duration'])
else: 
     longer = "recording 2"
     diff =((stats2['duration']- stats1['duration']) / stats1['duration'])
print(f"{longer is by {diff:.1f}}%")
if stats1['avg_volume'] > stats2['avg_volume']:

     louder = "Recording 1"
     diff = ((stats1['avg_volume'] - stats2['avg_volume']) / stats2['avg_volume']) * 100

else:
    louder = "Recording 2"
    diff = ((stats2['avg_volume'] - stats1['avg_volume']) / stats1['avg_volume']) * 100
print(f"???? {louder} is louder by {diff:.1f}%")

def plot_both(stats1, stats2, rate):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
t1 = np.linspace(0, len(stats1['samples']) / rate, len(stats1['samples']))
ax1.plot(t1, stats1['samples'], color='blue', linewidth=0.5)
ax1.set_title(f"Recording 1 (normal) - duration:{ stats1['duration']:2f}s, Avg: {stats1[avg_volume:.0f]}")
ax1.set_ylabel("Amplitude")
ax1.grid(True,alpha=0.3)
ax1.set_ylim(-35000, 35000)

t2 = np.linspace(0, len(stats2['samples']) / rate, len(stats2['samples']))
ax2.plot(t2, stats2['samples'], color='red', linewidth=0.5)
