template = ''

bin = input('request bin url: ')
comfort = input('comfort url: ')
code = template % (bin, comfort)
origin = input('origin: ')

print(f'upload the following code to {origin}\n')
print(f'{code}\n')
