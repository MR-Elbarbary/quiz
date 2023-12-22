i = 0                     # Simple Quiz Game by NAME : YOUSSEF MOHAMED HASSAN  ID : 2305382                

print("Welcome to quiz game !!\n")
answer = str (input("Do you want to play ?\n"))
print("Remember There is spaces between each word \nAll small letters CAPITAL only if question asks \n")
print("IF you don't follow instruitions your answer will be Invalied !!\n")


if  answer == "yes" :                                  # Always assuming y1 y2 y3 =1 to get sum in final
                                                       # Assume (i+=1) in every rigth question to get total coorect Questions
                                                            
   x1 = str (input("What does CPU stande for ? "))             # Question 1
   if x1 == "central processing unit":
      print("correct ! you got ",1,"point\n")
      i += 1
      
   else :
       print("Incorrect")
       print("The correct answer is central processing unit\n") 
       
       
   x2 = str (input("What does Ram stand for ? "))              # Question 2
   if x2 == "random access memory":
    print("correct ! you got " , 1,"point\n")
    i += 1
     
   else :
       print("Incorrect")
       print("The correct answer is random access memory\n")       
       
       
   x3 = str (input("What does ROM stand for ? "))               # Question 3
   if x3 == "read only memory":
    print("correct ! you got " , 1,"point\n")
    i += 1
    
   else :
      print("Incorrect")
      print("The correct answer is read only memory\n") 
       
       
   x4 = str (input("What does PSU stands for ? "))              #  Question 4
   if x4 == "power supply unit":
    print("correct ! you got " , 1,"point\n")
    i += 1
    
   else:
      print("Incorrect")
      print("The correct answer is power supply unit\n") 
      
      
   x5 = int (input("What does One Byte equal to bit  (Remember only number enter) ? "))           # Question 5
   if x5 == 8: 
    print("correct ! you got " , 1,"point\n")
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is 8 ")
    
    
   x6 = int (input("How many parts in Cpu? (Remember answer only a number) "))                # Question 6
   if x6 == 3: 
    print("correct ! you got " , 1,"point\n")
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer 3")
    
    
   x7 = int(input("What 1 Kilo byte equal to ? (Remember number only) "))                # Question 7
   if x7 == 1024: 
    print("correct ! you got " , 1,"point\n")
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is 1024\n")
    
    
   x8 = int  (input("What is sum of 2 + 2 ?  "))                # Question 8
   if x8 == 4: 
    print("correct ! you got " , 1,"point\n")
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is 4\n")
    
    
   x9 = str (input("What's the computer shudtown shortcut key ? (Remember this question may hava Capital letter) "))   # Question 9
   if x9 == "Alt + F4": 
    print("correct ! you got " , 1,"point")
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is Alt + F4\n")
    
    
   x10 = str (input("What's is the Shortcut key of folder creation ? "))  # Question 10
   if x10 == "ctrl + Shift + n": 
    print("correct ! you got " , 1,"point\n")
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is Ctrl + Shift + N\n")
    
    
   x11 = str (input("What is the shortcutkey for cut ? "))           # Question 11
   if x11 == "ctrl + x": 
    print("correct ! you got " , 1,"point\n")
    i += 1
    
   else :
     print("Incorrect")
     print("The correct answer is ctrl + x\n")
    
       
   x12 = str (input("What is sthe shortcut key for selcet all ? "))    # Question 12
   if x12 == "ctrl + a": 
    print("correct ! you got " , 1,"point\n")
    i += 1
    
   else:
    print("Incorrect")
    print("The correct answer is ctrl + a\n")
    
    
   x13 = str (input("What is the shortcut key for Undo ? "))           # Question 13
   if x13 == "ctrl + z": 
    print("correct ! you got " , 1,"point\n")
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is ctrl + z\n")
    
    
   x14 = int (input("How many keys are there on keyboard ? "))           # Question 14
   if x14 == 104: 
    print("correct ! you got " , 1,"point\n")
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is 104\n")
    
   x15 = str (input("If we Have Logic gate , What is name of gate to get two input = 1 and output = 1 ? "))           # Question 15
   if x15 == "and gate": 
    print("correct ! you got " , 1,"point\n")
    i += 1
    
   else :
    print("Incorrect")
    print("The correct answer is and gate\n")

     
    # ----------------------------------------------------------------------------------------------
      #  Mscqs Questions :  
    
    
   z = [1,2,3,4]    # Assuming that another Mscqs quetions and this list has the answer of all quetions 
                     # If User Put the wrong answer 
    
   print("Answer the following Mscqs questions:\n")
    
   print("Which protocol is used for browsing data ?\n")             # Question 16
   print("1. TCP \n2. FTP \n3. TFTP \n4. HTTP ")
   x16 = int (input())
    
   if x16 == z[3]:
        print("correct ! you got ",1,"point\n")
        i +=1
        
   else:
     print("Incorrect")
     print("The correct choice is 4 =>HTTP \n")
     
   print("Which of the following is necessary to work on a computer ? ")              # Question 17
   print("1. Compiler\n2. Assembly\n3. Operating System\n4. None of these")
   x17 = int (input())
    
   if x17 == z[2]:
        print("correct ! you got ",1,"point\n")
        i +=1
        
   else :
     print("Incorrect")
     print("The correct choice is 3 => Operating System \n")   

   print("Which of the following is for Entering data to user ? ")                  # Question 18
   print("1. Input\n2. Output\n3. Processing\n4. Storage")
   x18 = int (input())
    
   if x18 == z[0] :
        print("correct ! you got ",1,"point\n")
        i +=1
     
   else :
     print("Incorrect")
     print("The correct choice is 1 => Input\n")
     
     
   print("Which of the following is for saving data , programs or output for future use ? ")          # Question 19
   print("1. Input\n2. Storage\n3. Output\n4. Communications")
   x19 = int (input())
    
   if x19 == z[1] :
        print("correct ! you got ",1,"point\n")
        i +=1
        
   else :
     print("Incorrect")
     print("The correct choice is 2 => Storage\n")  
     
     
   print("Which of the following is one of the input devices ? ")                          # Question 20
   print("1. Keyboards\n2. Monitors\n3. Printers\n4. Speakers")
   x20 = int (input())
    
   if x20 == z[0]:
        print("correct ! you got ",1,"point\n")
        i +=1
        
   else :
     print("Incorrect")
     print("The correct choice is 1 => Keyboards\n")  
     
    
   print("Which of the following is one of the output devices ?")                       # Question 21
   print("1. Keyboars\n2. Monitors\n3. Cameras\n4. Scanners")
   x21 =int (input())     
    
   if x20 == z[1] :
        print("correct ! you got ",1,"point\n")
        i +=1
        
   else :
     print("Incorrect")
     print("The correct choice is 2 => Monitors\n")
     
     print("What does Cpu controls ? ")                                                   # Question 22
     print("1. All input,Output and processing\n2. Controlled by the input data\n3. Controls Memory\n4 .Output")
     x22 = int (input())
     
   if x22 == z[0] :
        print("correct ! you got ",1,"point\n")
        i +=1
        
   else :
      print("Incorrect")
      print("The correct choice is 1 => All input,Output and processing\n")
    
     
   print("Waht is another name of ROM ?")                                         # Question 23
   print("1. Virtual memory\n2. Volatile memory\n3. Non volatile memory\n4. Cache memory")
   x23 = int (input())
   
   if  x23 == z[2]:
       print("correct ! you got ",1,"point\n")
       i +=1
       
   else:
       print("Incorrect")  
       print("The correct choice is 3 => Non volatile memeory\n") 
   
   
   print("How much data can be stored in CD ?")                                   # Question 24
   print("1. 300 Mb\n2. 400 MB\n3. 600 Mb\n4. 700 Mb")
   x24 = int (input())  
   
   if x24 ==z[3]:
       print("correct ! you got ",1,"point\n")
       i +=1
    
   else :
       print("Incorrect")
       print("The correct choice is 3 => 700\n")
       
   print("What is the another name of CD-ROM ?")                                  # Question 25
   print("1. Memory register\n2. Secondary Memory\n3. Semiconductor memory\n4. None of these")
   x25 = int (input())  
   
   if x25 == z[1]:
        print("correct ! you got ",1,"point\n")
        i +=1
    
   else:
      print("Incorrect")
      print("The correct choice is 2 => Secondary Memory\n")   
        
            
 
print("Number of the questions is 25")
print("Your score is " , i)     
print(((i / 25) * 100),"% Questions are correct\nBe Ready for Round 2 !!")

#--------------------------------------------------------------------------------------------------------------
#------------ End Statment for another Team's Member-----------------------------------------------------------