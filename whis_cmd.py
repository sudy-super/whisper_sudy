import os
import time
import shlex
import subprocess

# --- 設定 ---
INPUT_FILE = "inter_3.mp3"
TRANSCRIPT_FILE = "transcription.txt"
WHISPER_CLI = "./whisper.cpp/build/bin/whisper-cli"
MODEL_PATH = "./whisper.cpp/models/ggml-large-v3.bin"
LANG = "en"     # --language の値
BEAM_SIZE = 5   # --beam_size の値

# 出力ファイルを初期化
open(TRANSCRIPT_FILE, "w", encoding="utf-8").close()

# コマンド文字列を組み立て
# -m: モデルパス, -f: 入力ファイル, --language: 言語, --beam_size: ビーム幅
cmd = (
    f"{WHISPER_CLI} "
    f"-m {shlex.quote(MODEL_PATH)} "
    f"-f {shlex.quote(INPUT_FILE)} "
    # f"--language {shlex.quote(LANG)} "
    # f"--beam_size {BEAM_SIZE}"
)

print("文字起こし開始...")
start = time.time()

# サブプロセス実行：標準出力をキャプチャし、テキストとして取得
result = subprocess.run(
    shlex.split(cmd),
    capture_output=True,  # stdout と stderr を PIPE に割り当て
    text=True             # bytes → str に自動デコード
)

# エラー時には例外を発生させる
result.check_returncode()  # returncode != 0 の場合、CalledProcessError を送出

# Whisper-CLI の出力（文字起こし結果）をそのまま使う
transcript = result.stdout

elapsed = time.time() - start
print(f"認識完了: {len(transcript)} 文字, {len(transcript)/elapsed:.2f} chars/s")

# ファイルへ書き込み
with open(TRANSCRIPT_FILE, "w", encoding="utf-8") as f:
    f.write(transcript)

print(f"文字起こし結果を '{TRANSCRIPT_FILE}' に保存")
