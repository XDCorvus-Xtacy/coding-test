###################################################

# Day24. math, simulation, strings, conditionals, loops

###################################################
'''
문제 설명
프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다. 
쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 
치킨에도 쿠폰이 발급됩니다. 시켜먹은 치킨의 수 chicken이 매개변수로 
주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 
함수를 완성해주세요.

제한사항
chicken은 정수입니다.
0 ≤ chicken ≤ 1,000,000
'''
def solution(chicken):
    service = 0
    coupon = chicken
    while coupon >= 10:
        new = coupon//10
        service += new
        coupon = coupon % 10 + new
    return service


###################################################
'''
문제 설명
이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 
두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

제한사항
return 값은 이진수를 의미하는 문자열입니다.
1 ≤ bin1, bin2의 길이 ≤ 10
bin1과 bin2는 0과 1로만 이루어져 있습니다.
bin1과 bin2는 "0"을 제외하고 0으로 시작하지 않습니다.
'''
def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2)).replace("0b", "")

###################################################
'''
문제 설명
문자열 before와 after가 매개변수로 주어질 때, before의 순서를 
바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 
하도록 solution 함수를 완성해보세요.

제한사항
0 < before의 길이 == after의 길이 < 1,000
before와 after는 모두 소문자로 이루어져 있습니다.
'''
def solution(before, after):
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0

###################################################
'''
문제 설명
1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 
등장합니다. 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 
몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ i < j ≤ 100,000
0 ≤ k ≤ 9
'''
def solution(i, j, k):
    total = 0
    for num in range(i, j+1):
        total += str(num).count(str(k))
    return total

###################################################
