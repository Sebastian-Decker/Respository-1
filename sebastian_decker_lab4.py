#Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p' 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_shift():
    try:
        shift = int(input('Enter a number between 1 and 26 to shift by: '))
        if shift in range(1,27):
            return shift
        else:
            print('Number must be between 1 and 26')
            return get_shift()
    except:
        print('Invalid number')
        return get_shift()

get_shift()


#print(Letters)
