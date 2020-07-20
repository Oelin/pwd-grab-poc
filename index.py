with open('./template.js') as file:
  tempalate = file.read()

try:
  log = input('logger url: ')
  final = input('final url: ')
  origin = input('origin: ')
  
except:
  print('whoops')
  exit(1)

code = template % (log, final)
print(f'upload the following code to {origin}\n')
print(f'{code}\n')
