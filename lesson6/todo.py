todos = open('todos.txt', 'a')

print('Put out the trash.', file=todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.', file=todos)

todos.close()

print('-------------------------------------')

tasks = open('todos.txt')

for chore in tasks:
    print(chore, end='')

tasks.close()

print('-------------------------------------')

with open('todos.txt') as task:
    for row in task:
        print(row, end='')
