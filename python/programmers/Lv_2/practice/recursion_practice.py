'''
원소 n개짜리 리스트의 부분집합은 몇 개인가를 재귀를 통해 구해보시오.
'''
def solution(lst):
    index = 0
    length = len(lst)
    def combinations(index):
        if index == length:
            return 1
        return combinations(index+1) + combinations(index+1)
    answer = combinations(index)
    return answer