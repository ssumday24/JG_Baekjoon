# 11053 : 가장 긴 증가하는 부분 수열
import sys 
input=  sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
dp=[1]*(N) # 1~N번 인덱스 사용

for i in range(N): # i 번 인덱스를볼때
   for j in range(0,i): # 0 ~ i-1 인덱스 검사
       
       #if A[j]<A[i] and dp[j]==max(dp):
       if A[j]<A[i] :
            dp[i]=max(dp[i],dp[j]+1)



print(dp) #테이블 확인용
print(max(dp))
