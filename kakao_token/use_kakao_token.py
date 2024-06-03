import json
import kakao_utils

KAKAO_TOKEN_FILENAME = "res/kakao_message/kakao_token.json" #"<kakao_token.json 파일이 있는 경로를 입력하세요.>"
KAKAO_APP_KEY = "<REST_API 앱키를 입력하세요>"
kakao_utils.update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)


##오픈소스 출처 : https://ai-creator.tistory.com/36 ##