-- # 문제 설명
-- # 다음은 어느 한 서점에서 판매중인 도서들의 도서 정보(BOOK), 
-- 저자 정보(AUTHOR) 테이블입니다.
-- # BOOK 테이블은 각 도서의 정보를 담은 테이블로 아래와 같은 
-- 구조로 되어있습니다.
-- # AUTHOR 테이블은 도서의 저자의 정보를 담은 테이블로 아래와 
-- 같은 구조로 되어있습니다.
-- # 문제
-- # '경제' 카테고리에 속하는 도서들의 도서 ID(BOOK_ID), 
-- 저자명(AUTHOR_NAME), 출판일(PUBLISHED_DATE) 리스트를 
-- 출력하는 SQL문을 작성해주세요.
-- # 결과는 출판일을 기준으로 오름차순 정렬해주세요.

-- 코드를 입력하세요
SELECT B.BOOK_ID, A.AUTHOR_NAME, B.PUBLISHED_DATE
FROM BOOK B
INNER JOIN AUTHOR A
    ON B.AUTHOR_ID = A.AUTHOR_ID
WHERE CATEGORY = '경제'
ORDER BY PUBLISHED_DATE;