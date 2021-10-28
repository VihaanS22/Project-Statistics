import csv
import math
import pandas as pd
import plotly.express as px
from PIL import Image 


print("")
print("Project Statistics")
print("")
print("Hello. This is The Grapher AI. Here you can analyze many types of graphs and arithmetic operations related to Data Handling. Please choose what you want to analyze and type the exact same thing in the input given!")
print("")
print("Standard deviation")
print("Central tendancy")
print("Covid cases")
print("Statistical calculations")

print("")

choice = input("Please enter your choice :- ")

  
if(choice == "Statistical calculations"):


    print("")
    print("Standard deviation")
    print("Mean")
    print("Median")
    print("Mode")

    pro = input("Please choose one of these :- ")

    if(pro == "Standard deviation"):

        sd = Image.open(r"C:\Users\91911\OneDrive\Desktop\Coder's Corner\All Games and Apps\Python\Python games and apps\The Grapher Project\sd.jpg") 
  
        sd.show()

    if(pro == "Mean"):

        mean = Image.open(r"C:\Users\91911\OneDrive\Desktop\Coder's Corner\All Games and Apps\Python\Python games and apps\The Grapher Project\mean.jpg") 
  
        mean.show()

    if(pro == "Median"):

        median = Image.open(r"C:\Users\91911\OneDrive\Desktop\Coder's Corner\All Games and Apps\Python\Python games and apps\The Grapher Project\median.jpg") 
  
        median.show()

    if(pro == "Mode"):

        mode = Image.open(r"C:\Users\91911\OneDrive\Desktop\Coder's Corner\All Games and Apps\Python\Python games and apps\The Grapher Project\mode.jpg") 
  
        mode.show()

print("")


if(choice == "Standard deviation"):

    print("You have chosen to analyze the deviation of a set of numbers. The numbers to be deviated are : ")
    print("")
    print("60, 61, 65, 63, 98, 99, 90, 95, 91, 96")
    print("")
        
    with open("deviation.csv", newline = "") as index:
        data = csv.reader(index)
        values = list(data)

    data = values[0]

    total = 0

    for i in data:
        total += float(i)

    n = len(data)


    mean = total/n

    squared_list = []

    for i in data:
        x = int(i)-mean
        x = x**2
        squared_list.append(x)

    sum = 0

    for i in squared_list:
        sum += i

    result = sum/(n-1)
    deviation = math.sqrt(result)

    print("The standard deviation is : " , deviation)
    print("")




elif(choice == "Covid cases"):

    print("What graph do you want to view?")
    print("")
    print("Bar Graph")
    print("Line Graph")
    print("Scatter Graph")
    print("")

        
    graph = input("Please enter your choice according to the options given :-")

    if(graph == "Bar Graph"):
        
        #bar graph
        df = pd.read_csv("data.csv")
        fig = px.bar(df, x='Cases', y='Dates', color="Countries")
        fig.show()


    elif(graph == "Line Graph"):
        
        #line graph
        df = pd.read_csv("data.csv")

        fig = px.line(df, x="Dates", y="Cases", color="Countries")

        fig.show()


    elif(graph == "Scatter Graph"):

        #scatter graph
        df = pd.read_csv("data.csv")
        fig = px.scatter(df, x="Dates", y="Cases",
                    color="Countries")
        fig.show()


    else:
        print("You haven't chosen anything. We'll show you the best graph from these.")
        print(" ")
        df = pd.read_csv("data.csv")

        fig = px.line(df, x="Dates", y="Cases", color="Countries")

        fig.show()


elif(choice == "Central tendancy"):
    
    print("You have chosen to analyze the central tendancy. Which data do you want to view?")
    print("")
    print("Heights")
    print("Weights")
        
    data = input("Please enter your choice:- ")
    print("")
    if(data == "Heights"):

            
        print("Choose your calculation process:-")
        print("")
        print("Mean")
        print("Median")
        print("Mode")
        print("")
        calc = input("Please enter you choice:-")
        print("")
        if(calc == "Mean"):
            
            #mean
            with open("index.csv", newline = "") as index:
                data = csv.reader(index)
                values = list(data)

            values.pop(0)

            new_values = []

            for i in range(len(values)):
                num = values[i][1]
                new_values.append(float(num))

            n = len(new_values)
            sum = 0

            for i in new_values:
                sum += i

            mean = sum/n
            print("The mean of the heights is:" + str(mean))
        
        if(calc == "Median"):

            #median
            with open("Index.csv", newline = "") as index:
                data = csv.reader(index)
                values = list(data)

            values.pop(0)

            new_values = []

            for i in range(len(values)):
                num = values[i][1]
                new_values.append(float(num))

            n = len(new_values)

            new_values.sort()

            if(n%2 == 0):
                m1 = new_values[n//2]
                m2 = new_values[n//2-1]
                median = (m1+m2)/2

            else:
                median = new_values[n//2]

            print("Median of the heights is :", median)

        if(calc == "Mode"):
            

            #mode
            with open("Index.csv", newline = "") as index:
                data = csv.reader(index)
                values = list(data)

            values.pop(0)

            new_values = []

            for i in range(len(values)):
                num = values[i][1]
                new_values.append(float(num))

            from collections import Counter

            data = Counter(new_values)

            interval = {"50-60": 0,  "60-70" : 0, "70-80" : 0}

            for height, occurence in data.items():
                if(50<float(height)<60):
                    interval["50-60"] += occurence

                elif(60<float(height)<70):
                    interval["60-70"] += occurence

                elif(70<float(height)<80):
                    interval["70-80"] += occurence

            modeHeight, modeOccurence = 0,0

            for range, occurence in interval.items():
                if(occurence>modeOccurence):
                    modeRange, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

            mode = float((modeRange[0] + modeRange[1] ) / 2)
            print(f"mode is : {mode:2f}")


    if(data == "Weights"):
                
        print("Choose your calculation process:-")
        print("")
        print("Mean")
        print("Median")
        print("Mode")
        print("")
        calc = input("Please enter you choice:-")
        print("")
        if(calc == "Mean"):
            
            #mean
            with open("index.csv", newline = "") as index:
                data = csv.reader(index)
                values = list(data)

            values.pop(0)

            new_values = []

            for i in range(len(values)):
                num = values[i][2]
                new_values.append(float(num))

            n = len(new_values)
            sum = 0

            for i in new_values:
                sum += i

            mean = sum/n
            print("The mean of the weights is:" + str(mean))
            print("")
        
        if(calc == "Median"):

            #median
            with open("Index.csv", newline = "") as index:
                data = csv.reader(index)
                values = list(data)

            values.pop(0)

            new_values = []

            for i in range(len(values)):
                num = values[i][2]
                new_values.append(float(num))

            n = len(new_values)

            new_values.sort()

            if(n%2 == 0):
                m1 = new_values[n//2]
                m2 = new_values[n//2-1]
                median = (m1+m2)/2

            else:
                median = new_values[n//2]

            print("Median of the weights is :", median)
            print("")

        if(calc == "Mode"):
            

            #mode
            with open("Index.csv", newline = "") as index:
                data = csv.reader(index)
                values = list(data)

            values.pop(0)

            new_values = []

            for i in range(len(values)):
                num = values[i][2]
                new_values.append(float(num))

            from collections import Counter

            data = Counter(new_values)

            interval = {"100-110": 0,  "110-120" : 0, "120-130" : 0, "130-140" : 0, "140-150" : 0, "150-160" : 0}

            for weight, occurence in data.items():
                if(100<float(weight)<110):
                    interval["100-110"] += occurence

                elif(110<float(weight)<120):
                    interval["110-120"] += occurence

                elif(120<float(weight)<130):
                    interval["120-130"] += occurence

                elif(130<float(weight)<140):
                    interval["130-140"] += occurence

                elif(140<float(weight)<150):
                    interval["140-150"] += occurence

                elif(150<float(weight)<160):
                    interval["150-160"] += occurence

            modeWeight, modeOccurence = 0,0

            for range, occurence in interval.items():
                if(occurence>modeOccurence):
                    modeRange, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

            mode = float((modeRange[0] + modeRange[1] ) / 2)
            print(f"Mode of the weights is : {mode:2f}")
            print("")

else:
    print("")
    print("Thankyou for using Project Statistics.")
    print("")