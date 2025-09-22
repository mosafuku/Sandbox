import requests

# Gina Reader URL
URL_JINA = 'https://r.jina.ai/'
# 対象URL
URL = 'https://ja.wikipedia.org/wiki/%E4%BB%BB%E5%A4%A9%E5%A0%82'

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

content = get_content(URL)

print(content)