-- # 문제 설명
-- # ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. 
-- ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, 
-- DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 
-- 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 
-- 여부를 나타냅니다.
-- # ANIMAL_INS 테이블에 등록된 모든 레코드에 대해, 각 동물의 아이디와 이름, 
-- 들어온 날짜를 조회하는 SQL문을 작성해주세요. 이때 결과는 아이디 순으로 조회해야 
-- 합니다.

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATE(DATETIME) 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

/*
자주 쓰는 포맷 문자
%Y  4자리 연도 (2022)    %y  2자리 (22)
%m  월 2자리 (01)        %c  월 (1)
%d  일 2자리 (01)        %e  일 (1)
%H  24시 (14)            %h  12시 (02)
%i  분 (30)              %s  초 (00)
%W  요일명 (Monday)      %p  AM/PM
*/