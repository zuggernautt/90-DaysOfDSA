tokens = ["2","1","+","3","*"]


def evalRPN(tokens):
    res = []

    for i in tokens:
        if i == "-" or i == "/" :
            a,b = res.pop(), res.pop()
            if i == "-":
                res.append(b-a)
            else:
                res.append(int(b/a))
        elif i == "+" or i=="*":
            a,b = res.pop(), res.pop()

            if i == "+":
                res.append(a + b)
            else:
                res.append(a*b)

      
        else:
            res.append(int(i))

    return res[0]


print(evalRPN(tokens))

def evalRPN(tokens):
    res = []

    for i in tokens:
        if i == "+" :
            res.append(res.pop() + res.pop())
        elif i == "-":
            a,b = res.pop(), res.pop()
            res.append(b-a)
        elif i == "*":
            res.append(res.pop()+ res.pop())
        elif i == "/":
            a,b = res.pop(), res.pop()
        

            res.append(int(b/a))
        else:
            res.append(int(i))
    
            

    return res[0]

print(evalRPN(tokens))