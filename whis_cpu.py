import os
import time
import numpy as np
import soundfile as sf
from faster_whisper import WhisperModel

# --- 設定 ---
INPUT_FILE = "inter_3.wav"
TRANSCRIPT_FILE = "transcription.txt"

# Whisper モデルのロード
model = WhisperModel(
    model_size_or_path="large-v3",  # medium や small に変更可
    device="cpu",
    compute_type="int8"
)

# --- 音声ファイル読み込み ---
# soundfile で直接 wav を読み込み
audio_array, sampling_rate = sf.read(INPUT_FILE)
# Whisper は float32 を期待
if audio_array.dtype != np.float32:
    audio_fp32 = audio_array.astype(np.float32)
else:
    audio_fp32 = audio_array

# トランスクリプション用ファイルを初期化
with open(TRANSCRIPT_FILE, "w", encoding="utf-8") as f:
    pass

# 逐次ではなく一度に全体を認識
start = time.time()
print("文字起こし開始...")
# Whisper に直接 numpy 配列を渡して文字起こし
segments, info = model.transcribe(
    audio=audio_fp32,
    beam_size=5,
    language="en",        # 必要に応じて"ja"などに変更
    word_timestamps=False  # 単語単位のタイムスタンプが必要な場合はTrue
)

# テキスト抽出
text = "".join([segment.text for segment in segments])

elapsed = time.time() - start
print(f"認識完了: {len(text)} 文字, Char Per Second: {len(text)/elapsed:.2f} chars/s")

# ファイルへ書き込み
with open(TRANSCRIPT_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print(f"文字起こし結果を '{TRANSCRIPT_FILE}' に保存")