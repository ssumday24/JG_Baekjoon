#이진 탐색에서 MID 는 예상 후보군들중 하나 

import sys

N = int(sys.stdin.readline()) # 지방의 수
arr = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline()) # 총 예산

total=0

if sum(arr) < M : #정상 요청인 경우
    print(max(arr))
    
else:
    #여기서 arr sort 필요없음
    left = 0
    right = max(arr)
    
    while(True):
        total=0  #예산이 바뀔때마다 새로 계산
        mid = (left+right) //2 # 평균값으로 후보.
        
        for i in arr: #i는 값.
            if i > mid: #예산이 상한액보다 크다면 상한액으로 +
                total += mid
            else: #작으면 그대로 +
                total += i
                
        if total > M : #예산이 총 상한액보다 크다면 mid 줄이기
            right= mid -1
            
      
        elif total <=M: #예산이 아직 남았다면 mid 늘려보기
            left = mid+1
            
        if left>right:
            print(right) 
            break # 이진탐색 일반적 종료조건 
        
        # MID= 127을 성공하고, MID =128을 시도했는데 실패하면
        # 당연히 MID = 127이 최대값  = > right=127