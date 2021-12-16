# Number 1
def sum_to(n):
  sum = 0
  p = 0
  while p <= n:
    sum = sum + p
    # print(sum)
    p += 1
  print(sum, 'solution 1')


sum_to(6)

# Number 2
def largest(list):
  list.sort()
  number = list[-1]
  print(number, 'solution 2')


largest([1, 2, 3, 4, 0])  
largest([10, 4, 2, 231, 91, 54])  

# Number 3
def occurances(str1, str2):
  count = str1.count(str2)
  print(count, 'number 3')
    
occurances('fleep floop', 'e')   
occurances('fleep floop', 'p')   
occurances('fleep floop', 'ee')  
occurances('fleep floop', 'fe')

# Number 4
def product(*args):
  result = 1
  for number in args:
    result *= number
  print(result, 'number 4')
  
product(-1, 4) 
product(2, 5, 5)