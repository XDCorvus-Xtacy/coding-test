-- # 대장균들은 일정 주기로 분화하며, 분화를 시작한 개체를 부모 개체, 
-- 분화가 되어 나온 개체를 자식 개체라고 합니다.
-- # 다음은 실험실에서 배양한 대장균들의 정보를 담은 ECOLI_DATA 테이블입니다. 
-- ECOLI_DATA 테이블의 구조는 다음과 같으며, ID, PARENT_ID, SIZE_OF_COLONY, 
-- DIFFERENTIATION_DATE, GENOTYPE 은 각각 대장균 개체의 ID, 부모 개체의 ID, 
-- 개체의 크기, 분화되어 나온 날짜, 개체의 형질을 나타냅니다.
-- # 최초의 대장균 개체의 PARENT_ID 는 NULL 값입니다.
-- # 3세대의 대장균의 ID(ID) 를 출력하는 SQL 문을 작성해주세요. 이때 결과는 대장균의 
-- ID 에 대해 오름차순 정렬해주세요.

-- 코드를 작성해주세요
-- 3세대 = 2세대의 자식
-- 2세대 = 1세대의 자식
-- 1세대 = PARENT_ID IS NULL

-- method 1. using subquery
SELECT ID
FROM ECOLI_DATA
WHERE PARENT_ID IN (SELECT ID 
                    FROM ECOLI_DATA 
                    WHERE PARENT_ID IN 
                        (SELECT ID 
                         FROM ECOLI_DATA 
                         WHERE PARENT_ID IS NULL))
ORDER BY ID;


-- method 2. using subquery, CTE
WITH gen1 AS (
    SELECT ID FROM ECOLI_DATA WHERE PARENT_ID IS NULL
),
gen2 AS (
    SELECT ID FROM ECOLI_DATA WHERE PARENT_ID IN (SELECT ID FROM gen1)
)
SELECT ID
FROM ECOLI_DATA
WHERE PARENT_ID IN (SELECT ID FROM gen2)
ORDER BY ID;


-- method 3. using JOIN
SELECT C.ID
FROM ECOLI_DATA A            -- 1세대
INNER JOIN ECOLI_DATA B 
    ON B.PARENT_ID = A.ID    -- B는 A의 자식 = 2세대
INNER JOIN ECOLI_DATA C 
    ON C.PARENT_ID = B.ID    -- C는 B의 자식 = 3세대
WHERE A.PARENT_ID IS NULL    -- A가 최초세대(1세대)
ORDER BY C.ID;


-- more: recursive CTE
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
SELECT ID
FROM generations
WHERE gen = 3
ORDER BY ID;