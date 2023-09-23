import time, os

main_list = []

head = ['Name', 'Description', 'Size', 'Quantity', 'Total($)']

def menu():
  a = '\033[4mPIZZA SHOPING LIST\033[0m'
  print(f'\033[1;33m{a:^40}\033[0m')
  time.sleep(1.5)
  print()
  ask = input('''
  1: Add pizzas
  2: View pizzas
  3: Quit
  >> ''')
  return ask

def add():
  auto_load()
  time.sleep(1.5)
  name = input ('What is your name: ')
  time.sleep(1.5)
  desc = input('What type of pizza do you want?: ')
  time.sleep(1.5)

  while True:
    print()
    try:
      quantity = int(input('Enter the quantity of pizza that you want to add: ').strip())
      break
    except ValueError:
      print()
      time.sleep(1)
      print('\033[31mPlease input figures not words!\033[0m')
      continue 
      
  time.sleep(1.5)
  while True:
    print ()
    size1 = input('''Enter the size:
           L for Large
           M for Medium
           S for Small
           >> ''').strip().upper()
    
    if size1 == 'L':
      size = 1.4
      break
    elif size1 == 'M':
      size = 1.6
      break
    elif size1 == 'S':
      size = 1.8
      break
    else:
      print('\033[31mPlease, input L, M or S to proceed!\033[0m]')
      time.sleep(4)
      continue 
    
  total = round((quantity * size), 2)

  list1 = [name, desc,  size1, quantity, total]
  main_list.append(list1)
  auto_save(main_list)
  time.sleep(1.5)
  print()
  print ('\033[32mItem added Successfully!😉😎\033[Om')
  time.sleep(2)
  os.system ('clear')

def view():
  auto_load()
  printer (main_list)
  print()

def printer(w):
  os.system('clear')
  m = 0
  for i in w:
    if m == 0:
      for j in i:
        print(f'\033[1;33m{j:^15}', end='|')
        m += 1
      print()
      print('    _____________________________________________________________________________')
    else:
      for j in i:
        print(f'\033[34m{j:^15}', end='|')
    print()
  print()
  ask4 = input('''\033[0mWhen you are done viewing, press 'Enter' to go back to main menu: 
''')
  if len(ask4) == 0:
    time.sleep(1) 
    os.system('clear')
  
  
p = 0
def auto_load():
  global main_list, p
  try:
    m = open('pizza.txt', 'r')
    main_list = eval(m.read())
    if head in main_list:
      p += 1
    m.close()
  except FileNotFoundError:
    print ()
    #print('\033[31mThere is nothing in your Pizza Shop. Add items first!')
    time.sleep(3)
    pass

def auto_save(anylist):
  global p
  if p == 0:
    anylist.insert(0, head)
  else:
    pass
  n = open('pizza.txt', 'w')
  n.write(str(anylist))
  n.close()
  p += 1

while True:
  b = menu()
  if b == '1':
    add()
  elif b == '2':
    view()
  elif b == '3':
    break
  else:
    print ()
    print ('\033[31mInvalid Selection!😥 Please, select 1 or 2 !!\033[31m')
    time.sleep(2)
    os.system('clear')
    continue 
print ()
print('\033[32mByeee🙋‍♂️😎. Hoping to get more pizza orders from you 😉. Take Care!')