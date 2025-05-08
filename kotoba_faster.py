from faster_whisper import WhisperModel

model_size = "kotoba-tech/kotoba-whisper-v2.0-faster"

# Run on GPU with FP16
model = WhisperModel(model_size, device="cpu", compute_type="float32")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("inter_7.wav", temperature=0.7, beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

with open("inter_7_transcript.txt", "w", encoding="utf-8") as f:
    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        f.write(segment.text + "\n")