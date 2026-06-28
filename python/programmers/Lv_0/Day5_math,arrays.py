###################################################

# Day5. math, arrays

###################################################
'''
문제 설명
머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 
50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 
하도록 solution 함수를 완성해보세요.

제한사항
10 ≤ price ≤ 1,000,000
price는 10원 단위로(1의 자리가 0) 주어집니다.
소수점 이하를 버린 정수를 return합니다.
'''

# sol1. using if-elif
def solution(price):
    if price >= 500000:
        return int(price*0.8)
    elif price >= 300000:
        return int(price*0.9)
    elif price >= 100000:
        return int(price*0.95)
    return int(price)


# sol2. using list, tuple
'''
왜 딕셔너리는 안 될까?
- 딕셔너리는 키로 빠르게 찾는 자료구조임. 즉, 순서가 목적인 자료형이 아님(물론 동작은 함)
- 따라서 순서가 중요하다는 목적이 드러나는 리스트형이 목적에 부합함.
'''
def solution(price):
    discounts = [(500000, 0.8), (300000, 0.9), (100000, 0.95)]
    for limit, rate in discounts:
        if price >= limit:
            return int(price * rate)
    return price

# 만약 할인율을 유지보수 해야한다면?
def solution(price):
    discounts = [
        (100000, 0.95),
        (500000, 0.8),
        (700000, 0.75),   # 아무 순서로나 추가해도 됨
        (300000, 0.9),
    ]
    # 검사 직전에 금액 큰 순으로 정렬
    for limit, rate in sorted(discounts, reverse=True):
        if price >= limit:
            return int(price * rate)
    return price

###################################################
'''
문제 설명
머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 
아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 가지고 있는 
돈 money가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 
아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 
하도록 solution 함수를 완성해보세요.

제한사항
0 < money ≤ 1,000,000
'''
# sol1. using loop
def solution(money):
    cnt = 0
    while money >= 5500:
        money = money - 5500
        cnt += 1
    answer = [cnt, money]
    return answer

# sol2. using math
def solution(money):
    return list(divmod(money, 5500))

###################################################
'''
문제 설명
머쓱이는 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 
2022년 기준 선생님의 나이 age가 주어질 때, 선생님의 출생 연도를 
return 하는 solution 함수를 완성해주세요

제한사항
0 < age ≤ 120
나이는 태어난 연도에 1살이며 매년 1월 1일마다 1살씩 증가합니다.
'''
def solution(age):
    return 2023-age

###################################################
'''
문제 설명
정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. 
num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 
solution 함수를 완성해주세요.

제한사항
1 ≤ num_list의 길이 ≤ 1,000
0 ≤ num_list의 원소 ≤ 1,000
'''
# sol1. using slicing
def solution(num_list):
    return num_list[::-1]

# sol2. using reversed()
def solution(num_list):
    return list(reversed(num_list))

# sol3. using .reverse()
def solution(num_list):
    num_list.reverse()
    return num_list