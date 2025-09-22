from ddgs import DDGS

# 検索するキーワード
KEYWORD = '任天堂'

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

results = search_news(KEYWORD)

print(results)