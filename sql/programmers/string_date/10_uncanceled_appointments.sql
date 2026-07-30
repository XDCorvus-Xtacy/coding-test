-- # 문제 설명
-- # 다음은 환자 정보를 담은 PATIENT 테이블과 의사 정보를 담은 DOCTOR 테이블, 
-- 그리고 진료 예약목록을 담은 APPOINTMENT에 대한 테이블입니다. PATIENT 테이블은 
-- 다음과 같으며 PT_NO, PT_NAME, GEND_CD, AGE, TLNO는 각각 환자번호, 
-- 환자이름, 성별코드, 나이, 전화번호를 의미합니다.
-- # DOCTOR 테이블은 다음과 같으며 DR_NAME, DR_ID, LCNS_NO, HIRE_YMD, 
-- MCDP_CD, TLNO는 각각 의사이름, 의사ID, 면허번호, 고용일자, 진료과코드, 
-- 전화번호를 나타냅니다.
-- # APPOINTMENT 테이블은 다음과 같으며 APNT_YMD, APNT_NO, PT_NO, 
-- MCDP_CD, MDDR_ID, APNT_CNCL_YN, APNT_CNCL_YMD는 각각 진료 예약일시, 
-- 진료예약번호, 환자번호, 진료과코드, 의사ID, 예약취소여부, 예약취소날짜를 나타냅니다.
-- # 문제
-- # PATIENT, DOCTOR 그리고 APPOINTMENT 테이블에서 2022년 4월 13일 
-- 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회하는 SQL문을 작성해주세요. 
-- 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목이 
-- 출력되도록 작성해주세요. 결과는 진료예약일시를 기준으로 오름차순 정렬해주세요.

-- 코드를 입력하세요
WITH cs_apt AS (
    SELECT *
    FROM APPOINTMENT
    WHERE MCDP_CD = 'CS'
        AND APNT_CNCL_YN = 'N'
        AND APNT_YMD >= '2022-04-13'
        AND APNT_YMD < '2022-04-14'
    ),
pt_info AS (
    SELECT C.APNT_NO, PT_NAME, C.PT_NO, MCDP_CD, APNT_YMD, MDDR_ID
    FROM cs_apt C
    INNER JOIN PATIENT P
        ON C.PT_NO = P.PT_NO
    )

SELECT APNT_NO, PT_NAME, PT_NO, P.MCDP_CD, DR_NAME, APNT_YMD
FROM pt_info P
INNER JOIN DOCTOR D
    ON P.MDDR_ID = D.DR_ID
ORDER BY APNT_YMD;
