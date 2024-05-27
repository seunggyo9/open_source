from collections import Counter
from nltk.tokenize import word_tokenize
import re

def summarize_text(text, num_sentences=3):
    # 텍스트에서 구두점 제거 및 소문자로 변환
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    # 단어 토큰화
    words = word_tokenize(text)
    
    # 단어 빈도 계산
    word_freq = Counter(words)
    
    # 가장 빈도가 높은 단어 추출
    top_words = word_freq.most_common(num_sentences)
    
    # 요약 생성
    summary = ' '.join(word for word, _ in top_words)
    
    return summary

