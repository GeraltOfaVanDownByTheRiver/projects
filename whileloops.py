count = 0
while (count < 10):
    count+=1
    print(count)

answer = ''
while (answer != 'when'):
    answer = input('Say when: ')
    answer = answer.lower()
    if answer == 'when':
        break
