try:
    num = int(input('Enter number->'))
    start = 1
    factorial = 1

    for item in range(1, num+1):
        factorial *= item
    print(f'{factorial}')
except Exception as ex:
    print(f'Error information: {ex}')