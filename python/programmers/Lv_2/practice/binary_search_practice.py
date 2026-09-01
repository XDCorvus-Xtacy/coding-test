'''
정렬된 리스트 arr과 찾을 값 target이 주어집니다.
target이 arr에 있으면 그 인덱스를, 없으면 -1을 반환하세요.

예) arr = [1, 3, 5, 7, 9, 11], target = 7  → 3
    arr = [1, 3, 5, 7, 9, 11], target = 4  → -1

Q1. 탐색 범위를 어떻게 표현할까? (변수 두 개)
Q2. 가운데는 어떻게 구할까?
Q3. 가운데 값과 target을 비교했을 때, 어느 쪽을 버릴까?
'''
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target: 
            return mid
        elif arr[mid] < target: 
            left = mid + 1
        else: 
            right = mid - 1
    return -1   

arr = [1, 3, 5, 7, 9, 11]
target = 4

print(binary_search(arr, target))