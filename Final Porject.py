k = 0
 # Question 1
print("Which of the following storage devices provides the fastest access to data in a computer system?\n") 
print("1. Solid State Drive (SSD)\n2. Optical Disc Drive (ODD)\n3. USB Flash Drive\n4. External Hard Disk Drive (HDD) ")
Q1 = int (input())

if Q1 == 1:
 print("correct ! you got 1 point\n")
 k +=1

else:
 print("Incorrect")
 print("The correct choice is 1.Solid State Drive (SSD) \n")
 # Question 2
print("Which of the following is responsible for managing and controlling the flow of data between the computer's hardware components?\n")
print("1. Operating System\n2. Application Software\n3. BIOS (Basic Input/Output System)\n4. Motherboard")
Q2 = int (input())

if Q2 == 1:
 print("correct ! you got 1 point\n")
 k +=1

else:
 print("Incorrect")
 print("The correct choice is 1. Operating System \n")
# Question 3
print(" Which of the following is an example of a secondary storage device in a computer system?\n")
print("1. Random Access Memory (RAM)\n2. Central Processing Unit (CPU)\n3. Hard Disk Drive (HDD)\n4. Graphics Processing Unit (GPU)")
Q3 = int (input())

if Q3 == 3:
 print("correct ! you got 1 point\n")
 k +=1

else:
 print("Incorrect")
 print("The correct choice is 3. Hard Disk Drive (HDD)\n")

 
print("Number of the questions is 5")
print("Your score is " , 3)     
print(((k / 3) * 100)," % Questions are correct\nBe Ready for Round 2 !!")
# -------------------------  Seconed Round ---------------------------


j=0
print("put True or False :")
print("------------------")
A1=str(input ("1)  Just as you can learn to drive a car without knowing much about car engines, you can learn to use a computer without understanding the technical details of how a computer works  : "))
if (A1=="True") or (A1=="true")  :
    print("1 mark")
    print("Your Answer is corret")
    j=j+1
   
else:
   print("0 mark ")
   print("the correct Answer is True")
   j=j-1
A2=str(input("2) computer does not always do whatever the instructions, or program, tell it to do :"))
if (A2 =="False") or (A2=="false"):
    print("1 marks")
    print("Your Answer is corret")
    j=j+1

else:
    print("0 mark ")
    print("the correct Answer is False")
    j=j-1
A3=str(input("3) The external hardware components are located inside the main box or system unit of the computer : "))
if (A3 =="False") or  (A3=="false"):
    print("1 marks")
    print("Your Answer is corret")
    j=j+1
  
else:
    print("0 mark ")
    print("the correct Answer is False")
    j=j-1
A4=str(input("4) Storage devices are hardware used to store data on or access data from storage media, such as CD discs, DVD discs, or flash memory cards  : "))
if (A4=="True") or (A4=="true")  :
    print("1 mark")
    print("Your Answer is corret")
    j=j+1
  
else :
   print("0 mark ")
   print("the correct Answer is True")
   j=j-1
print("The Number of questions is 5")
print("Your Score is",j)
print(((j/4)*100)," % Questions are correct\nBe Ready for Round 3 !!")

# -------------------------  Third  Round ---------------------------

i = 0                        

print("Remember There is spaces between each word \nAll small letters CAPITAL only if question asks \n")
print("IF you don't follow instruitions your answer will be Invalied !!\n")
                                 
                                                            
x1 = str (input("What does CPU stande for ? "))             # Question 1
if x1 == "central processing unit":
      print("correct ! you got ",1,"point\n")
      i += 1
      
else :
       print("Incorrect")
       print("The correct answer is => central processing unit\n") 
       
       
x2 = str (input("What does Ram stand for ? "))              # Question 2
if x2 == "random access memory":
    print("correct ! you got " , 1,"point\n")
    i += 1
     
else :
       print("Incorrect")
       print("The correct answer is => random access memory\n")       
       
       
x4 = str (input("What does PSU stands for ? "))              #  Question 3
if x4 == "power supply unit":
    print("correct ! you got " , 1,"point\n")
    i += 1
    
else:
      print("Incorrect")
      print("The correct answer is => power supply unit\n") 
      
x4 = str (input("What is the shortcutkey for cut ? "))           # Question 4
if x4 == "ctrl + x": 
    print("correct ! you got " , 1,"point\n")
    i += 1
    
else:
     print("Incorrect")
     print("The correct answer is => ctrl + x\n")
     
     
 
print("Number of the questions is 4")
print("Your score is " , i)     
print(((i / 4) * 100),"% Questions are correct\nBe Ready for Round 4 !!") 

# -------------------------  Fourth  Round --------------------------- 

# -----------------------   Fifth Round ------------------------------
m=0
print("          Trace This Code           ")
print("1)        --------------")
print("N=4 \nK=5 \nR=N \nif K>N : \n    R=K")
ans=5
ans1=int(input("Enter R = "))
if ans==ans1:
    print("True")
    m=m+1
else :
    print("False")
print("---------------------------------------------------------")
print(  "2)")
print("N=5 \nP=0 \nO=1 \nif P>0 : \n     N+=1 \nelse O>0 :  \n     N-=1")
print(  "--------------")
ans1=4
ans=int(input("N= "))
if ans==ans1 :
    m=m+1
    print("TRUE")
else:
    print("FALSE")

print("---------------------------------------------------------")
print(  "3)")
print("N=0.0\nY=1.0\nif abs(N-Y)<1 :\n     print(N)   \nelse :  \n     print(Y)  ")
print(  "--------------")
ans1=1.0
ans=float(input("Output is"))
if ans==ans1:
    m=m+1
    print("True")
else :
    print("False")
    print("---------------------------------------------------------")
print(  "4)")
print("N=5 \nP=2\nO=1\nif P>0 :\n     N+=1\nif O>0 :  \n     N-=1")
print(  "--------------")
ans1=5
ans=int(input("N= "))
if ans==ans1:
    m=m+1
    print("True")
else :
    print("False")
print("your grade is ",m ,"of 4")