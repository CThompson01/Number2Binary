binary = ['0','0','0','0','0']
binaryVal = [ 16, 8, 4, 2, 1]
def main():
    binary = ['0','0','0','0','0']
    number = int(raw_input('Please input a number: '))
    for i in xrange(4,-1,-1):
        if(binaryVal[i] == number):
            binary[i] = '1'
    print ''.join(binary)

main()