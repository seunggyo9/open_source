def summarize_text(text, num_sentences=3):
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.corpus import stopwords
    from nltk.probability import FreqDist

    # 텍스트를 문장으로 분할
    sentences = sent_tokenize(text)
    
    # 단어를 토큰화하고 불용어를 제거
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    
    # 단어 빈도 계산
    freq_dist = FreqDist(filtered_words)
    
    # 문장 점수 계산
    sentence_scores = {}
    for sentence in sentences:
        sentence_word_count = word_tokenize(sentence)
        for word in sentence_word_count:
            if word.lower() in freq_dist:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = freq_dist[word.lower()]
                else:
                    sentence_scores[sentence] += freq_dist[word.lower()]
    
    # 가장 점수가 높은 문장들을 선택
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    # 요약문 생성
    summary = ' '.join(summary_sentences)
    
    return summary
