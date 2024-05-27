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
