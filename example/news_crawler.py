from apple import summarize_text
import ntlk
ntlk.download('punkt')
ntlk.download('stopwords')

# 사용 예시
article_text = """
오늘은 화창한 날이다. 햇빛이 화사하게 비치고 있습니다. 나무 그늘 아래에서도 햇빛이 따뜻하게 들어오고 있어서 시원한 바람을 맞으며 산책하는 것이 기분 좋습니다. 차 한 잔을 마시면서 책을 읽는 것도 좋겠네요. 책을 읽으며 햇빛을 맞으면서 조용한 시간을 보내는 것은 참으로 행복한 일이죠. 새들의 지저귐이 귀를 감싸고 있어 마치 대자연의 향연 속에 있는 듯한 기분이 듭니다. 책과 차의 조합은 정말 최고입니다. 햇빛 아래에서 책을 읽는 것은 더욱 특별한 경험이 될 것 같습니다. 차 한 잔과 함께 읽는 책은 더욱 맛있는 것 같아요. 책을 읽으면서 차 한 잔 마시며 오늘 하루를 마무리하면 좋을 것 같아요.
"""
summary = summarize_text(article_text, num_sentences=3)
print(summary)
