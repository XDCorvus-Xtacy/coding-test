-- # 문제 설명
-- # 다음은 고객의 정보를 담은 MEMBER_PROFILE테이블과 식당의 리뷰 
-- 정보를 담은 REST_REVIEW 테이블입니다. MEMBER_PROFILE 테이블은 
-- 다음과 같으며 MEMBER_ID, MEMBER_NAME, TLNO, GENDER, 
-- DATE_OF_BIRTH는 회원 ID, 회원 이름, 회원 연락처, 성별, 생년월일을 
-- 의미합니다.
-- # REST_REVIEW 테이블은 다음과 같으며 REVIEW_ID, REST_ID, 
-- MEMBER_ID, REVIEW_SCORE, REVIEW_TEXT,REVIEW_DATE는 각각 
-- 리뷰 ID, 식당 ID, 회원 ID, 점수, 리뷰 텍스트, 리뷰 작성일을 의미합니다.
-- # 문제
-- # MEMBER_PROFILE와 REST_REVIEW 테이블에서 리뷰를 가장 많이 작성한 
-- 회원의 리뷰들을 조회하는 SQL문을 작성해주세요. 회원 이름, 리뷰 텍스트, 
-- 리뷰 작성일이 출력되도록 작성해주시고, 결과는 리뷰 작성일을 기준으로 
-- 오름차순, 리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순 정렬해주세요.

-- 코드를 입력하세요

-- 문제 정답
SELECT M.MEMBER_NAME, R.REVIEW_TEXT, R.REVIEW_DATE
FROM REST_REVIEW R
INNER JOIN MEMBER_PROFILE M
    ON R.MEMBER_ID = M.MEMBER_ID
WHERE R.MEMBER_ID = (
    SELECT MEMBER_ID
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT;


-- 실질적 정답
WITH review_cnt AS (
    SELECT R.MEMBER_ID, COUNT(*) AS cnt
    FROM REST_REVIEW R
    INNER JOIN MEMBER_PROFILE M ON R.MEMBER_ID = M.MEMBER_ID
    GROUP BY R.MEMBER_ID
)
SELECT M.MEMBER_NAME, R.REVIEW_TEXT, R.REVIEW_DATE
FROM REST_REVIEW R
INNER JOIN MEMBER_PROFILE M ON R.MEMBER_ID = M.MEMBER_ID
WHERE R.MEMBER_ID = (
    SELECT MEMBER_ID FROM review_cnt
    WHERE cnt = (SELECT MAX(cnt) FROM review_cnt)
)
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT;

-- 문제의 오류
-- 당연히 공동순위를 다루는 부분이 없으면 공동순위 모두를 출력해야 하는데
-- 이 문제 정답을 보면 그렇지 않음. 즉, 문제가 잘못됐음.