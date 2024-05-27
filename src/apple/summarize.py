def summarize_text(text, num_sentences=3):
    
    # 문장 단위로 텍스트를 분할
    sentences = text.split('. ')
    
    # 문장을 길이(단어 수) 기준으로 정렬
    sorted_sentences = sorted(sentences, key=lambda s: len(s.split()), reverse=True)
    
    # 가장 긴 num_sentences개의 문장 선택
    summary_sentences = sorted_sentences[:num_sentences]
    
    # 요약문 생성
    summary = '. '.join(summary_sentences)
    
    return summary

# 사용 예제
article_text = """
여기에 요약하고 싶은 텍스트를 넣으세요. 이 텍스트는 문장이 여러 개로 이루어져 있습니다. 각 문장은 다소 길이가 다를 수 있습니다.
가장 긴 문장을 골라서 요약을 생성할 것입니다. 요약문은 가장 중요한 정보를 포함할 것입니다.
"""
summary = summarize_text(article_text, num_sentences=3)
print(summary)
