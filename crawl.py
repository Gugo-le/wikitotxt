import requests
from bs4 import BeautifulSoup
import time

def crawl_korean_dictionary(output_file, base_url, num_pages=10):
    """
    표준국어대사전 단어 크롤링 함수
    :param output_file: 결과를 저장할 txt 파일 이름
    :param base_url: 크롤링 대상 URL
    :param num_pages: 크롤링할 페이지 수
    """
    with open(output_file, "w", encoding="utf-8") as file:
        for page in range(1, num_pages + 1):
            url = f"{base_url}?page={page}"
            try:
                response = requests.get(url)
                response.raise_for_status()  # 요청 에러가 있으면 예외 발생
                soup = BeautifulSoup(response.text, "html.parser")

                # 단어 목록 추출 (CSS 선택자 수정 필요)
                words = soup.select(".word_list .word")  # 사이트에 맞는 CSS 선택자 사용
                if not words:
                    print(f"Page {page}: 단어를 찾을 수 없음")
                    continue

                for word in words:
                    word_text = word.get_text(strip=True)
                    file.write(word_text + "\n")

                print(f"Page {page} 크롤링 완료")
                time.sleep(1)  # 서버에 과부하를 주지 않도록 딜레이 추가

            except requests.exceptions.RequestException as e:
                print(f"Error on page {page}: {e}")
                continue

if __name__ == "__main__":
    # 표준국어대사전의 실제 URL로 교체 필요
    BASE_URL = "https://stdict.korean.go.kr/search/wordSearchList.do"
    OUTPUT_FILE = "korean_dictionary.txt"
    NUM_PAGES = 10  # 크롤링할 페이지 수

    print("표준국어대사전 크롤링 시작...")
    crawl_korean_dictionary(OUTPUT_FILE, BASE_URL, NUM_PAGES)
    print(f"크롤링 완료! 결과는 '{OUTPUT_FILE}'에 저장되었습니다.")
