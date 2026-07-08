###################################################

# Day20. math, simulation, strings, arithmetic

###################################################
'''
문제 설명
2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 
직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], 
[x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때, 직사각형의 
넓이를 return 하도록 solution 함수를 완성해보세요.

제한사항
dots의 길이 = 4
dots의 원소의 길이 = 2
-256 < dots[i]의 원소 < 256
잘못된 입력은 주어지지 않습니다.
'''
def solution(dots):
    xs = [d[0] for d in dots]      # x좌표들
    ys = [d[1] for d in dots]      # y좌표들
    width = max(xs) - min(xs)      # 가로 = x 범위
    height = max(ys) - min(ys)     # 세로 = y 범위
    return width * height

###################################################
'''
문제 설명
머쓱이는 RPG게임을 하고 있습니다. 게임에는 up, down, left, 
right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 
한 칸씩 이동합니다. 예를 들어 [0,0]에서 up을 누른다면 캐릭터의 
좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 
[-1, 0], right를 누른다면 [1, 0]입니다. 머쓱이가 입력한 
방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 
캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 
좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.

[0, 0]은 board의 정 중앙에 위치합니다. 예를 들어 board의 가로 
크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 
[4, 0]까지 이동할 수 있습니다.

제한사항
board은 [가로 크기, 세로 크기] 형태로 주어집니다.
board의 가로 크기와 세로 크기는 홀수입니다.
board의 크기를 벗어난 방향키 입력은 무시합니다.
0 ≤ keyinput의 길이 ≤ 50
1 ≤ board[0] ≤ 99
1 ≤ board[1] ≤ 99
keyinput은 항상 up, down, left, right만 주어집니다.
'''
def solution(keyinput, board):
    move = {"left": -1, 
            "right": 1, 
            "up": 1, 
            "down": -1}
    x, y = 0, 0
    x_max = (board[0]-1)//2
    y_max = (board[1]-1)//2
    for key in keyinput:
        if key == "left" or key == "right":
            x += move[key]
            if x > x_max or x < -x_max:
                x -= move[key]
        if key == "up" or key == "down":
            y += move[key]
            if y > y_max or y < -y_max:
                y -= move[key]
    return [x, y]


# 변화량을 기준으로 좌표 구하기
def solution(keyinput, board):
    move = {"left": (-1, 0), 
            "right": (1, 0), 
            "up": (0, 1), 
            "down": (0, -1)}
    x, y = 0, 0
    x_max = (board[0]-1)//2
    y_max = (board[1]-1)//2
    for key in keyinput:
        dx, dy = move[key]              # 방향의 x,y 변화량
        if abs(x + dx) <= x_max and abs(y + dy) <= y_max:
            x += dx
            y += dy
    return [x, y]

###################################################
'''
문제 설명
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 
solution 함수를 완성해주세요.

제한사항
-10,000 ≤ numbers의 원소 ≤ 10,000
2 ≤ numbers 의 길이 ≤ 100
'''
def solution(numbers):
    numbers.sort()
    return max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])

###################################################
'''
문제 설명
한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 
다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 덧셈으로 
이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 
더한 결괏값을 문자열로 return 하도록 solution 함수를 
완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.

제한사항
0 < polynomial에 있는 수 < 100
polynomial에 변수는 'x'만 존재합니다.
polynomial은 양의 정수, 공백, ‘x’, ‘+'로 이루어져 있습니다.
항과 연산기호 사이에는 항상 공백이 존재합니다.
공백은 연속되지 않으며 시작이나 끝에는 공백이 없습니다.
하나의 항에서 변수가 숫자 앞에 오는 경우는 없습니다.
" + 3xx + + x7 + "와 같은 잘못된 입력은 주어지지 않습니다.
0으로 시작하는 수는 없습니다.
문자와 숫자 사이의 곱하기는 생략합니다.
polynomial에는 일차 항과 상수항만 존재합니다.
계수 1은 생략합니다.
결괏값에 상수항은 마지막에 둡니다.
0 < polynomial의 길이 < 50
'''
def solution(polynomial):
    token_list = polynomial.split(" + ")
    x = 0
    num = 0
    for token in token_list:
        if 'x' in token:
            coef = token.replace("x", "")
            coef = int(coef) if coef else 1
            x += coef
        else:
            num += int(token)
    result = []
    if x > 0:
        result.append("x" if x == 1 else f"{x}x")
    if num > 0:
        result.append(str(num))
    return " + ".join(result)


###################################################