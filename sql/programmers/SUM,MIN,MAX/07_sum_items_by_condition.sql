-- # 다음은 어느 한 게임에서 사용되는 아이템들의 아이템 정보를 담은 
-- ITEM_INFO 테이블입니다. ITEM_INFO 테이블은 다음과 같으며, 
-- ITEM_ID, ITEM_NAME, RARITY, PRICE는 각각 아이템 ID, 
-- 아이템 명, 아이템의 희귀도, 아이템의 가격을 나타냅니다.
-- # ITEM_INFO 테이블에서 희귀도가 'LEGEND'인 아이템들의 가격의 
-- 총합을 구하는 SQL문을 작성해 주세요. 이때 컬럼명은 'TOTAL_PRICE'
-- 로 지정해 주세요.

-- 코드를 작성해주세요
SELECT SUM(PRICE) AS TOTAL_PRICE
FROM ITEM_INFO
WHERE RARITY = 'LEGEND'