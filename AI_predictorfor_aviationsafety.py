import random      # This  is to import random values in our project
import matplotlib.pyplot as plt      # This is to access matplot library special functions to draw graph in our output

class Askweather:    # Storing the data enterd in class to access it later
    def __init__(self,city,wind,temperature,pressure,visibility):
        self.city=city
        self.wind=wind
        self.temperature=temperature
        self.pressure=pressure
        self.visibility=visibility

    def __str__(self):    # Returns the value stored in class to print it later when the class is called
      return (f"City:{self.city}, Wind:{self.wind} knots, "
                    f"Temperature:{self.temperature}°C, "
                    f"Pressure:{self.pressure} hPa, "
                    f"Visibility:{self.visibility} miles,")
                
    
    def safety_score(self):       # Method defined to calculate score 
        score=0
        count=4   # total parameters checked

        # Wind check
        if 0<=self.wind<=30:
            score+=100
        elif 30<self.wind<=50:
            score+=70
        else:
            score+=20

        # Temperature check
        if -10<=self.temperature<=35:
            score+=100
        elif 35<self.temperature<=45:
            score+=70
        else:
            score+=20


        # Pressure check
        if 980<=self.pressure<=1040:
            score+=100
        else:
            score+=40

        # Visibility check
        if self.visibility>5:
            score+=100
        elif 3<=self.visibility<=5:
            score+=70
        else:
            score+=20

        return score/count   # average out of 100


    def is_safe_to_fly(self):    # Returns the actual result by checking all the condition when it is called
        avg =self.safety_score()
        if avg>=80:
            return "Safe to fly"
        elif 50<=avg<80:
            return "Fly with caution"
        else:
            return "Unsafe to fly"
        


    def plot_safety(self):       # It is method defined to make the use of matplotlib that is graph
        parameters=['Wind','Temperature','Pressure','Visibility']   # X-axis values in bargraph
        scores=[]        # Empty Y-axis values for bargraph which is later on appended as per the actual data

        # Calculate individual parameter scores
        # Wind
        if 0<=self.wind<=30:
            scores.append(100)
        elif 30<self.wind<=50:
            scores.append(70)
        else:
            scores.append(20)

         # Temperature
        if -10<=self.temperature<=35:
            scores.append(100)
        elif 35<self.temperature<=45:
            scores.append(70)
        else:
            scores.append(20)

        # Pressure
        if 980<=self.pressure<=1040:
            scores.append(100)
        else:
            scores.append(40)

        # Visibility
        if self.visibility>5:
            scores.append(100)
        elif 3<=self.visibility<=5:
            scores.append(70)
        else:
            scores.append(20)

        # Plot
        plt.figure(figsize=(8, 5))
        plt.bar(parameters, scores, color='orange')
        plt.ylim(0, 120)
        plt.title(f"Safety Score Analysis for {self.city}")
        plt.ylabel("Score (out of 100)")
        plt.xlabel("Factors affecting weather")
        for i, v in enumerate(scores):
            plt.text(i, v + 2, str(v), ha='center')
        plt.show()


ask=input("Do you want to enter data by yourself or want random data?(self/random):").lower()

if ask=="self":     # Normal conditions
 query=input("Do you want assist to fill up the correct values at present?(yes/no):").lower()
 if query=="yes":
     print("Please click:<< windy.com >> to have assist with live values.   NOTE: steps to follow " \
     "1.open menu" \
     "2.goto setting" \
     "3.change the unit of wind to knots , temperature to degree celsius , visibility to miles and pressure to hPa ",end="\n")

     city1=input("enter the city name:")    # Asks users to enter the value by themself
     wind1=int(input("enter the wind speed in knots:"))
     temperature1=int(input("enter the temperature in celsius:"))
     pressure1=int(input("enter the pressure in hectopascals:"))
     visibility1=float(input("enter the visibility in miles:"))

     userinput=Askweather(city1,wind1,temperature1,pressure1,visibility1)    # Returning the parameters to Askweather class 
     print("\n\n")
     print(">>> Your safety is our concern and all the information is listed below <<<")
     print("\n")
     print(">>>          Safety Analysis           <<<",end="\n")
     print(        userinput.is_safe_to_fly())
     userinput.plot_safety()      # Calling plot to actually run in output
 
 else:
     city1=input("enter the city name:")
     wind1=int(input("enter the wind speed in knots:"))
     temperature1=int(input("enter the temperature in celcius:"))
     pressure1=int(input("enter the pressure in hectopascals:"))
     visibility1=float(input("enter the visibility in miles:"))

     userinput=Askweather(city1,wind1,temperature1,pressure1,visibility1)
     print("\n\n")
     print(">>> Your safety is our concern and all the information is listed below <<<")
     print("\n")
     print(">>>          Safety Analysis           <<<",end="\n")
     print(       userinput.is_safe_to_fly())
     userinput.plot_safety() 


  # Now this is to assume random values 
elif ask=="random":
    city="Kathmandu" 
    wind=random.randint(0, 50)
    temperature=random.randint(-20, 40)
    pressure=random.randint(950, 1050)
    visibility=round(random.uniform(0.5, 10), 1)

    randomdata=Askweather(city, wind, temperature, pressure, visibility)
    print("\n",randomdata)
    print(">>>            Safety Analysis          <<<",end="\n")
    print(        randomdata.is_safe_to_fly())
    randomdata.plot_safety()
   

else:   # This condition is to check if user have entered wrong input
   print("enter only self or random")
   ask=input("Do you want to enter data by yourself or want random data?(self/random):").lower()