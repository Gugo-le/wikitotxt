import requests
from bs4 import BeautifulSoup
import time

# 네이버 국어사전 URL
base_url = "https://ko.dict.naver.com/#/search?query={word}"

# 크롤링할 단어 목록 (예시)
words_to_crawl = ['사랑', '행복', '기쁨', '슬픔']  # 여기에서 원하는 단어들을 추가

# 파일로 저장
with open('naver_korean_dict_words.txt', 'w', encoding='utf-8') as file:
    for word in words_to_crawl:
        # URL에 단어를 삽입하여 요청을 보냄
        response = requests.get(base_url.format(word=word))
        response.encoding = 'utf-8'
        
        if response.status_code == 200:
            # BeautifulSoup으로 HTML 파싱
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 예시: 'mean' 클래스 내에 있는 뜻을 추출 (HTML 구조에 맞게 조정 필요)
            meaning_section = soup.find('span', {'class': 'fnt_k05'})
            if meaning_section:
                meaning = meaning_section.get_text(strip=True)
                file.write(f"{word}\n")
            else:
                file.write(f"{word}\n")
        else:
            file.write(f"{word}\n")
        
        # 요청 간 시간 간격을 둬서 서버에 부담을 줄임
        time.sleep(1)

print("단어 크롤링 완료!")