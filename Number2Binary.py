binary = ['0','0','0','0','0']
def getNumber():
    binary = ['0','0','0','0','0']
    number = int(raw_input('Please enter a number: '))
    #print ''.join(binary)
    if(number > 1):
        if(number < 3):
            binary[3] = '1'
        elif(number > 3):
            # have another nested if statement
            print number
        else:
            binary[3] = '1'
            binary[4] = '1'
    elif(number == 1):
        binary[4] = '1'
    else:
        for i in range(len(binary)):
            binary[i] = '0'
    print ''.join(binary)
    
getNumber()