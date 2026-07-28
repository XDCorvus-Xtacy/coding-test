'''
문제 설명
스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.
이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 
엄지손가락을 사용하는 규칙은 다음과 같습니다.

엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 
1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 
위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 
왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 
문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인지 오른손인지를 
나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
'''

# sol1. version 1 (using for)
def solution(numbers, hand):
    answer = []
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    left_hand = [1,4,7]
    right_hand = [3,6,9]
    middle = [2,5,8,0]
    L_loc = '*'
    R_loc = '#'
    
    for num in numbers:
        if num in left_hand:
            answer.append('L')
            L_loc = num
        elif num in right_hand:
            answer.append('R')
            R_loc = num
        elif num in middle:
            num_idx = []
            L_idx = []
            R_idx = []
            for row in range(4):
                for col in range(3):
                    if num == keypad[row][col]:
                        num_idx = [row, col]
                    if L_loc == keypad[row][col]:
                        L_idx = [row, col]
                    if R_loc == keypad[row][col]:
                        R_idx = [row, col]
            R_d = abs(num_idx[0]-R_idx[0]) + abs(num_idx[1]-R_idx[1])
            L_d = abs(num_idx[0]-L_idx[0]) + abs(num_idx[1]-L_idx[1])
            if R_d > L_d:
                answer.append('L')
                L_loc = num
            elif L_d > R_d:
                answer.append('R')
                R_loc = num
            elif L_d == R_d:
                if hand == 'right':
                    answer.append('R')
                    R_loc = num
                else:
                    answer.append('L')
                    L_loc = num

    return "".join(answer)

# sol2. version2 (using dict)
def solution(numbers, hand):
    answer = []
    keypad = {1: (0,0), 2: (0,1), 3: (0,2),
              4: (1,0), 5: (1,1), 6: (1,2),
              7: (2,0), 8: (2,1), 9: (2,2),
              '*': (3,0), 0: (3,1), '#': (3,2)}
    left_hand = [1,4,7]
    right_hand = [3,6,9]
    L_loc = keypad['*']
    R_loc = keypad['#']
    
    for num in numbers:
        use = ''
        if num in left_hand:
            use = 'L'
        elif num in right_hand:
            use = 'R'
        else:
            num_idx = keypad[num]
            R_d = abs(num_idx[0]-R_loc[0]) + abs(num_idx[1]-R_loc[1])
            L_d = abs(num_idx[0]-L_loc[0]) + abs(num_idx[1]-L_loc[1])
            if R_d > L_d:
                use = 'L'
            elif L_d > R_d:
                use = 'R'
            else:
                use = 'R' if hand == 'right' else 'L'
        answer.append(use)
        if use == 'L':
            L_loc = keypad[num]
        else:
            R_loc = keypad[num]

    return "".join(answer)