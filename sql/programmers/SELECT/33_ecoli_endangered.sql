-- # 대장균들은 일정 주기로 분화하며, 분화를 시작한 개체를 부모 개체, 
-- 분화가 되어 나온 개체를 자식 개체라고 합니다.
-- # 다음은 실험실에서 배양한 대장균들의 정보를 담은 ECOLI_DATA 테이블입니다. 
-- ECOLI_DATA 테이블의 구조는 다음과 같으며, ID, PARENT_ID, 
-- SIZE_OF_COLONY, DIFFERENTIATION_DATE, GENOTYPE 은 각각 
-- 대장균 개체의 ID, 부모 개체의 ID, 개체의 크기, 분화되어 나온 날짜, 
-- 개체의 형질을 나타냅니다.
-- # 최초의 대장균 개체의 PARENT_ID 는 NULL 값입니다.
-- # 문제
-- # 각 세대별 자식이 없는 개체의 수(COUNT)와 세대(GENERATION)를 출력하는 
-- SQL문을 작성해주세요. 이때 결과는 세대에 대해 오름차순 정렬해주세요. 
-- 단, 모든 세대에는 자식이 없는 개체가 적어도 1개체는 존재합니다.

-- 코드를 작성해주세요
WITH RECURSIVE generations AS (
    -- 시작점(앵커): 1세대
    SELECT ID, 1 AS gen
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL

    UNION ALL

    -- 재귀: 자식 세대를 계속 붙여나감
    SELECT E.ID, G.gen + 1
    FROM ECOLI_DATA E
    INNER JOIN generations G 
        ON E.PARENT_ID = G.ID
)

-- sol1. using NOT IN
SELECT COUNT(gen) AS "COUNT", gen AS GENERATION 
FROM ECOLI_DATA E
INNER JOIN generations G
    ON E.ID = G.ID
WHERE E.ID NOT IN (SELECT PARENT_ID 
                   FROM ECOLI_DATA
                   WHERE PARENT_ID IS NOT NULL)
GROUP BY gen
ORDER BY gen;

-- sol2. using NOT EXISTS
SELECT G.gen AS GENERATION, COUNT(*) AS COUNT
FROM generations G
WHERE NOT EXISTS (
    SELECT 1 FROM ECOLI_DATA child WHERE child.PARENT_ID = G.ID
)
GROUP BY G.gen
ORDER BY G.gen;