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
-- # HR_DEPARTMENT, HR_EMPLOYEES, HR_GRADE 테이블에서 
-- 2022년도 한해 평가 점수가 가장 높은 사원 정보를 조회하려 합니다. 
-- 2022년도 평가 점수가 가장 높은 사원들의 점수, 사번, 성명, 직책, 
-- 이메일을 조회하는 SQL문을 작성해주세요.

-- # 2022년도의 평가 점수는 상,하반기 점수의 합을 의미하고, 
-- 평가 점수를 나타내는 컬럼의 이름은 SCORE로 해주세요.

-- 코드를 작성해주세요

-- sol1 using GROUP BY
WITH grade AS (
    SELECT EMP_NO, SUM(SCORE) SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
    ),
    high_emp AS (SELECT EMP_NO, SCORE
    FROM grade
    WHERE SCORE = (SELECT MAX(SCORE) FROM grade)
    )
 
SELECT H.SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM HR_EMPLOYEES E
INNER JOIN high_emp H
    ON E.EMP_NO = H.EMP_NO

-- sol2. using Window Function
WITH ranked AS (
    SELECT EMP_NO, SUM(SCORE) AS SCORE,
           RANK() OVER (ORDER BY SUM(SCORE) DESC) AS rnk
    FROM HR_GRADE
    WHERE YEAR = 2022
    GROUP BY EMP_NO
)
SELECT R.SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM ranked R
INNER JOIN HR_EMPLOYEES E ON E.EMP_NO = R.EMP_NO
WHERE R.rnk = 1
ORDER BY E.EMP_NO;