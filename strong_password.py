alphabet=input("enter the alphabet")
number=input("enter the number")
special_charecter=input("enter the special charecter")
if alphabet=="A-Z":
    print("alphabet")
    if number==0-9:
        print(number)
    elif special_charecter=="@":
      print(special_charecter)
    else:
        print("print invalid")
else:
    print(alphabet+number+special_charector)
    print("strong password")