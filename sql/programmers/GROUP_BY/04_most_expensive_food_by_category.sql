-- # 문제 설명
-- # 다음은 식품의 정보를 담은 FOOD_PRODUCT 테이블입니다. 
-- FOOD_PRODUCT 테이블은 다음과 같으며 PRODUCT_ID, 
-- PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE는 
-- 식품 ID, 식품 이름, 식품코드, 식품분류, 식품 가격을 
-- 의미합니다.
-- # 문제
-- # FOOD_PRODUCT 테이블에서 식품분류별로 가격이 제일 비싼 
-- 식품의 분류, 가격, 이름을 조회하는 SQL문을 작성해주세요. 
-- 이때 식품분류가 '과자', '국', '김치', '식용유'인 경우만 
-- 출력시켜 주시고 결과는 식품 가격을 기준으로 내림차순 정렬해주세요.

-- 코드를 입력하세요
-- sol1. using MAX()
WITH MAX_layered AS (
    SELECT 
        CATEGORY, 
        PRICE, 
        MAX(PRICE) OVER (
            PARTITION BY CATEGORY
            ) AS MAX_PRICE, 
        PRODUCT_NAME
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
)
SELECT CATEGORY, MAX_PRICE, PRODUCT_NAME
FROM MAX_layered
WHERE PRICE = MAX_PRICE
ORDER BY MAX_PRICE DESC;


-- sol2. using RANK()
WITH ranked AS (
    SELECT CATEGORY, PRICE, PRODUCT_NAME,
           RANK() OVER (PARTITION BY CATEGORY ORDER BY PRICE DESC) AS rnk
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
)
SELECT CATEGORY, PRICE, PRODUCT_NAME
FROM ranked
WHERE rnk = 1
ORDER BY PRICE DESC;