import wave

obj = wave.open("patrick.wav", "rb")

print("number of channels : ", obj.getnchannels())
print("sample width : ", obj.getsampwidth())
print("frame rate : ", obj.getframerate())
print("number of frames : ", obj.getnframes())
print("parameters : ", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print("time / second : ", t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))
