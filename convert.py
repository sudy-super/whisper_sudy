import subprocess
import json

def has_audio_stream(input_path: str) -> bool:
    """ffprobe で音声ストリームの有無を確認"""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_streams", "-of", "json", input_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    info = json.loads(result.stdout)
    for stream in info.get("streams", []):
        if stream.get("codec_type") == "audio":
            return True
    return False

def webm_to_mp3(input_path: str, output_path: str, bitrate: str = "10000k"):
    if not has_audio_stream(input_path):
        raise RuntimeError(f"No audio stream found in {input_path}")
    cmd = [
        "ffmpeg",
        "-i", input_path,
        "-vn",
        "-b:a", bitrate,
        "-y",
        output_path
    ]
    subprocess.run(cmd, check=True)

def webm_to_wav(input_path: str, output_path: str, sample_rate: int = 100000):
    """
    .webm → .wav 変換を実行する。

    :param input_path: 入力の .webm ファイルパス
    :param output_path: 出力の .wav ファイルパス
    :param sample_rate: 出力サンプルレート（Hz）
    """
    if not has_audio_stream(input_path):
        raise RuntimeError(f"No audio stream found in {input_path}")
    cmd = [
        "ffmpeg",
        "-i", input_path,         # 入力ファイル
        "-vn",                    # 動画ストリーム無視
        "-ar", str(sample_rate),  # サンプルレート指定
        "-ac", "2",               # チャンネル数指定（ステレオ）
        "-y",                     # 上書き許可
        output_path
    ]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    webm_to_wav("international_II_6.mp4", "inter_6.wav")
