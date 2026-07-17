'''
문제 설명
정수 배열 numbers가 주어집니다. numbers에서 서로 다른 
인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 
수를 배열에 오름차순으로 담아 return 하도록 solution 
함수를 완성해주세요.

제한사항
numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.
'''
def solution(numbers):
    answer = set()
    for k, v in enumerate(numbers):
        for i in range(k+1,len(numbers)):
            answer.add(v+numbers[i])
        
    return sorted(answer)

'''
아이디어
모든 합의 조합이니까 인덱스 0부터 시작 인덱스 기준으로
이후의 값들을 더한 것을 누적해나가면 됨.

불변값 끌어올리기
- 불변하는 변수를 반복문 밖에 배치하면 성능유도를 꾀할 수 있음.
- 여기에서 v는 두 번째 for문에서는 불변값임. 따라서 첫 번째 for문에서
- v로 할당하는 게 성능유도를 꾀할 수 있음
'''
