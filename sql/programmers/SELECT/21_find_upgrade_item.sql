-- # 어느 한 게임에서 사용되는 아이템들은 업그레이드가 가능합니다.
-- # 'ITEM_A'->'ITEM_B'와 같이 업그레이드가 가능할 때
-- # 'ITEM_A'를 'ITEM_B' 의 PARENT 아이템,
-- # PARENT 아이템이 없는 아이템을 ROOT 아이템이라고 합니다.

-- # 예를 들어 'ITEM_A'->'ITEM_B'->'ITEM_C'와 같이 업그레이드가 가능한 아이템이 있다면
-- # 'ITEM_C'의 PARENT 아이템은 'ITEM_B'
-- # 'ITEM_B'의 PARENT 아이템은 'ITEM_A'
-- # ROOT 아이템은 'ITEM_A'가 됩니다.

-- # 아이템의 희귀도가 'RARE'인 아이템들의 모든 다음 업그레이드 아이템의 아이템 ID(ITEM_ID), 
-- 아이템 명(ITEM_NAME), 아이템의 희귀도(RARITY)를 출력하는 SQL 문을 작성해 주세요. 
-- 이때 결과는 아이템 ID를 기준으로 내림차순 정렬주세요.

-- 코드를 작성해주세요

-- method 1
SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY
FROM ITEM_INFO I
INNER JOIN ITEM_TREE T
    ON I.ITEM_ID = T.ITEM_ID
WHERE T.PARENT_ITEM_ID IN (SELECT ITEM_ID FROM ITEM_INFO WHERE RARITY = 'RARE')
ORDER BY I.ITEM_ID DESC;

-- method 2
SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO
WHERE ITEM_ID IN (
    SELECT ITEM_ID
    FROM ITEM_TREE
    WHERE PARENT_ITEM_ID (
        SELECT ITEM_ID
        FROM ITEM_INFO
        WHERE RARITY = 'RARE'
    )
)
ORDER BY ITEM_ID DESC;