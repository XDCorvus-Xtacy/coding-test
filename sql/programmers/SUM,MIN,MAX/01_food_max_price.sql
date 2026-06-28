-- # 다음은 식품의 정보를 담은 FOOD_PRODUCT 테이블입니다. 
-- FOOD_PRODUCT 테이블은 다음과 같으며 PRODUCT_ID, PRODUCT_NAME, 
-- PRODUCT_CD, CATEGORY, PRICE는 식품 ID, 식품 이름, 식품 코드, 
-- 식품분류, 식품 가격을 의미합니다.
-- # 문제
-- # FOOD_PRODUCT 테이블에서 가격이 제일 비싼 식품의 식품 ID, 식품 이름, 
-- 식품 코드, 식품분류, 식품 가격을 조회하는 SQL문을 작성해주세요.

-- 코드를 입력하세요

-- sol1. using LIMIT (최고가 1개만 출력)
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1;

-- sol2. using Window Function (최고가들 출력)
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM (
    SELECT *, MAX(PRICE) OVER () AS max_price 
    FROM FOOD_PRODUCT
    ) AS T
WHERE PRICE = max_price
