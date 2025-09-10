from google import genai
import os

# 環境変数からAPIキーを取得
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# テキスト生成
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="自己紹介をしてください。"
)

# 結果の出力
print(response.text)