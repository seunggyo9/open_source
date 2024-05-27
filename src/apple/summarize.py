def textrank_summarize(text, num_sentences=3):
    # 문장 분리
    sentences = nltk.sent_tokenize(text)

    # 문장 간 유사도 그래프 생성
    graph = nx.Graph()
    for i, sentence in enumerate(sentences):
        for j, other_sentence in enumerate(sentences):
            if i == j:
                continue
            similarity = compute_similarity(sentence, other_sentence)
            graph.add_edge(i, j, weight=similarity)

    # 텍스트 랭크 알고리즘을 사용하여 문장 순위 결정
    scores = nx.pagerank(graph)

    # 순위에 따라 문장 정렬
    ranked_sentences = sorted(((score, i) for i, score in scores.items()), reverse=True)
    
    # 상위 num_sentences 개의 문장 추출
    top_sentences = [sentences[i] for _, i in ranked_sentences[:num_sentences]]

    return ' '.join(top_sentences)
