# Whisper Sudy

> [!IMPORTANT]
> NOTE: Macbook M4 Airで動作確認しています。

## 前提

- python 3.10.17 (3.10ならなんでも)
- ffmpegのインストール
- Xcodeのインストール, パス通し
- cmakeのインストール

## 環境構築

1. pythonバージョン合わせ

```
pyenv install 3.10.17
pyenv local 3.10.17
```

2. 仮想環境作成

```
python -m venv whis
source whis/bin/activate
```

3. 依存関係インストール

```
pip install -r requirements.txt
```

4. ビルド等

```
git clone https://github.com/ggml-org/whisper.cpp.git
cd whisper.cpp
sh ./models/download-ggml-model.sh large-v3 # ggmlバイナリが未取得の場合のみ
./models/generate-coreml-model.sh large-v3

cmake -B build -DWHISPER_COREML=1 # Core MLを使わない場合は0
cmake --build build --config Release
```

5. 実行

動画 / 音声ファイルを配置し、各ファイルの`if __name__ == "__main__":`以下の関数に適切なファイル名・パスを記入

whis_cmd.txtを参考にwhis_cmd.shの引数を調整

```
python convert.py # ファイルが音声ファイルでない時実行
python slow.py # 音声ファイルが早送りの時実行
bash whis_cmd.py
```