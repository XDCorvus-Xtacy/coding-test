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



# ============================================================
# 계단 2: bisect 모듈
# ============================================================
'''
[bisect는 "찾기"가 아니라 "경계 찾기"]
어제 만든 binary_search : 있으면 인덱스, 없으면 -1
bisect                  : "어디에 넣어야 정렬이 유지되나" = 삽입 위치
                          없는 값도 위치를 알려줌

[두 함수의 차이 — 같은 값들의 "덩어리" 기준]
  arr = [1, 3, 3, 3, 5, 7]
  인덱스  0   1  2  3  4  5
           └3 덩어리┘
              ↑           ↑
  bisect_left(arr, 3)  = 1   ← 덩어리가 시작되는 자리
  bisect_right(arr, 3) = 4   ← 덩어리가 끝난 다음 자리

  · 중복이 없으면 둘의 결과가 같음 (중복이 있을 때만 차이가 드러남)
  · 중복 여부와 무관하게 항상 쓸 수 있음

[개수 세기에 활용]
  bisect_left(arr, x)                      = x 미만인 원소의 개수
  bisect_right(arr, x)                     = x 이하인 원소의 개수
  bisect_right(arr, x) - bisect_left(arr, x) = x의 개수  (O(log n))
    → list.count()는 O(n)

[모듈 전체 — 함수 6개, 실질 4종류]
  위치만 반환 (리스트 안 바꿈)
    bisect_left(a, x)
    bisect_right(a, x)
    bisect(a, x)          ← bisect_right의 별칭
  실제로 삽입 (리스트 수정)
    insort_left(a, x)
    insort_right(a, x)
    insort(a, x)          ← insort_right의 별칭

  ⚠️ insort는 None을 반환 (sort, heapify와 같은 제자리 수정 계열)
     a = insort(a, x) 로 쓰면 a가 None이 됨 → 자가 점검 4번
  ⚠️ insort의 삽입 자체는 O(n)
     위치는 O(log n)에 찾지만 중간에 끼워넣으려면 뒤를 전부 밀어야 함
     루프에서 반복하면 O(n^2) → 대량이면 힙을 고려

[내부 구현 — 어제 코드와 무엇이 다른가]
  def bisect_left(a, x):
      lo, hi = 0, len(a)
      while lo < hi:
          mid = (lo + hi) // 2
          if a[mid] < x: lo = mid + 1
          else:          hi = mid        # 같아도 멈추지 않고 계속 왼쪽으로
      return lo

  def bisect_right(a, x):
      lo, hi = 0, len(a)
      while lo < hi:
          mid = (lo + hi) // 2
          if x < a[mid]: hi = mid
          else:          lo = mid + 1    # 같으면 계속 오른쪽으로
      return lo

  차이 3가지
   1. == 가지가 없음
      어제는 찾으면 즉시 return / bisect는 같은 값을 만나도 멈추지 않고
      덩어리의 끝까지 밀어붙임
   2. hi = mid  (마이너스 1 없음)
      mid 자리가 답일 수 있으므로 후보에서 제외하면 안 됨
   3. 범위 표현이 다름
      어제  : [left, right]  양끝 포함  → while left <= right, right = len-1
      bisect: [lo, hi)       오른쪽 미포함 → while lo < hi, hi = len
      → 어제 <= 가 필요했고 오늘 < 가 맞는 이유는 "범위를 어떻게 표현했느냐"의 차이

[탐색 횟수]
  bisect_left([1,3,3,3,5,7], 3) → 3번 만에 종료 (일일이 세지 않음)
'''

from bisect import bisect_left, bisect_right

arr = [1, 3, 5, 7, 9, 11, 13]
print(bisect_left(arr, 7))   # 3  = 7 미만의 개수
print(bisect_right(arr, 7))  # 4  = 7 이하의 개수