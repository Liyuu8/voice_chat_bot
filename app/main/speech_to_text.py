import os
import sounddevice as sd
from scipy.io.wavfile import write
import openai
from dotenv import load_dotenv

# .envファイルの内容を読み込見込む
load_dotenv()

# OpenAIのAPIキーを設定
openai.api_key = os.environ['API_KEY']

# 録音のパラメータ
fs = 44100  # サンプルレート
seconds = 5  # 録音時間

# 録音の開始
print("録音を開始します。")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # 録音が終了するまで待つ

# 録音の保存
write('output.wav', fs, recording)
print("録音が終了しました。")

# ファイルをバイナリモードで開く
with open('output.wav', "rb") as audio_file:
    # Whisper APIを使用してオーディオファイルをテキストに変換
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

# 音声からテキスト変換した結果を表示
print(transcript.text)
