import random
a = random.randint(1,100)
print("I have chosen my number ,it is your time to guess")
while True:
      c=int(input())
      if c==a:
        print("great,you won!")
        break
      elif c>a:
        print("lower")
      elif c<a:
        print("above")
        
      
