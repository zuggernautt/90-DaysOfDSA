
def binaryToDecimal(bin):
    decimal = 0
    power = 0
    for i in reversed(bin):
        if i == '1':
            decimal += 2**power
        power+=1
    return decimal



if __name__=="__main__":
    binary_input = input("enter binary number: ")
    decimal_op= binaryToDecimal(binary_input)
    print(decimal_op)
