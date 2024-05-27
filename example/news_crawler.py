from crawler import make_pg_num, make_url
import requests
from bs4 import BeautifulSoup

def crawl_naver_news(search, start_pg, end_pg):
    urls = make_url(search, start_pg, end_pg)
    headers = {"User-Agent": "Mozilla/5.0"}
    
    news_data = []
    for url in urls:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.select("div.news_area > a")
        for article in articles:
            if "news.naver.com" in article['href']:
                news_data.append({"title": article.get_text(), "link": article['href']})
    
    return news_data

# 사용 예시
if __name__ == "__main__":
    search = "테스트"
    start_pg = 1
    end_pg = 2
    news = crawl_naver_news(search, start_pg, end_pg)
    for n in news:
        print(n)
