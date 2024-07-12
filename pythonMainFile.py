import pandas as pd

data = pd.read_csv('D:\Python\PythonProjects\BBDataAnalysisProject\Automobile.csv')
print(data)
print(data.columns)

name = data['name']
print(name)

mpg = data['mpg']
print(mpg)

cylinders = data['cylinders']
print(cylinders)

displacement = data['displacement']
print(displacement)

horsepower = data['horsepower']
print(horsepower)

weight = data['weight']
print(weight)

acceleration = data['acceleration']
print(acceleration)

model_year = data['model_year']
print(model_year)

origin = data['origin']
print(origin)




def analyze1():

    # Analyze of how many cars are there from particular country

    # importing libraries
    import pandas as pd
    import matplotlib.pyplot as plt

    # reading the data from csv file
    data = pd.read_csv('D:\Python\PythonProjects\CarsDataAnalysisProject\Automobile.csv')

    # Getting the origin list from main data

    origin = data['origin']

    # Getting the unique origin names list
    
    originNameList = []
    for item in origin:
        if item not in originNameList:
            originNameList.append(item)
    print(originNameList)

    # Getting the origins count    
    
    # making a list same size as the unique origin names list 
    originNameCount = []
    for item in originNameList:
        originNameCount.append(0)
    
    # Filling the list with unique origins count value
    for index, row in data.iterrows():
        if row['origin'] == 'usa':
            originNameCount[0]+=1
        elif row['origin'] == 'japan':
            originNameCount[1]+=1
        elif row['origin'] == 'europe':
            originNameCount[2]+=1
    
    print(originNameCount)
    
    # data visualizing with matplotlib in bar chart
    plt.bar(originNameList, originNameCount, width=0.3, color=['r', 'b', 'g'], 
            label=originNameList)
    plt.xlabel('Countries')
    plt.ylabel('Count of cars')
    plt.title('Countries cars production')
    plt.legend()
    
    #saving the figure
    #plt.savefig('D:\Python\PythonProjects\CarsDataAnalysisProject\Analyze1.jpg')
    plt.show()

analyze1()




def analyze2():
    # Analyze of how many cars are there from different years
    
    # importing the libraries
    import pandas as pd
    import matplotlib.pyplot as plt

    # reading the data using csv file
    data = pd.read_csv('D:\Python\PythonProjects\CarsDataAnalysisProject\Automobile.csv')

    # Getting the years list from main data

    full_year = data['full_year']

    # Getting the unique years list
    yearList = []
    for item in full_year:
        if item not in yearList:
            yearList.append(item)
    print(yearList)

    # Getting cars with different years count
    
    # to make array same size as unique years list size
    yearCount=[]
    for item in yearList:
        yearCount.append(0)
    
    # Filling the values with unique years count values
    for index, row in data.iterrows():
        if row['full_year'] == 1970:
            yearCount[0]+=1
        elif row['full_year'] == 1971:
            yearCount[1]+=1
        elif row['full_year'] == 1972:
            yearCount[2]+=1
        elif row['full_year'] == 1973:
            yearCount[3]+=1
        elif row['full_year'] == 1974:
            yearCount[4]+=1
        elif row['full_year'] == 1975:
            yearCount[5]+=1
        elif row['full_year'] == 1976:
            yearCount[6]+=1
        elif row['full_year'] == 1977:
            yearCount[7]+=1
        elif row['full_year'] == 1978:
            yearCount[8]+=1
        elif row['full_year'] == 1979:
            yearCount[9]+=1
        elif row['full_year'] == 1980:
            yearCount[10]+=1
        elif row['full_year'] == 1981:
            yearCount[11]+=1
        elif row['full_year'] == 1982:
            yearCount[12]+=1
            
    print(yearCount)
    
    # data visualizing with matplotlib in bar chart
    
    plt.pie(yearCount, labels=yearList, startangle=90, shadow=True, autopct='%.1f%%')
    plt.title('Manufacture by year')
    
    #saving the figure
    #plt.savefig('D:\Python\PythonProjects\CarsDataAnalysisProject\Analyze2.jpg')
    plt.show()
    
analyze2()




def analyze3():
    
    # Horsepower of Toyota cars
    
    # importing key libraries for this project
    import pandas as pd
    import matplotlib.pyplot as plt
    from numpy import random

    # taking data from a csv file
    data = pd.read_csv('D:\Python\PythonProjects\CarsDataAnalysisProject\Automobile.csv')

    # analyze the data
    
    # making two empty lists for the analyze
    toyotaCarsList = []
    toyotaCarsHorsepowerList = []

    # Filling the two lists with some data
    for index, row in data.iterrows():
        if 'toyota' in row['name']:
            toyotaCarsList.append(row['name'])
            toyotaCarsHorsepowerList.append(row['horsepower'])
        
    print(toyotaCarsList)
    print(toyotaCarsHorsepowerList)

    
    # visualize the data
    plt.scatter(toyotaCarsHorsepowerList, toyotaCarsList, marker='D',
                c=random.randint(1,100, len(toyotaCarsList)) , cmap='flag')
    plt.xlabel('horsepower')
    plt.title('Horsepower of Toyota cars')
    
    #saving the figure
    #plt.savefig('D:\Python\PythonProjects\CarsDataAnalysisProject\Analyze3.jpg')
    plt.show()
        
analyze3()




def analyze4():
    # importing libraries
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd

    # reading the data using pandas library
    data = pd.read_csv('D:\Python\PythonProjects\CarsDataAnalysisProject\Automobile.csv')


    # making a dataset to work with it
    carsModel = []
    carsMPG = []

    for index,row in data.iterrows():
        if 'toyota' in row['name']:
            carsModel.append('toyota')
            carsMPG.append(row['mpg'])
        elif 'ford' in row['name']:
            carsModel.append('ford')
            carsMPG.append(row['mpg'])
        elif 'audi' in row['name']:
            carsModel.append('audi')
            carsMPG.append(row['mpg'])
        elif 'chevrolet' in row['name']:
            carsModel.append('chevrolet')
            carsMPG.append(row['mpg'])
        elif 'volkswagen' in row['name']:
            carsModel.append('volkswagen')
            carsMPG.append(row['mpg'])
            
    carsMPGdata = pd.DataFrame({'Model': carsModel, 'MPG': carsMPG})

    # plotting the values using seaborn
    sns.set(style='whitegrid')
    sns.boxplot(x='Model', y='MPG', data=carsMPGdata, 
                order=['audi', 'chevrolet', 'ford', 'toyota', 'volkswagen'],
                palette='Accent')
    plt.title('Miles per gallons as per car manufacturers')
    
    #saving the figure
    #plt.savefig('D:\Python\PythonProjects\CarsDataAnalysisProject\Analyze4.jpg')
    plt.show()

analyze4()




def analyze5():
    # How much cars produced by different countries over the year 1970-73
    
    # importing libraries
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd

    # reading the data using pandas library
    data = pd.read_csv('D:\Python\PythonProjects\CarsDataAnalysisProject\Automobile.csv')
    

    # analyzing the data         
    years=[]
    country=[]
    
    for index, row in data.iterrows():
        if(row['full_year'] == 1970 or row['full_year'] == 1971 or 
        row['full_year'] == 1972 or row['full_year'] == 1973):
            years.append(row['full_year'])
            country.append(row['origin'])
    
    df = pd.DataFrame({"year": years, "country": country})
    
    
    # plotting the data for visualization
    sns.countplot(y='year', data=df, hue='country', palette='twilight')
    plt.title("Cars produced by different countries over the year 1970-73")
    
    #saving the figure
    #plt.savefig('D:\Python\PythonProjects\CarsDataAnalysisProject\Analyze4.jpg')
    plt.show()

analyze5()

