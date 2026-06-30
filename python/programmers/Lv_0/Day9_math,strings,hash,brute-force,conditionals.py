###################################################

# Day9. math, strings, hash, brute-force, conditionals

###################################################
'''
문제 설명
개미 군단이 사냥을 나가려고 합니다. 개미군단은 사냥감의 체력에 
딱 맞는 병력을 데리고 나가려고 합니다. 장군개미는 5의 공격력을, 
병정개미는 3의 공격력을 일개미는 1의 공격력을 가지고 있습니다. 
예를 들어 체력 23의 여치를 사냥하려고 할 때, 일개미 23마리를 
데리고 가도 되지만, 장군개미 네 마리와 병정개미 한 마리를 데리고 
간다면 더 적은 병력으로 사냥할 수 있습니다. 사냥감의 체력 hp가 
매개변수로 주어질 때, 사냥감의 체력에 딱 맞게 최소한의 병력을 
구성하려면 몇 마리의 개미가 필요한지를 return하도록 solution 
함수를 완성해주세요.

제한사항
hp는 자연수입니다.
0 ≤ hp ≤ 1000
'''
def solution(hp):
    total_ants = hp // 5
    rest = hp % 5
    total_ants += rest // 3
    total_ants += rest % 3
    
    return total_ants

# additional: using divmod()
def solution(hp):
    generals, rest = divmod(hp, 5)   # (장군 수, 남은 체력)
    soldiers, workers = divmod(rest, 3)  # (병정 수, 일개미 수)
    return generals + soldiers + workers

# 옵션이 더 늘어날 경우 or 수정 사항이 생길 경우
def solution(hp):
    powers = [5, 3, 1]   # 공격력 큰 순 (여기만 고치면 확장됨)
    count = 0
    for p in powers:
        cnt, hp = divmod(hp, p)
        count += cnt
    return count

###################################################
'''
머쓱이는 친구에게 모스부호를 이용한 편지를 받았습니다. 
그냥은 읽을 수 없어 이를 해독하는 프로그램을 만들려고 합니다. 
문자열 letter가 매개변수로 주어질 때, letter를 영어 소문자로 
바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
모스부호는 다음과 같습니다.

morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}

제한사항
1 ≤ letter의 길이 ≤ 1,000
return값은 소문자입니다.
letter의 모스부호는 공백으로 나누어져 있습니다.
letter에 공백은 연속으로 두 개 이상 존재하지 않습니다.
해독할 수 없는 편지는 주어지지 않습니다.
편지의 시작과 끝에는 공백이 없습니다.
'''
def solution(letter):
    morse = { 
        '.-':'a', 
        '-...':'b',
        '-.-.':'c',
        '-..':'d',
        '.':'e',
        '..-.':'f', 
        '--.':'g',
        '....':'h',
        '..':'i',
        '.---':'j',
        '-.-':'k',
        '.-..':'l',
        '--':'m',
        '-.':'n',
        '---':'o',
        '.--.':'p',
        '--.-':'q',
        '.-.':'r',
        '...':'s',
        '-':'t',
        '..-':'u',
        '...-':'v',
        '.--':'w',
        '-..-':'x',
        '-.--':'y',
        '--..':'z'
    }
    return "".join(morse[word] for word in letter.split(" "))

###################################################
'''
문제 설명
가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 
순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 
저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 
문자열을 return하도록 solution 함수를 완성해보세요.

제한사항
0 < rsp의 길이 ≤ 100
rsp와 길이가 같은 문자열을 return 합니다.
rsp는 숫자 0, 2, 5로 이루어져 있습니다.
'''
#sol1. using if-elif
def solution(rsp):
    result = []
    for i in rsp:
        if i == "0":
            result.append("5")
        elif i == "2":
            result.append("0")
        elif i == "5":
            result.append("2")
    return "".join(result)

# sol2. using dictionary
def solution(rsp):
    win = {"0": "5", "2": "0", "5": "2"}
    return "".join(win[i] for i in rsp)

###################################################
'''
문제 설명
머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 
구슬은 모두 다르게 생겼습니다. 
머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 
구슬 개수 share이 매개변수로 주어질 때, balls개의 구슬 중 
share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 
solution 함수를 완성해주세요.

제한사항
1 ≤ balls ≤ 30
1 ≤ share ≤ 30
구슬을 고르는 순서는 고려하지 않습니다.
share ≤ balls
'''

# sol1. using factorial
import math

def solution(balls, share):
    f = math.factorial
    return f(balls)//(f(balls-share)*f(share))

# sol2. using comb()
import math
def solution(balls, share):
    return math.comb(balls, share)   # 조합 C(n,r)을 바로!

###################################################
