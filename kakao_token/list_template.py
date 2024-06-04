# 사용자가 선택한 카테고리를 제목에 넣기 위한 dictionary
sections_ko = {'pol': '정치', 'eco' : '경제', 'soc' : '사회'}

# 네이버 뉴스 URL
navernews_url = "https://news.naver.com/main/home.nhn"

# 추후 각 리스트에 들어갈 내용(content) 만들기
contents = []

# 리스트 템플릿 형식 만들기
template = {
    "object_type" : "list",
    "header_title" : sections_ko[my_section] + " 분야 상위 뉴스 빅3",
    "header_link" : {
        "web_url": navernews_url,
        "mobile_web_url" : navernews_url
    },
    "contents" : contents,
    "button_title" : "네이버 뉴스 바로가기"
}
## 내용 만들기
# 각 리스트에 들어갈 내용(content) 만들기
for news_info in news_list3:    
    content = {
        "title" : news_info.get('title'),
        "description" : "작성일 : " + news_info.get('date'),
        "image_url" : news_info.get('image_url'),
        "image_width" : 50, "image_height" : 50,
        "link": {
            "web_url": news_info.get('news_url'),
            "mobile_web_url": news_info.get('news_url')
        }
    }
    
    contents.append(content)
    
# 카카오 메시지 전송
res = kakao_utils.send_message(KAKAO_TOKEN_FILENAME, template)
if res.json().get('result_code') == 0:
    print('뉴스를 성공적으로 보냈습니다.')
else:
    print('뉴스를 성공적으로 보내지 못했습니다. 오류메시지 : ', res.json())


    ## 오픈소스 출처 : https://ai-creator.tistory.com/36 ##