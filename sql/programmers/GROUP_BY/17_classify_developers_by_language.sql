-- # 문제 설명
-- # SKILLCODES 테이블은 개발자들이 사용하는 프로그래밍 언어에 대한 
-- 정보를 담은 테이블입니다. SKILLCODES 테이블의 구조는 다음과 같으며, 
-- NAME, CATEGORY, CODE는 각각 스킬의 이름, 스킬의 범주, 스킬의 
-- 코드를 의미합니다. 스킬의 코드는 2진수로 표현했을 때 각 bit로 구분될 
-- 수 있도록 2의 제곱수로 구성되어 있습니다.
-- # DEVELOPERS 테이블은 개발자들의 프로그래밍 스킬 정보를 담은 테이블입니다. 
-- DEVELOPERS 테이블의 구조는 다음과 같으며, ID, FIRST_NAME, 
-- LAST_NAME, EMAIL, SKILL_CODE는 각각 개발자의 ID, 이름, 성, 
-- 이메일, 스킬 코드를 의미합니다. SKILL_CODE 컬럼은 INTEGER 타입이고, 
-- 2진수로 표현했을 때 각 bit는 SKILLCODES 테이블의 코드를 의미합니다.
-- # 예를 들어 어떤 개발자의 SKILL_CODE가 400 (=b'110010000')이라면, 
-- 이는 SKILLCODES 테이블에서 CODE가 256 (=b'100000000'), 
-- 128 (=b'10000000'), 16 (=b'10000') 에 해당하는 스킬을 가졌다는 
-- 것을 의미합니다.

-- # 문제
-- # DEVELOPERS 테이블에서 GRADE별 개발자의 정보를 조회하려 합니다. 
-- GRADE는 다음과 같이 정해집니다.

-- # A : Front End 스킬과 Python 스킬을 함께 가지고 있는 개발자
-- # B : C# 스킬을 가진 개발자
-- # C : 그 외의 Front End 개발자
-- # GRADE가 존재하는 개발자의 GRADE, ID, EMAIL을 조회하는 SQL 
-- 문을 작성해 주세요.

-- # 결과는 GRADE와 ID를 기준으로 오름차순 정렬해 주세요.

-- 코드를 작성해주세요

WITH masks AS (
    SELECT
        (SELECT SUM(CODE) 
        FROM SKILLCODES 
        WHERE CATEGORY = 'Front End') 
        AS front_end,

        (SELECT CODE 
        FROM SKILLCODES 
        WHERE NAME = 'Python')
        AS python,

        (SELECT CODE 
        FROM SKILLCODES 
        WHERE NAME = 'C#')
        AS csharp
)

SELECT
    CASE
        WHEN (D.SKILL_CODE & m.front_end) != 0
         AND (D.SKILL_CODE & m.python)    != 0  THEN 'A'
        WHEN (D.SKILL_CODE & m.csharp)    != 0  THEN 'B'
        WHEN (D.SKILL_CODE & m.front_end) != 0  THEN 'C'
    END AS GRADE,
    D.ID,
    D.EMAIL
FROM DEVELOPERS D
CROSS JOIN masks m
WHERE (D.SKILL_CODE & m.front_end) != 0
   OR (D.SKILL_CODE & m.csharp)    != 0
ORDER BY GRADE, D.ID;