import random

for x in range(0,6):
  #print(x)

  number = int(input("Enter the number: "))
  print(number)
  for i in range(random.randint(0,100)):
    num = i
  print(num)
  if (number == num):
    print("Both numbers are same,Congratulation you won!")
    break

  elif(number > num):
    print("Number is too high")
   
  elif(number < num):
    print("Number is too small")
  
  if(x < 5):
   print("Try again")
  
  else:
   print("Game Over")