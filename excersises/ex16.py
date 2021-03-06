from sys import argv

script, filename = argv

print(f'We\'re going to erase {filename}.')
print('If you don\'t want that, hit CTRL-C (ˆC).')
print('If you do want that, hit RETURN.')

input('?')

print('Opening the file...')
target = open(filename, 'w')

print('Truncating the file. Goodbye!')
target.truncate()

print('Now I\'m going to ask you for three lines.')

line1 = input('Line 1: ')
line2 = input('Line 2: ')
line3 = input('Line 3: ')

print('I\'m going to write these to the file.')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('And finally we close the file.')
target.close()

print('And we will read the file that we just created')
target_read = open(filename)
print('The content of the file in question: \n', target_read.read())
target_read.close()
