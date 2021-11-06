"""
https://programmers.co.kr/learn/courses/30/lessons/59045

- 문제
ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.
보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 보호소에 들어올 당시에는 중성화1되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.

- ANIMAL_INS
ANIMAL_ID	ANIMAL_TYPE	DATETIME	INTAKE_CONDITION	NAME	SEX_UPON_INTAKE
A367438	Dog	2015-09-10 16:01:00	Normal	Cookie	Spayed Female
A382192	Dog	2015-03-13 13:14:00	Normal	Maxwell 2	Intact Male
A405494	Dog	2014-05-16 14:17:00	Normal	Kaila	Spayed Female
A410330	Dog	2016-09-11 14:09:00	Sick	Chewy	Intact Female

- ANIMAL_OUTS
ANIMAL_ID	ANIMAL_TYPE	DATETIME	NAME	SEX_UPON_OUTCOME
A367438	Dog	2015-09-12 13:30:00	Cookie	Spayed Female
A382192	Dog	2015-03-16 13:46:00	Maxwell 2	Neutered Male
A405494	Dog	2014-05-20 11:44:00	Kaila	Spayed Female
A410330	Dog	2016-09-13 13:46:00	Chewy	Spayed Female

- 출력
ANIMAL_ID	ANIMAL_TYPE	NAME
A382192	Dog	Maxwell 2
A410330	Dog	Chewy
"""

SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME
FROM ANIMAL_INS AS INS
    JOIN ANIMAL_OUTS AS OUTS
    ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.SEX_UPON_INTAKE like '%Intact%' AND regexp_like(OUTS.SEX_UPON_OUTCOME,'Spayed|Neutered')
ORDER BY INS.ANIMAL_ID