-- # 낚시앱에서 사용하는 FISH_INFO 테이블은 잡은 물고기들의 
-- 정보를 담고 있습니다. FISH_INFO 테이블의 구조는 다음과 
-- 같으며 ID, FISH_TYPE, LENGTH, TIME은 각각 잡은 물고기의 
-- ID, 물고기의 종류(숫자), 잡은 물고기의 길이(cm), 물고기를 
-- 잡은 날짜를 나타냅니다.
-- # 단, 잡은 물고기의 길이가 10cm 이하일 경우에는 LENGTH 가 
-- NULL 이며, LENGTH 에 NULL 만 있는 경우는 없습니다.
-- # FISH_NAME_INFO 테이블은 물고기의 이름에 대한 정보를 담고 
-- 있습니다. FISH_NAME_INFO 테이블의 구조는 다음과 같으며, 
-- FISH_TYPE, FISH_NAME 은 각각 물고기의 종류(숫자), 
-- 물고기의 이름(문자) 입니다.
-- # 물고기 종류 별로 가장 큰 물고기의 ID, 물고기 이름, 길이를 
-- 출력하는 SQL 문을 작성해주세요.
-- # 물고기의 ID 컬럼명은 ID, 이름 컬럼명은 FISH_NAME, 길이 
-- 컬럼명은 LENGTH로 해주세요.
-- # 결과는 물고기의 ID에 대해 오름차순 정렬해주세요.
-- # 단, 물고기 종류별 가장 큰 물고기는 1마리만 있으며 10cm 
-- 이하의 물고기가 가장 큰 경우는 없습니다.

-- 코드를 작성해주세요

-- sol1. using correlated subquery
-- 이렇게 풀 수도 있지만, 효율적인 방법은 아님.(상관 서브쿼리는 무거움)
SELECT I.ID, N.FISH_NAME, I.LENGTH
FROM FISH_INFO I
INNER JOIN FISH_NAME_INFO N ON I.FISH_TYPE = N.FISH_TYPE
WHERE I.LENGTH = (
    SELECT MAX(sub.LENGTH)
    FROM FISH_INFO sub
    WHERE sub.FISH_TYPE = I.FISH_TYPE    -- ← 같은 종류끼리만!
)
ORDER BY I.ID;


-- sol2. using Window Function (rank)
SELECT ID, FISH_NAME, LENGTH
FROM (SELECT I.ID, N.FISH_NAME, I.LENGTH, 
      RANK() OVER (PARTITION BY I.FISH_TYPE 
                   ORDER BY I.LENGTH DESC) AS rnk
     FROM FISH_INFO I
     INNER JOIN FISH_NAME_INFO N
        ON I.FISH_TYPE = N.FISH_TYPE
     ) AS T
WHERE rnk = 1
ORDER BY ID;