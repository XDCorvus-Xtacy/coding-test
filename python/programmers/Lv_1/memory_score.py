'''
사진 속 인물들의 그리움 점수를 모두 더한 값이 그 사진의 추억 점수입니다.
그리움 점수가 없는 인물은 0점으로 칩니다.
name(이름), yearning(그리움 점수, name과 같은 순서), photo(사진별 인물 이름)가 주어질 때,
사진들의 추억 점수를 photo 순서대로 배열에 담아 return 하세요.

[제한사항]
- name과 yearning의 길이는 3 이상 100 이하이며 서로 같음
- name의 원소는 3~7글자 소문자, 중복 없음
- yearning의 원소는 1 이상 100 이하
- photo의 길이는 3 이상 100 이하
- photo[i]의 길이는 1 이상 100 이하, 한 사진 안에서 이름 중복 없음
'''
def solution(name, yearning, photo):
    answer = []
    score = {}
    for k, v in zip(name, yearning):
        score[k] = v
        
    for people in photo:
        total = 0
        for person in people:
            total += score.get(person, 0)
        answer.append(total)
        
    return answer