-- # 문제 설명
-- # HR_DEPARTMENT 테이블은 회사의 부서 정보를 담은 테이블입니다. 
-- HR_DEPARTMENT 테이블의 구조는 다음과 같으며 DEPT_ID, 
-- DEPT_NAME_KR, DEPT_NAME_EN, LOCATION은 각각 부서 ID, 
-- 국문 부서명, 영문 부서명, 부서 위치를 의미합니다.
-- # HR_EMPLOYEES 테이블은 회사의 사원 정보를 담은 테이블입니다. 
-- HR_EMPLOYEES 테이블의 구조는 다음과 같으며 EMP_NO, EMP_NAME, 
-- DEPT_ID, POSITION, EMAIL, COMP_TEL, HIRE_DATE, SAL은 
-- 각각 사번, 성명, 부서 ID, 직책, 이메일, 전화번호, 입사일, 연봉을 
-- 의미합니다.
-- # HR_GRADE 테이블은 2022년 사원의 평가 정보를 담은 테이블입니다. 
-- HR_GRADE의 구조는 다음과 같으며 EMP_NO, YEAR, HALF_YEAR, 
-- SCORE는 각각 사번, 연도, 반기, 평가 점수를 의미합니다.
-- # 문제
-- # HR_DEPARTMENT, HR_EMPLOYEES, HR_GRADE 테이블을 이용해 
-- 사원별 성과금 정보를 조회하려합니다. 평가 점수별 등급과 등급에 따른 
-- 성과금 정보가 아래와 같을 때, 사번, 성명, 평가 등급, 성과금을 
-- 조회하는 SQL문을 작성해주세요.

-- # 평가등급의 컬럼명은 GRADE로, 성과금의 컬럼명은 BONUS로 해주세요.
-- # 결과는 사번 기준으로 오름차순 정렬해주세요.

-- 코드를 작성해주세요
WITH grade AS (
    SELECT EMP_NO, SUM(SCORE)/2 AS SCORE
    FROM HR_GRADE
    WHERE YEAR = 2022
    GROUP BY EMP_NO
),
graded AS (
    SELECT H.EMP_NO, H.EMP_NAME, H.SAL,
        CASE
            WHEN G.SCORE >= 96 THEN 'S'
            WHEN G.SCORE >= 90 THEN 'A'
            WHEN G.SCORE >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE
    FROM HR_EMPLOYEES H
    INNER JOIN grade G ON H.EMP_NO = G.EMP_NO
)

SELECT EMP_NO, EMP_NAME, GRADE,
    CASE GRADE
        WHEN 'S' THEN SAL * 20 / 100
        WHEN 'A' THEN SAL * 15 / 100
        WHEN 'B' THEN SAL * 10 / 100
        ELSE 0
    END AS BONUS
FROM graded
ORDER BY EMP_NO;