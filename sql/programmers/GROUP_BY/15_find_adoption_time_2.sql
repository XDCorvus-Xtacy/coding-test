-- # 문제 설명
-- # ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물의 
-- 정보를 담은 테이블입니다. ANIMAL_OUTS 테이블 구조는 다음과 같으며, 
-- ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME는 
-- 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다.
-- # 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 
-- 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 
-- SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

-- 코드를 입력하세요
WITH RECURSIVE timelist AS (
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR + 1
    FROM timelist
    WHERE HOUR < 23
)

SELECT T.HOUR HOUR, COUNT(HOUR(DATETIME)) COUNT
FROM timelist T
LEFT JOIN ANIMAL_OUTS A
    ON T.HOUR = HOUR(A.DATETIME)
GROUP BY T.HOUR
ORDER BY T.HOUR