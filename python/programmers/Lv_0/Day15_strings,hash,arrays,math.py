###################################################

# Day15. strings, hash, arrays math

###################################################
'''
문제 설명
영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 
합니다. 문자열 numbers가 매개변수로 주어질 때, numbers를 
정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.

제한사항
numbers는 소문자로만 구성되어 있습니다.
numbers는 "zero", "one", "two", "three", "four", 
"five", "six", "seven", "eight", "nine" 들이 
공백 없이 조합되어 있습니다.
1 ≤ numbers의 길이 ≤ 50
"zero"는 numbers의 맨 앞에 올 수 없습니다.
'''
def solution(numbers):
    nums = {"zero":"0", "one":"1", "two":"2", 
    "three":"3", "four":"4", "five":"5", "six":"6", 
    "seven":"7", "eight":"8", "nine":"9"}
    for eng, digit in nums.items():
        numbers = numbers.replace(eng, digit)
    return int(numbers)

###################################################
'''
문제 설명
문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, 
my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 
바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

제한사항
1 < my_string의 길이 < 100
0 ≤ num1, num2 < my_string의 길이
my_string은 소문자로 이루어져 있습니다.
num1 ≠ num2
'''
def solution(my_string, num1, num2):
    list_str = list(my_string)
    list_str[num1], list_str[num2] = list_str[num2], list_str[num1]
    return "".join(list_str)

###################################################
'''
문제 설명
문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를 
사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 
완성해보세요. 한 번만 등장하는 문자가 없을 경우 빈 문자열을 
return 합니다.

제한사항
0 < s의 길이 < 1,000
s는 소문자로만 이루어져 있습니다.

'''
def solution(s):
    count = {}
    strings = ""
    for i in s:
        count[i] = count.get(i, 0) + 1
    for k, v in count.items():
        if v == 1:
            strings += k
    return "".join(sorted(strings))

###################################################
'''
문제 설명
정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 
배열을 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ n ≤ 10,000
'''
def solution(n):
    answer = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            answer.append(i)
            if i != n // i:
                answer.append(n//i)
    return sorted(answer)

###################################################
