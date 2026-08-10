'''
문제 설명
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 
서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 
개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 
개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 
return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 
진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
'''
def solution(progresses, speeds):
    progresses = progresses[:]
    sppeds = speeds[:]

    answer = []
    days = (100-progresses[0]+speeds[0]-1)//speeds[0]
    features = 0
    while progresses:
        progress = progresses.pop(0)
        speed = speeds.pop(0)
        if speed*days+progress >= 100:
            features += 1
            continue
        answer.append(features)
        features = 1
        days = (100 - progress + speed - 1)//speed
    answer.append(features)
    return answer


def solution(progresses, speeds):
    # 1단계: 각 기능이 완성되는 데 걸리는 날 (순회 1회)
    days = [(100 - p + s - 1) // s for p, s in zip(progresses, speeds)]

    # 2단계: 앞에서부터 훑으며 묶기 (순회 1회)
    answer = []
    deadline = days[0]   # 현재 묶음의 기준일
    count = 0

    for d in days:
        if d <= deadline:
            count += 1               # 기준일 안에 끝나니 같이 배포
        else:
            answer.append(count)     # 현재 묶음 확정
            deadline = d             # 이 기능이 새 기준
            count = 1                # 자기 자신이 첫 번째

    answer.append(count)             # 마지막 묶음 처리
    return answer