-- # 문제 설명
-- # 다음은 어느 한 서점에서 판매중인 도서들의 도서 정보(BOOK), 
-- 저자 정보(AUTHOR) 테이블입니다.
-- # BOOK 테이블은 각 도서의 정보를 담은 테이블로 아래와 같은 
-- 구조로 되어있습니다.
-- # AUTHOR 테이블은 도서의 저자의 정보를 담은 테이블로 아래와 같은 
-- 구조로 되어있습니다.
-- # BOOK_SALES 테이블은 각 도서의 날짜 별 판매량 정보를 담은 테이블로 
-- 아래와 같은 구조로 되어있습니다.
-- # 문제
-- # 2022년 1월의 도서 판매 데이터를 기준으로 
-- 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여, 
-- 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 
-- 매출액(SALES) 리스트를 출력하는 SQL문을 작성해주세요.
-- # 결과는 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 
-- 정렬해주세요.

-- 코드를 입력하세요
-- 2022년 1월 도서 판매 데이터 책 별 판매량
WITH S AS (
    SELECT BOOK_ID, SUM(SALES) AS TOTAL_SALES
    FROM BOOK_SALES
    WHERE YEAR(SALES_DATE) = 2022 
      AND MONTH(SALES_DATE) = 1
    GROUP BY BOOK_ID
),
-- 저자 별, 카테고리 별 판매량
BI AS (
    SELECT 
        B.AUTHOR_ID, 
        B.CATEGORY, 
        SUM(TOTAL_SALES * B.PRICE) AS TOTAL_SALES
    FROM BOOK B
    INNER JOIN S
        ON B.BOOK_ID = S.BOOK_ID
    GROUP BY B.AUTHOR_ID, B.CATEGORY
)


SELECT 
    BI.AUTHOR_ID, 
    A.AUTHOR_NAME, 
    BI.CATEGORY, 
    BI.TOTAL_SALES
FROM BI
INNER JOIN AUTHOR A
    ON A.AUTHOR_ID = BI.AUTHOR_ID
ORDER BY BI.AUTHOR_ID, BI.CATEGORY DESC;

