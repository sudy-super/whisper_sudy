#!/usr/bin/env bash

INPUT_FILE="inter_6.wav"
OUTPUT_FILE="inter_6_transcript"
WHISPER_CLI="./whisper.cpp/build/bin/whisper-cli"
MODEL_PATH="./whisper.cpp/models/ggml-large-v3.bin"
TMP=0.7
LANG="en"

"$WHISPER_CLI" \
  -m "$MODEL_PATH" \
  -f "$INPUT_FILE" \
  -tp $TMP \
  -otxt \
  -of "$OUTPUT_FILE" \
  -l "$LANG" \
  -pp \
  -nt \
  -pc
# -np