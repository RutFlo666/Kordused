#1
while True:
    try:
        n=int(input("Mitu tk: "))
        if 0<n<10:
            break
    except ValueError:
        print("Viga. Sisesta arv 1-9!")
for i in range(n):
    print(" (\_/)\n (O O)\n / | \\,*")
  #2     
summ=0 
for i in range(15+1):
    summ+=i

print(summ)

#3
import random   #Добавляем модуль для  рандомного числа
x=0                                      
a=random.randint(1,100)    #Создаем это число в промежутке 1<=a<=100
while x<10:
   b=int(input('число: '))
   if b>a:
       print("Меньше!")
   elif b<a:
       print('Больше!')
   elif b==a:
       print('Вы угадали!')
       break    
   x+=1
print('Это число: ' + str(a))

  



#4
n1=int(input("введите целое число: "))
n2=0

while n1>0:
    digit=n1 % 10
    n1=n1//10

    n2=n2*10
    n2=n2+digit
print('"Обратно"ему число:',n2)


#5
inputNumber = input('Введите число: ')
numbers = []
i = 0
while i < len(inputNumber):
   number = inputNumber[i]
   if not number.isnumeric():
       continue
   numbers.append(int(number))
   i += 1
n = 0
m = 1
for number in numbers:
   n += number
   m *= number
print(n, m, sep='\n')
#oryna chehlatonieva
#tetiana nalyvai
