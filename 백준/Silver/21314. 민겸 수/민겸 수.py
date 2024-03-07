minkyeom = input()

digit = 0
max_result = ''
min_result = ''
for i in minkyeom:
    if i == 'M':
        digit += 1
    else:
        max_result += '5' + '0' * digit
        if digit > 0:
            min_result += '1' + '0' * (digit-1) + '5'
        else:
            min_result += '5'
        digit = 0

if digit != 0:
    max_result += '1' * digit
    min_result += '1' + '0' * (digit-1)

print(max_result)
print(min_result)