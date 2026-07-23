-- # 문제 설명
-- # ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. 
-- ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, 
-- DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 
-- 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 
-- 나타냅니다.
-- # ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. 
-- ANIMAL_OUTS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, 
-- NAME, SEX_UPON_OUTCOME는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 
-- 중성화 여부를 나타냅니다. ANIMAL_OUTS 테이블의 ANIMAL_ID는 ANIMAL_INS의 
-- ANIMAL_ID의 외래 키입니다.
-- # 보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 보호소에 들어올 당시에는 
-- 중성화되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 
-- 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.

-- 코드를 입력하세요
WITH intact AS (
    SELECT *
    FROM ANIMAL_INS
    WHERE SEX_UPON_INTAKE LIKE 'Intact%'
    )

SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
FROM intact I
INNER JOIN ANIMAL_OUTS O
    ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE SEX_UPON_OUTCOME LIKE 'Spayed%'
    OR SEX_UPON_OUTCOME LIKE 'Neutered%'
ORDER BY O.ANIMAL_ID;

-- WHERE 조건을 
-- NOT LIKE 'Intact%'
-- 로 작성해도 됨