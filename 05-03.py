import getpass
import os

CONTENT = '1889年に創業した老舗企業で、娯楽に関するさまざまな事業を展開している。創業以来、多くの種類の玩具を製作しており、特に花札やトランプは、創業初期から現在に至るまで製造、販売を続けている。1970年代後期にコンピュータゲーム機の開発を開始した。1981年発売のアーケードゲーム『ドンキーコング』の成功で頭角を現し、1983年発売の家庭用据え置き型ゲーム機「ファミリーコンピュータ」のゲームソフトとして1985年に発売した『スーパーマリオブラザーズ』が世界的にヒットしたことでゲーム機やゲームソフトを開発する会社として広く認知されるようになった。スウェーデンのハッランド県にあるマリオの像。『スーパーマリオブラザーズ』（マリオシリーズ）の主人公「マリオ」など、任天堂のゲームソフトに登場するキャラクターは世界的に認知されているものが多く、2010年代からはキャラクターIPのゲーム外での活用を進めている。'

# 環境変数にGOOGLE_API_KEYが設定されているか確認
if not os.environ.get("GOOGLE_API_KEY"):
  # 環境変数が未設定の場合、ユーザーにAPIキーの入力を促す
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

def summarize(text):
    # LangChainのinit_chat_model関数を使用して、Geminiモデルを初期化
    # "gemini-2.5-flash"は利用するモデル名、model_providerはプロバイダー名
    from langchain.chat_models import init_chat_model
    model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

    # ユーザーからのメッセージ（プロンプト）をHumanMessageオブジェクトとして定義
    # Langchainにはテンプレート機能が存在するが、ここでは文字列結合で実現させる
    from langchain_core.messages import HumanMessage
    messages = [
        HumanMessage(content="以下のテキストを要約してください。\n\n" + text)
    ]

    # 定義したメッセージをモデルに送信し、応答を取得
    # invokeメソッドがAPI呼び出しを実行します
    result = model.invoke(messages)

    return result.content

summary = summarize(CONTENT)

# モデルからの応答を出力
# 応答はAIMessageオブジェクトとして返されます
print(summary)