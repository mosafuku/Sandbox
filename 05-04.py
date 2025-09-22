import getpass
import os
import requests
from ddgs import DDGS

# Gina Reader URL
URL_JINA = 'https://r.jina.ai/'
# 対象URL
URL = 'https://ja.wikipedia.org/wiki/%E4%BB%BB%E5%A4%A9%E5%A0%82'

# 環境変数にGOOGLE_API_KEYが設定されているか確認
if not os.environ.get("GOOGLE_API_KEY"):
  # 環境変数が未設定の場合、ユーザーにAPIキーの入力を促す
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

def search_news(keyword):
    with DDGS() as ddgs:
        results = list(ddgs.news(
            query=keyword,
            region='jp-jp',
            safesearch='off',
            timelimit=None,
            max_results=3
        ))
    return results

def get_content(url):
    content = ''

    try:
        # Gina ReaderにリクエストするURL
        url = URL_JINA + url
        # リクエスト
        response = requests.get(url)
        # HTTPエラーがあれば例外を発生させる
        response.raise_for_status()
        # 記事内容
        content = response.text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return content

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


#----------------------------------------------------
# 検索するキーワード
KEYWORD = '任天堂'

# ニュース検索
results = search_news(KEYWORD)

for result in results:
    # 内容取得
    content = get_content(result['url'])
    # 要約
    summary = summarize(content)
    # 結果出力
    print('-------------------------------------')
    print(result['title'])
    print(result['url'])
    print(summary)