while True:
  print("Hello You!, ik ben Kilian")
  print("de datum en tijd is")
  import datetime
  x = datetime.datetime.now()
  print(x)
  name = input("Wie ben jij?: ")
  print("Hello " + name)
  print("Wil je dit programma nog een keer doen? Type y/n")
  answer = input()

  if answer == 'n':
    print("Dankjewel")
    break

  if answer == 'y':
    print("Restarting...")
  



  

 


  





