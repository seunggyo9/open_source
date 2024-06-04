import requests
from bs4 import BeautifulSoup
import csv

# 네이버 뉴스 기사 URL 예시
url = input("뉴스 url을 입력해주세요: ")

# 웹 페이지 요청
response = requests.get(url)
if response.status_code == 200:
    # HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 기사 제목 크롤링 (예시)
    title_tag = soup.find('h2', {'class': 'media_end_head_headline'})
    if title_tag:
        title = title_tag.get_text()
    else:
        title = "Title not found"

    # 기사 본문 크롤링 (예시)
    content_tag = soup.find('div', {'id': 'contents'})
    if content_tag:
        content = content_tag.get_text(strip=True)
        # 점을 기준으로 분리하여 줄바꿈 추가
        content = content.replace('.', '.\n')
    else:
        content = "Content not found"

    print("Title:", title)
    print("Content:", content)

    print("Title:", title)
    print("Content:", content)

    # Save to CSV file
    with open('article.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Content'])
        writer.writerow([title, content])

    print("Article saved to article.csv")
else:
    print("Failed to retrieve the webpage")
