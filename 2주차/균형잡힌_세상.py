# 4949 
# 괄호들의 균형이 잘 맞춰져 있는지
while (True):
    sentence = input()
    
    if sentence == '.':
        break    
    
    stack=[]
    result = 'yes'
    
    for ch in sentence:
        if ch=='(' or ch=='[':
            stack.append(ch)
            
        elif ch==')':
            if stack and stack[-1]=='(':
                stack.pop() # 탑의() 쌍을 제거
            
            else:  # top이 ( 가 아니었을때
                result='no'
                break
                
        elif ch==']':
            if stack and stack[-1] == '[':
                stack.pop() # 탑의[] 쌍을 제거

            else:
                result='no'
                break
    if stack: #예시: ([hello world]
        result = 'no'
    #yes / no 출력
    print(result)