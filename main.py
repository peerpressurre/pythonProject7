try:
    num1 = int(input('enter first number->'))
    num2 = int(input('enter second number->'))
    count = num2 - num1+1
    sum = num1
    for x in range(num1, num2):
        num1 += 1
        sum += num1

    else:
        sa = sum / count

    print(f'Сумма:{sum}\nСереднє арифметичне: {sa}')

except Exception as ex:
    print('Error:',ex)