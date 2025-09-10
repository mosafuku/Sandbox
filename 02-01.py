import requests
import json
import os

# 環境変数からAPIキーを取得
API_KEY = os.environ.get("GOOGLE_API_KEY")

# エンドポイントURL
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

# リクエストヘッダー
headers = {
    "Content-Type": "application/json"
}

# リクエストボディ
payload = {
    "contents": [
        {
            "parts": [
                {"text": "自己紹介をしてください。"}
            ]
        }
    ]
}

# POSTリクエストの送信
response = requests.post(url, headers=headers, data=json.dumps(payload))

# レスポンスの解析と出力
result = response.json()
generated_text = result['candidates'][0]['content']['parts'][0]['text']

print("生成されたテキスト：")
print(generated_text)