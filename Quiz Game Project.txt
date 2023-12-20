i = 0                     # Simple Quiz Game by YOUSSEF ESSA
sum = 0                    

print("Welcome to quiz game !!\n")
answer = str (input("Do you want to play ?\n"))
print("Remember There is spaces between each word \n and all small letters CAPITAL only if question asks ")
print("IF you don't follow instruitions your answer will be Invalied !!")


if  answer == "yes" :                                  # Always assuming y1 y2 y3 =1 to get sum in final
                                                       # Assume (i+=1) in every rigth question to get total coorect Questions
                                                            
   x1 = str (input("what does CPU stande for ?"))                 # Question 1
   if x1 == "central processing unit":
      print("correct ! you got ",1,"point\n")
      y1 = 1 
      i += 1
      
   else :
       print("Incorrect")
       print("The correct answer is central processing unit\n") 
       
       
   x2 = str (input("What does Ram stand for ?"))              # Question 2
   if x2 == "random access memory":
    print("correct ! you got " , 1,"point\n")
    y2 = 1
    i += 1
     
   else :
       print("Incorrect")
       print("The correct answer is random access memory\n")       
       
       
   x3 = str (input("What does ROM stand for ?"))               # Question 3
   if x3 == "read only memory":
    print("correct ! you got " , 1,"point\n")
    y3 = 1 
    i += 1
    
   else :
      print("Incorrect")
      print("The correct answer is read only memory\n") 
       
       
   x4 = str (input("What does PSU stands for ?"))              #  Question 4
   if x4 == "power supply unit":
    print("correct ! you got " , 1,"point\n")
    y4 =1
    i += 1
    
   else:
      print("Incorrect")
      print("The correct answer is power supply unit\n") 
      
      
   x5 = int (input("What does One Byte equal to bit  (Remember only number enter) ?"))           # Question 5
   if x5 == 8: 
    print("correct ! you got " , 1,"point\n")
    y5 =1
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is 8 ")
    
    
   x6 = int (input("How many parts in Cpu? (Rember answer only a number)"))                # Question 6
   if x6 == 3: 
    print("correct ! you got " , 1,"point\n")
    y6 =1
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer 3")
    
    
   x7 = int(input("What 1 Kilo byte equal to ? (Remmber number only)"))                # Question 7
   if x7 == 1024: 
    print("correct ! you got " , 1,"point\n")
    y7 =1
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is 1024\n")
    
    
   x8 = int  (input("What is sum of 2 + 2 ?  "))                # Question 8
   if x8 == "4": 
    print("correct ! you got " , 1,"point\n")
    y8 =1
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is 4\n")
    
    
   x9 = str (input("What's the computer shudtown shortcut key ? (Remember this question may hava Capital letter)"))   # Question 9
   if x9 == "Alt + F4": 
    print("correct ! you got " , 1,"point")
    y9 =1
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is Alt + F4\n")
    
    
   x10 = str (input("What's is the Shortcut key of folder creation ? "))  # Question 10
   if x10 == "ctrl + Shift + n": 
    print("correct ! you got " , 1,"point\n")
    y10 =1
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is Ctrl + Shift + N\n")
    
    
   x11 = str (input("What is the shortcutkey for cut ? "))           # Question 11
   if x11 == "ctrl + x": 
    print("correct ! you got " , 1,"point\n")
    y11 =1
    i += 1
    
   else :
     print("Incorrect")
     print("The correct answer is ctrl + x\n")
    
       
   x12 = str (input("What i sthe shortcut key for selcet all?"))    # Question 12
   if x12 == "ctrl + a": 
    print("correct ! you got " , 1,"point\n")
    y12 =1
    i += 1
    
   else:
    print("Incorrect")
    print("The correct answer is ctrl + a\n")
    
    
   x13 = str (input("What is the shortcut key for Undo?"))           # Question 13
   if x13 == "crtl + z": 
    print("correct ! you got " , 1,"point\n")
    y13 =1
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is ctrl + z\n")
    
    
   x14 = int (input("How many keys are there on keyboard"))           # Question 14
   if x14 == "104": 
    print("correct ! you got " , 1,"point\n")
    y14 =1
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is 104\n")
    
   x15 = str (input("If we Have Logic gate , What is name of gate to get two input=1 and output =1"))           # Question 15
   if x15 == "and gate": 
    print("correct ! you got " , 1,"point\n")
    y15 =1
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is and gate\n")
    
    
    

print("number of questions is 15")
print("Your score is ",i)
print((i/15) * 100,"Questions are right")
     
   
