binary = ['0','0','0','0','1']
def getNumber():
    number = int(raw_input('Please enter a number: '))
    #print ''.join(binary)
    if(number > 1):
        binary[4] = '0'
    elif(number == 1):
        binary[4] = '1'
    else:
        for i in range(len(binary)):
            binary[i] = '0'
    print ''.join(binary)
    