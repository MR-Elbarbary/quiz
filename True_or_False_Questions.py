
j=0
print("put True or False :")
print("------------------")
A1=str(input ("1)  Just as you can learn to drive a car without knowing much about car engines, you can learn to use a computer without understanding the technical details of how a computer works  : "))
if A1=="True" or "true"  :
    print("1 mark")
    print("Your Answer is corret")
    j=j+1
   
else :
   print("0 mark ")
   print("the correct Answer is True")
A2=str(input("2) computer does not always do whatever the instructions, or program, tell it to do :"))
if A2 =="False" or "false":
    print("1 marks")
    print("Your Answer is corret")
    j=j+1

else:
    print("0 mark ")
    print("the correct Answer is False")
A3=str(input("3) The external hardware components are located inside the main box or system unit of the computer : "))
if A3 =="False" or "false":
    print("1 marks")
    print("Your Answer is corret")
    j=j+1
  
else:
    print("0 mark ")
    print("the correct Answer is False")
A4=str(input("4) Storage devices are hardware used to store data on or access data from storage media, such as CD discs, DVD discs, or flash memory cards  : "))
if A4=="True" or "true"  :
    print("1 mark")
    print("Your Answer is corret")
    j=j+1
  
else :
   print("0 mark ")
   print("the correct Answer is True")
A5=str(input("5) There are application programs that help users write their own programs using a programming language  : "))
if A5=="True" or "true"  :
    print("1 mark")
    print("Your Answer is corret")
    j=j+1
   
else :
   print("0 mark ")
   print("the correct Answer is True")

print("The Number of questions is 5")
print("Your Score is",j)
print(((j/5)*100),"% Questions are correct")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

 
