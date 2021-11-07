/*
고양이와 개는 몇 마리 있을까
동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.
*/
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE)
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE

/*
동명 동물 수 찾기
동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.
*/
SELECT NAME, COUNT(NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT(NAME) > 1
ORDER BY NAME

/*
입양 시각 구하기(1)
보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
*/
SELECT HOUR(DATETIME) AS HOUR, COUNT(*)
FROM ANIMAL_INS
GROUP BY HOUR
HAVING HOUR >= 9 AND HOUR < 20
ORDER BY HOUR

/*
입양 시각 구하기(2)
보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
*/
WITH RECURSIVE
    TIME AS
    (
    SELECT 0 AS HOUR
UNION ALL
    SELECT HOUR + 1
    FROM TIME
    WHERE HOUR < 23)
SELECT TIME.HOUR, COUNT(OUTS.ANIMAL_ID)
FROM TIME
    LEFT JOIN ANIMAL_OUTS AS OUTS
    ON TIME.HOUR = HOUR(OUTS.DATETIME)
GROUP BY TIME.HOUR