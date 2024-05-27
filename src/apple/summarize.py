def summarize_article(article):
    # 문장으로 나누기
    sentences = sent_tokenize(article)
    
    # 처음 세 문장 선택하여 반환
    summary = ' '.join(sentences[:3])
    
    return summary
