-- # 문제 설명
-- # 낚시앱에서 사용하는 FISH_INFO 테이블은 잡은 물고기들의 
-- 정보를 담고 있습니다. FISH_INFO 테이블의 구조는 다음과 같으며 
-- ID, FISH_TYPE, LENGTH, TIME은 각각 잡은 물고기의 ID, 
-- 물고기의 종류(숫자), 잡은 물고기의 길이(cm), 물고기를 잡은 
-- 날짜를 나타냅니다.
-- # 단, 잡은 물고기의 길이가 10cm 이하일 경우에는 LENGTH 가 
-- NULL 이며, LENGTH 에 NULL 만 있는 경우는 없습니다.
-- # 문제
-- # FISH_INFO에서 평균 길이가 33cm 이상인 물고기들을 종류별로 
-- 분류하여 잡은 수, 최대 길이, 물고기의 종류를 출력하는 SQL문을 
-- 작성해주세요. 결과는 물고기 종류에 대해 오름차순으로 정렬해주시고, 
-- 10cm이하의 물고기들은 10cm로 취급하여 평균 길이를 구해주세요.

-- # 컬럼명은 물고기의 종류 'FISH_TYPE', 잡은 수 'FISH_COUNT', 
-- 최대 길이 'MAX_LENGTH'로 해주세요.

-- 코드를 작성해주세요
WITH rm_null AS (
    SELECT FISH_TYPE, IFNULL(LENGTH, 10) LENGTH
    FROM FISH_INFO
    )

SELECT COUNT(*) FISH_COUNT, 
       MAX(LENGTH) MAX_LENGTH,
       FISH_TYPE
FROM rm_null
GROUP BY FISH_TYPE
HAVING AVG(LENGTH) >= 33
ORDER BY FISH_TYPE;
