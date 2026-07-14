-- # 문제 설명
-- # 낚시앱에서 사용하는 FISH_INFO 테이블은 잡은 물고기들의 
-- 정보를 담고 있습니다. FISH_INFO 테이블의 구조는 다음과 같으며 
-- ID, FISH_TYPE, LENGTH, TIME은 각각 잡은 물고기의 ID, 
-- 물고기의 종류(숫자), 잡은 물고기의 길이(cm), 물고기를 잡은 
-- 날짜를 나타냅니다.
-- # 단, 잡은 물고기의 길이가 10cm 이하일 경우에는 LENGTH 가 
-- NULL 이며, LENGTH 에 NULL 만 있는 경우는 없습니다.
-- # 문제
-- # 월별 잡은 물고기의 수와 월을 출력하는 SQL문을 작성해주세요.

-- # 잡은 물고기 수 컬럼명은 FISH_COUNT, 월 컬럼명은 MONTH로 
-- 해주세요.
-- # 결과는 월을 기준으로 오름차순 정렬해주세요.
-- # 단, 월은 숫자형태 (1~12) 로 출력하며 9 이하의 숫자는 두 
-- 자리로 출력하지 않습니다. 잡은 물고기가 없는 월은 출력하지 
-- 않습니다.

-- 코드를 작성해주세요
SELECT COUNT(*) FISH_COUNT, MONTH(TIME) MONTH
FROM FISH_INFO
GROUP BY MONTH(TIME)
ORDER BY MONTH(TIME)


-- 추가학습(재귀 CTE)
WITH RECURSIVE monthly AS (
    SELECT 1 AS MONTH
    UNION ALL
    SELECT MONTH + 1
    FROM monthly
    WHERE MONTH < 12
)

SELECT M.MONTH, COUNT(FISH_TYPE)
FROM monthly M
LEFT JOIN FISH_INFO I
    ON MONTH(I.TIME) = M.MONTH
GROUP BY M.MONTH
ORDER BY M.MONTH


-- 추가학습(월별 누적)
WITH RECURSIVE monthly AS (
    SELECT 1 AS MONTH
    UNION ALL
    SELECT MONTH + 1
    FROM monthly
    WHERE MONTH < 12
)

SELECT M.MONTH, COUNT(FISH_TYPE) FISH_COUNT,
        SUM(COUNT(FISH_TYPE)) OVER (ORDER BY M.MONTH)
FROM monthly M
LEFT JOIN FISH_INFO I
    ON MONTH(I.TIME) = M.MONTH
GROUP BY M.MONTH
ORDER BY M.MONTH