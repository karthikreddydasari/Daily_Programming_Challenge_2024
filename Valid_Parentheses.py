def valid_parantheses(str):
    stack=[]
    for i in str:
        if i=='[' or i=='{' or i=='(':
            stack.append(i)
        elif i==']' or i=='}' or i==')':
            stack.pop()
    if stack==[]:
        return True
    else:
        return False

str="{[(})]"
print(valid_parantheses(str))