import json
import requests
from gensim.summarization import summarize
from newspaper import Article
from bs4 import BeautifulSoup


def get_hacker_news_urls() -> list:
    html = requests.get('https://news.ycombinator.com/').text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('.storylink')
    return [link.get('href') for link in links if link.get('href')[-3:] != 'pdf']


def get_news_summary(url: str) -> str:
    news = Article(url, language='en')
    news.download()
    news.parse()
    return f"*{news.title}*\n{summarize(news.text, word_count=40)}\n{url}\n"


def send_message(message: str) -> None:
    webhook_url = 'https://hooks.slack.com/services/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'
    requests.post(webhook_url, data=json.dumps({'text': message}))


news_urls = get_hacker_news_urls()[:10] # 앞에 10개만 가져오기
send_message(("\n--------\n").join([get_news_summary(news_url) for news_url in news_urls]))
