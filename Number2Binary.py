binary = ['0','0','0','0','0']
binaryVal = [ 16, 8, 4, 2, 1]
def main():
    binary = ['0','0','0','0','0']
    number = int(raw_input('Please input a number: '))
    for i in xrange(0,5,1):
        if(number - binaryVal[i] >= 0):
            binary[i] = '1'
            number = number - binaryVal[i]
        else:
            binary[i] = '0'
    print ''.join(binary)

main()