import random        # This module help to take random objects
import time           # This module is used for keeping the track of time
import matplotlib.pyplot as plt         # This is used for visualization purpose
from datetime import datetime     # This is used to access real time and date
print("-"*15, "WELCOME TO YOUR STUDY ASSISTANT", "-"*15)
print("This chatbot is made to help you with your study",end="\n")
print("-"*100)
class Student:            # This is a class, which can be accesed later on in this project
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def __str__(self):
        return(f"---------------WELCOME grade {self.grade} aspirant Mr.{self.name}-----------------")

name_student=str(input("Enter your name: ")).upper()
while True:                  # This is looping and will check the case if it is true 
 try: 
  student_grade=int(input("Enter your Grade(<=12): "))
  if 1<=student_grade<=12:
     break
  else:
     print("*"*15,"Invalid Class","*"*15)
     print("*"*100)
 except ValueError:
     print("----------------Please enter a valid integer----------------")
     print("*"*100)


student_details=Student(name_student,student_grade)
print(student_details)
features_list=["EXPECTED RESULT EVALUATION", "NORMAL QUESTIONS", "STUDY HELP (ONLY FOR GRADE:11)"]  # This is list 
for index, item in enumerate(features_list):   # This line is used to give the index numbering to the objects inside of the list
 print(f"{index + 1}. {item}",end="\n")
print("-"*100)
required_feature=int(input("Enter the feature you want(1-3):"))
try:
 if required_feature==1:
   subjects=["MATH","ENGLISH","PHYSICS","CHEMISTRY","COMPUTER","NEPALI"]
   marks=[]       # This list is kept empty for the user to enter their marks
   print("Enter your expected marks for each subjects on scale of 100:")
   while True:
      score_total=0
      for sub in range(6):
         ask_mark=int(input(f"Enter your mark in {subjects[sub]}:"))   
         if 0<=ask_mark<=40:
            print("----SORRY TO HEAR THAT. BETTER LUCK NEXT TIME----")
         elif 41<=ask_mark<=60:
            print("---GREAT TO HEAR THAT. YOU ARE EXPECTED TO BE PASS. WORK MORE HARD NEXT TIME----")
         elif 61<=ask_mark<=80:
            print("---WONDERFUL, KEEP IT UP----")
         elif 81<=ask_mark<=100:
            print("---Excellent. YOU ARE GOING TO ROCK THIS TIME------")
         else:
            print("----------INVALID MARK------------------")
            print("*"*100)
         marks.append(ask_mark)
         score_total+=ask_mark
         print("-"*100)
      print(f"Your expected percentage is: {(score_total/600)*100} %")  
      plt.bar(subjects,marks, color="green")                            # This line is used to make a bar chart of the information 
      plt.title("SEE THE BAR CHART AND WORK ON SUBJECTS WHOSE SCORES ARE LOW")
      plt.xlabel("SUBJECTS")            # This is used for labeling the x-axis of bar chart
      plt.ylabel("MARKS")               # This is used for labeling the y-axis of bar chart
      plt.show()
      break                                         # This line is used to end the loop
 elif required_feature==2:
   print("-"*100)
   questions_list=["TODAYS DATE AND TIME","ABOUT MY DEVELOPER","ABOUT IMPROVING CONCENTRATION","ABOUT TIMETABLE"]
   print("These are few questions you can ask:")
   for index, item in enumerate(questions_list):
     print(f"{index + 1}. {item}",end="\n")
   print("-"*100)
   ask_user=int(input("What you want to know?(1-4):")) 
   if ask_user==1:
      current_datetime=datetime.now()
      print(f"Current date and time:{current_datetime}")
      print("-"*100)
   elif ask_user==2:
      print("My coder is Bibek Yadav. He is a high school graduate student looking for CS as his carrier")
      print("-"*100)
   elif ask_user==3:
      with open("Study Assistance system/concentration.txt","r") as file:
       content=file.read()
       print(content)
      game=str(input("DO you want to play SCRAMBLE GAME to improve concentration?(Yes if you want else type anything):")).lower()
      if game=="yes":
         words=["computer","encyclopedia","programmer","attribute","aerospace","entrepreneur","neuron"]
         print("=== WORD SCRAMBLE GAME ===")
         score=0
         for i in range(5):
            word=random.choice(words)         # This line is used to select any random word from the given list
            scrambled=''.join(random.sample(word,len(word)))        # This line is used to make the selected random word scrambled
            print(f"\nScrambled Word:{scrambled}")
            start=time.time()                                # This line is used to start the timer 
            guess=input("Your Guess: ").lower()
            end=time.time()                                  # This line is used to end the timer
            if guess==word: 
             print("------------Correct!----------------")
             score+=1
             print(f"Time taken:{round(end-start,2)}sec")
            else:
              print(f"Wrong! The correct word was:{word}")
         print(f"\nYour Final Score:{score}/5")
         print("*"*100)
      else:
         print("---------------THANK YOU------------------------")
   elif ask_user==4:
      print("Time table depends upon person to person. At least include 4 hours of serious study in your daily routein.")
      print("Try to find out the fix time of each activity and follow that on daily basis to make it habit.")
      print("-"*100)
   else:
      print("---------------INVALID QUESTION-----------------------")
 elif required_feature==3:
     if student_grade==11:
        print("The list of subjects are:")
        print("-"*50)
        subject_list11=["MATH","PHYSICS","CHEMISTRY","COMPUTER SCIENCE"]
        for subject in subject_list11:                 # This loop works if it satisfies the condition
            print(subject)  
        print("-"*100)  
        Choose_subject11=str(input("Enter the subject you want assistance with:")).upper()
         
        if Choose_subject11 in subject_list11:
            match Choose_subject11:                            # match-case is used to acess only the data which users wants
                case "MATH":
                   print("----------These are the topica included in your cirriculum activity-------------")
                   math_list11=["ALGEBRA","TRIGONOMETRY","ANALYTIC GEOMETRY","VECTORS",
                                "STATISTICS AND PROBABILITY","CALCULUS","COMPUTATIONAL METHOD"] 
                   for index, item in enumerate(math_list11):
                      print(f"{index + 1}. {item}")
                   print("-"*100)
                   math_topics=int(input("Enter the topic number(1-7) you are facing problem in:"))
                   print("*"*100)
                   while 1<=math_topics<=7:
                      match math_topics:
                        case 1:
                          with open("Study Assistance system/Math11/algebra.txt", "r") as file:      # This line is used to access the file without giving any system error
                           content = file.read()  # Read the entire content of the file
                           print(content)
                           print("*"*100)
                        case 2:
                          with open("Study Assistance system/Math11/trigonometry.txt","r") as file:
                            content=file.read()
                            print(content)
                            print("*"*100)
                        case 3:
                         with open("Study Assistance system/Math11/analytic.txt","r") as file:
                            content=file.read()
                            print(content)
                            print("*"*100)
                        case 4:
                          with open("Study Assistance system/Math11/vectors.txt","r") as file:
                            content=file.read()
                            print(content) 
                            print("*"*100) 
                        case 5:
                          with open("Study Assistance system/Math11/statistics.txt","r") as file:
                            content=file.read()
                            print(content) 
                            print("*"*100)   
                        case 6:
                          with open("Study Assistance system/Math11/calculus.txt","r") as file:
                            content=file.read()
                            print(content) 
                            print("*"*100) 
                        case 7:
                          with open("Study Assistance system/Math11/computational.txt","r") as file:
                            content=file.read()
                            print(content) 
                            print("*"*100)   
                        case _:                           # This line checks for every invalid inputs whcich is not the actual case
                          print("------------------------INVALID TOPIC-------------------------")
                      break
                    
                case "PHYSICS":
                  print("----------These are the topica included in your cirriculum activity-------------")
                  physics_list11=["MECHANICS","HEAT AND THERMODYNAMICS","WAVE AND OPTICS",
                                  "ELECTRICITY AND MAGNETISM","MODERN PHYSICS"]
                  for index, item in enumerate(physics_list11):
                   print(f"{index + 1}. {item}")
                  print("*"*100)
                  physics_topics=int(input("Enter the topic number(1-5) you are facing problem in:"))
                  print("*"*100)
                  while 1<=physics_topics<=5:
                    match physics_topics:
                      case 1:
                        with open("Study Assistance system/Physics11/mechanics.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 2:
                        with open("Study Assistance system/Physics11/thermo.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 3:
                        with open("Study Assistance system/Physics11/optics.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 4:
                        with open("Study Assistance system/Physics11/electric.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 5:
                        with open("Study Assistance system/Physics11/modern.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case _:
                        print("--------------------INVALID TOPIC-----------------")
                        print("*"*100)
                    break
              
                case "CHEMISTRY":
                  print("----------These are the topica included in your cirriculum activity-------------")
                  Chemistry_list11=["STOICHIOMETRY","ATOMIC STRUCTURE","CLASSIFICATION OF ELEMENTS AND PERODIC TABLE",
                                    "CHEMICAL BONDING AND SHAPE OF MOLECULES",
                                    "OXIDATION AND REDUCTION","STATES OF MATER","CHEMICAL EQUILIBRIUM","INORGANIC CHEMISTRY"
                                    ,"ORGANIC CHEMSITRY"]
                  for index, item in enumerate(Chemistry_list11):
                   print(f"{index + 1}. {item}")
                  print("*"*100)
                  chemistry_topics=int(input("Enter the topic number(1-9) you are facing problem in:"))
                  print("*"*100)
                  while 1<=chemistry_topics<=9:
                    match chemistry_topics:
                      case 1:
                        with open("Study Assistance system/Chemistry11/stoichem.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 2:
                        with open("Study Assistance system/Chemistry11/atomic.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 3:
                        with open("Study Assistance system/Chemistry11/perodic.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 4:
                        with open("Study Assistance system/Chemistry11/bonding.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 5:
                        with open("Study Assistance system/Chemistry11/redox.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 6:
                        with open("Study Assistance system/Chemistry11/matter.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 7:
                        with open("Study Assistance system/Chemistry11/equilibrium.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 8:
                        with open("Study Assistance system/Chemistry11/inorganic.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 9:
                        with open("Study Assistance system/Chemistry11/organic.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case _:
                        print("------------------INVALID TOPIC---------------------")
                case "COMPUTER SCIENCE":
                  print("----------These are the topica included in your cirriculum activity-------------")
                  Computer_list11=["COMPUTER SYSTEM","NUMBER SYSTEM AND CONVERSION BOOLEAN LOGIC",
                                   "COMPUTER SYSTEM AND SOFTWARE SYSTEM","APPLICATION PACKAGE",
                                   "PROGRAMMING CONCEPTCS AND LOGICS","WEB TECHNOLOGY-I",
                                   "MULTIMEDIA","INFORMATION AND SECURITY LAW"]
                  for index, item in enumerate(Computer_list11):
                   print(f"{index + 1}. {item}")
                  print("*"*100)
                  computer_topics=int(input("Enter the topic number(1-8) you are facing problem in:"))
                  print("*"*100)
                  while 1<=computer_topics<=8:
                    match computer_topics:
                      case 1:
                       with open("Study Assistance system/Computer/system.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 2:
                        with open("Study Assistance system/Computer/numbersys.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 3:
                        with open("Study Assistance system/Computer/software.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 4:
                        with open("Study Assistance system/Computer/appication.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 5:
                        with open("Study Assistance system/Computer/programming.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 6:
                        with open("Study Assistance system/Computer/web_technology.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 7:
                        with open("Study Assistance system/Computer/multimedia.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case 8:
                        with open("Study Assistance system/Computer/security.txt", "r") as file:
                         content = file.read()  # Read the entire content of the file
                         print(content)
                         print("*"*100)
                      case _:
                        print("---------------------INVALID TOPICS--------------------")

                    break
                case _:
                 print("----------------------INVALID SUBJECT-----------------------------")
        else:
            print("*"*15,"The subject is Invalid","*"*15)           
     else:
       print("*"*20,"YOU ARE NOT GRADE 11 STUDENT","*"*20)
       print("*"*20,"YOU CANNOT USE THIS FEATURE","*"*20)

 else:
   print("----------------------------INVALID INPUT---------------------------")
except ValueError:             # This line handles the valueerror if user enters the value which is not in programe
    print("Please enter a valid number.")