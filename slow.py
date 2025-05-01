import librosa
import soundfile as sf

def slow_down_librosa(input_path: str, output_path: str, speed_factor: float = 0.05):
    """
    MP3 ファイルを指定した速度に遅くして出力する。
    speed_factor: 1.0 が原速, 0.05 が 1/20 倍速相当
    """
    # 波形データとサンプリングレートを読み込み
    y, sr = librosa.load(input_path, sr=None)  # sr=None で元のレートを保持 :contentReference[oaicite:5]{index=5}

    # タイムストレッチ
    y_slow = librosa.effects.time_stretch(y, rate=speed_factor)  # rate<1 でスローダウン :contentReference[oaicite:6]{index=6}

    # WAV などで書き出し。MP3 へ変換したい場合はさらに pydub 等を利用
    sf.write(output_path, y_slow, sr)

if __name__ == "__main__":
    slow_down_librosa("international_II_3.mp3", "inter_3.mp3", speed_factor=1/3)
