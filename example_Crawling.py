import requests
from bs4 import BeautifulSoup as bs

사용자 검색어 입력
keyword = input("검색어를 입력하세요: ")

검색 결과 페이지 수 입력
total_page = int(input("몇 페이지까지 검색할까요: "))

page_num = 1
for i in range(1, total_page * 10, 10):
search_url = f"https://search.naver.com/search.naver?where=news&query={keyword}&start={i}"
response = requests.get(search_url)
html_text = response.text

print()
print(response.status_code)
print(f'******* {page_num}페이지 검색 결과입니다. *******')

# 다루기 어려운 html 문자열을 html 태그


// 참고 https://gojstudio.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%84%A4%EC%9D%B4%EB%B2%84-%EB%89%B4%EC%8A%A4-%ED%81%AC%EB%A1%A4%EB%A7%81-%EC%98%88%EC%A0%9C/
