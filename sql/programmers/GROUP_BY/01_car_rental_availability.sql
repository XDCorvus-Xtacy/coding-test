-- # 문제 설명
-- # 다음은 어느 자동차 대여 회사의 자동차 대여 기록 정보를 담은 
-- CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블입니다. 
-- CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블은 아래와 같은 
-- 구조로 되어있으며, HISTORY_ID, CAR_ID, START_DATE, 
-- END_DATE 는 각각 자동차 대여 기록 ID, 자동차 ID, 대여 시작일, 
-- 대여 종료일을 나타냅니다.
-- # 문제
-- # CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 
-- 2022년 10월 16일에 대여 중인 자동차인 경우 '대여중' 이라고 표시하고, 
-- 대여 중이지 않은 자동차인 경우 '대여 가능'을 표시하는 컬럼(컬럼명: AVAILABILITY)
-- 을 추가하여 자동차 ID와 AVAILABILITY 리스트를 출력하는 SQL문을 작성해주세요. 
-- 이때 반납 날짜가 2022년 10월 16일인 경우에도 '대여중'으로 표시해주시고 결과는 
-- 자동차 ID를 기준으로 내림차순 정렬해주세요.

-- 코드를 입력하세요

-- sol1. using EXISTS
SELECT DISTINCT
    CAR_ID,
    CASE
        WHEN EXISTS (
            SELECT 1 
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY sub
            WHERE sub.CAR_ID = h.CAR_ID
              AND '2022-10-16' BETWEEN sub.START_DATE AND sub.END_DATE
        )
        THEN '대여중' ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
ORDER BY CAR_ID DESC;


-- sol2. using MAX()
SELECT
    CAR_ID,
    CASE
        WHEN MAX(CASE WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE 
                      THEN 1 ELSE 0 END) = 1
        THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;