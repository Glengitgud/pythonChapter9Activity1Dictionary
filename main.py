fhand = open('mbox-short.txt')
fhand.read()
count = 0

input = input('Enter file name: ')

if input == 'mbox-short.txt':
    with open('mbox-short.txt') as fhand:
        for line in fhand:
            line = line.strip()
            if line.startswith('From: '):
                if '@' in line:
                    words = line.split()
                    print(words[1])
                    count += 1
print("There were ", count, " lines in the file")
fhand.close()
##