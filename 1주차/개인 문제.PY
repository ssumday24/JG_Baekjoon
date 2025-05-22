#생각나는거

# 중앙값 => 크기 순서대로 정렬했을때 가장 중앙에 오는 값
# n의자리 일반화?
# 서로소
#사전순으로 정렬?


# words = ['apple', 'dog', 'banana', 'cat']
# words.sort(key= lambda x:(x,len(x)))  # 사전 → 길이순 
# print(words)


def expt(b,n):
    if n==0:
        return b
    else:
        return n * expt(b,n-1)

print(expt(10,4))

