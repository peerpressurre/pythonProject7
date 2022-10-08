try:
    sighn = int(input('Enter sigh->'))
    length = int(input('Enter length->'))
    print('h = horizontal/n v = vertical')
    choice = input('->')
    for x in range(0,length):
        if choice == 'h':
            print(sighn)
        elif choice == 'v':
            print(sighn\n)
        else:
            raise Exception:
        print('Error: incorrect choice symble')
except Exception:
    print