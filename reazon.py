from reazonspeech.espnet.asr import load_model, transcribe, audio_from_path

audio = audio_from_path("inter_7_light.wav")
print("[INFO] Audio loaded")
model = load_model()
print("[INFO] Model loaded")
ret = transcribe(model, audio)

with open("inter_7_transcript.txt", "w", encoding="utf-8") as f:
    f.write(ret.text)