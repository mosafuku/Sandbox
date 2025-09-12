import getpass
import os

# 環境変数にGOOGLE_API_KEYが設定されているか確認
if not os.environ.get("GOOGLE_API_KEY"):
  # 環境変数が未設定の場合、ユーザーにAPIキーの入力を促す
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

# LangChainのinit_chat_model関数を使用して、Geminiモデルを初期化
# "gemini-2.5-flash"は利用するモデル名、model_providerはプロバイダー名
from langchain.chat_models import init_chat_model
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

# ユーザーからのメッセージ（プロンプト）をHumanMessageオブジェクトとして定義
# LangChainでは、人間からのメッセージをHumanMessageとして扱います
from langchain_core.messages import HumanMessage
messages = [
    HumanMessage(content="自己紹介をしてください。")
]

# 定義したメッセージをモデルに送信し、応答を取得
# invokeメソッドがAPI呼び出しを実行します
result = model.invoke(messages)

# モデルからの応答を出力
# 応答はAIMessageオブジェクトとして返されます
print(result.content)