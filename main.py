try:
    sign = input('Enter sigh->')
    length = int(input('Enter length->'))
    print('h = horizontal/n v = vertical')
    choice = input('->')
    for x in range(0,length):
        if choice == 'h':
            print(sign, end='')
        elif choice == 'v':
            print(sign)
        else:
            raise Exception ('Error: incorrect choice symble')
except Exception as ex:
    print(f'Error',{ex})