import pandas as pd
from matplotlib import pyplot as mypy
print("")
print("-"*48," CrimeMap ","-"*48)

print("\nWelcome to CrimeMap - an intuitive platform to explore crime data, trends, and patterns by location and time,\ndelivering clear, data-driven insights!\n")

def main_menu():
    print("                                          - MENU -                                         ")
    options={
        1:"View Overall Crime Statistics",
        2:"IPC Crimes Over The Years",
        3:"Crimes in Metropolitan Cities",
        4:"Metropolitan Cities - Statistics",
        5:"Search by Type of Crime (States & UTs)",
        6:"Arrests, Convictions & Acquittals (States & UTs)",
        7:"Exit"
    }
    for u,v in options.items():
        print(f"     {u}.{v}")
    print("")

def page_maker(page_title,dict):
    print("\n","-"*25,page_title,"-"*25,"\n")
    
    for i,j in dict.items():
        print(f"       {i}. {j}")
    
    print("")
def graphs_year_choice(df,x):
    yn=input("Do you wish to see the graphical representation of the above data? (y/n): ")
    if yn=='y' or yn=='Y':
        year=input("enter year (2020 to 2022): ")
        if year in [2020,2021,2022]:
            mypy.bar(df[x],df[year])
            mypy.xticks(rotation=45,ha='right',fontsize=7)
            mypy.show()
            print("\nReturning to the Main Menu...\n")
        else:
            print("Invalid input, please retry...")
            return graphs_year_choice(df,x)
    elif yn=='n' or yn=='N':
        print("Thank you! Returning to the Main Menu...\n")
    else:
        print("Invalid input, please retry...")
        return graphs_year_choice(df,x)
def graphs(df,x,y):
    yn=input("Do you wish to see the graphical representation of the above data? (y/n): ")
    if yn=='y' or yn=='Y':
        mypy.plot(df[x],df[y])
        mypy.xticks(rotation=45,ha='right',fontsize=7)
        mypy.xlabel(x,fontsize=10)
        mypy.ylabel(y,fontsize=10)
        mypy.show()
        print("\nReturning to the Main Menu...\n")
    elif yn=='n' or yn=='N':
        print("Thank you! Returning to the Main Menu...\n")
    else:
        print("Invalid input, please retry...")
        return graphs(df,x,y)


def page1():
    pg1={
        1: "IPC Crimes (2020-2022)",
        2: "SLL Crimes (2020-2022)",
        3: "Total Crimes - IPC & SLL (2020-2022)"
    }
    page_maker("Overall Crime Statisics",pg1)
    choice=input("Enter sub-page number to continue: ")

    if choice=='1':
        data=pd.read_csv("IPC_crimes_total.csv")
        print("                     - IPC Crimes -                      ")
        print(data,"\n")
        graphs_year_choice(data,'State/UT')
    
    elif choice=='2':
        data=pd.read_csv("SLL_crimes_total.csv")
        print("                     - SLL Crimes -                      ")
        print(data,"\n")
        graphs_year_choice(data,'State/UT')
    
    elif choice=='3':
        data=pd.read_csv("total_crimes.csv")
        print("                     - Total Crimes -                      ")
        print(data,"\n")
        graphs_year_choice(data,'State/UT')
    
    else:
        print("Invalid input; returning to previous page...")
        return page1()

def page2():
    pg2={
        1: "Crime Incidences",
        2: "Crime Rate",
        3: "Charge-Sheeting Rate"
    }
    page_maker("IPC Crimes Over The Years",pg2)
    choice=input("Enter sub-page number to continue: ")
    data=pd.read_csv("IPC_crimes_years.csv")

    if choice=='1':
        print("\n",data[["Year","Crime Incidences"]])
        graphs(data,'Year','Crime Incidences')
    elif choice=='2':
        print("\n",data[["Year","Crime Rate"]])
        graphs(data,'Year','Crime Rate')
    elif choice=='3':
        print("\n",data[["Year","Charge-sheeting Rate"]])
        graphs(data,'Year','Charge-sheeting Rate')
    else:
        print("Invalid input; returning to previous page...")
        return page2()

def page3():
    pg3={
        1: "IPC Crimes (2020-2022)",
        2: "SLL Crimes (2020-2022)",
        3: "Total IPC & SLL Crimes (2020-2022)"
    }
    page_maker("Crimes in Metropolitan Cities",pg3)
    choice=input("Enter sub-page number to continue: ")

    if choice=='1':
        data=pd.read_csv("metropolitan_IPC.csv")
        print("                     - IPC Crimes -                      ")
        print(data,"\n")
        graphs_year_choice(data,'City')
    
    elif choice=='2':
        data=pd.read_csv("metropolitan_SLL.csv")
        print("                     - SLL Crimes -                      ")
        print(data,"\n")
        graphs_year_choice(data,'City')
    
    elif choice=='3':
        data=pd.read_csv("metropolitan_total.csv")
        print("                     - Total Crimes -                      ")
        print(data,"\n")
        graphs_year_choice(data,'City')
    
    else:
        print("Invalid input; returning to previous page...")
        return page3()

def page4():
    pg4={
        1: "Rate of Cognizable Crimes (2022)",
        2: "Charge-Sheeting Rate (2022)"
    }
    page_maker("Crimes in Metropolitan Cities",pg4)
    choice=input("Enter sub-page number to continue: ")
    data=pd.read_csv("metropolitan_total.csv")

    if choice=='1':
        print("\n",data[['City','Rate of Cognizable Crime']])
        graphs(data,'City','Rate of Cognizable Crime')
    elif choice=='2':
        print("\n",data[['City','Charge-Sheeting Rate']])
        graphs(data,'City','Charge-Sheeting Rate')
    else:
        print("Invalid input; returning to previous page...")
        return page4()

def page5():
    crime_type={
        '1':'Violent Crimes',
        '2':'Murder',
        '3':'Kidnapping & Abduction',
        '4':'Crime Against Women',
        '5':'Crime Against Children',
        '6':'Cyber Crimes',
        '7':'Human Trafficking'
    }
    page_maker("Search by Type of Crime",crime_type)
    choice=input("Enter sub-page number to continue: ")
    
    crime_num=pd.read_csv("crimewise_num.csv")
    crime_rate=pd.read_csv("crimewise_rate.csv")
    chargesheeting_rate=pd.read_csv("chargesheeting_rate_crimewise.csv")

    print("\nThe following pages are available for exploration:")
    print("         1. Number of",crime_type[choice],"in 2022")
    print("         2. Rate of",crime_type[choice])
    print("         3. Chargesheeting Rate\n")
    choice0=input("Please enter the desired page number to continue: ")

    if choice0=='1':
        print("\n\n",crime_num[['State/UT',crime_type[choice]]])
        graphs(crime_num,'State/UT',crime_type[choice])
    elif choice0=='2':
        print("\n\n",crime_rate[['State/UT',crime_type[choice]]])
        graphs(crime_rate,'State/UT',crime_type[choice])
    elif choice0=='3':
        print("\n\n",chargesheeting_rate[['State/UT',crime_type[choice]]])
        graphs(chargesheeting_rate,'State/UT',crime_type[choice])
    else:
        print("Invalid input; returning to previous page...")
        return page5()

def page6():
    pg6={
        1: "Age Groups - Persons Arrested under IPC Crimes",
        2: "Gender-wise Persons Arrested under IPC Crimes)",
        3: "Disposal of Persons Arrested Under IPC Crimes"
    }
    page_maker("Arrests, Convictions & Acquittals",pg6)
    choice=input("Please enter the desired page number to continue: ")

    if choice=='1':
        data=pd.read_csv("agewise_arrested.csv")
        print("\n             - Age Groups of Persons Arrested Under IPC Crimes -                 ")
        print(data,"\n")
        yn=input("Do you wish to see the graphical representation of the above data? (y/n): ")

        if yn=='y' or yn=='Y':
            mypy.plot(data['State/UT'],data['Juveniles Apprehended'],label='Juveniles Apprehended')
            mypy.plot(data['State/UT'],data['18 Years & Above - Below 30 Years'],label='18 Years & Above - Below 30 Years')
            mypy.plot(data['State/UT'],data['30 Years & above - Below 45 Years'],label='30 Years & above - Below 45 Years')
            mypy.plot(data['State/UT'],data['45 Years & above - Below 60 Years'],label='45 Years & above - Below 60 Years')
            mypy.plot(data['State/UT'],data['60 Years & Above'],label='60 Years & Above')
            mypy.legend()
            mypy.xticks(rotation=45,ha='right',fontsize=7)
            mypy.show()
        elif yn=='n' or yn=='N':
            print("Thank you! Returning to the Main Menu...\n")
        else:
            print("Invalid input; returning to the previous page...")
            return page6()

    elif choice=='2':
        data=pd.read_csv("genderwise_arrested.csv")
        print("\n             - Gender Wise Persons Arrested Under IPC Crimes -                 ")
        print(data,"\n")
        yn=input("Do you wish to see the graphical representation of the above data? (y/n): ")

        if yn=='y' or yn=='Y':
            mypy.plot(data['State/UT'],data['Male'],label='Male')
            mypy.plot(data['State/UT'],data['Female'],label='Female')
            mypy.plot(data['State/UT'],data['Trans'],label='Trans')
            mypy.legend()
            mypy.xticks(rotation=45,ha='right',fontsize=7)
            mypy.show()
        elif yn=='n' or yn=='N':
            print("Thank you! Returning to the Main Menu...\n")
        else:
            print("Invalid input; returning to the previous page...")
            return page6()

    elif choice=='3':
        data=pd.read_csv("arrested_persons_disposal.csv")
        print("\n             - Disposal of Persons Arrested Under IPC Crimes -                 ")
        print(data,"\n")
        yn=input("Do you wish to see the graphical representation of the above data? (y/n): ")

        if yn=='y' or yn=='Y':
            mypy.bar(data['State/UT'],data['Persons Arrested'],label='Arrested')
            mypy.bar(data['State/UT'],data['Persons Convicted'],label='Convicted')
            mypy.bar(data['State/UT'],data['Persons Discharged'],label='Discharged')
            mypy.bar(data['State/UT'],data['Persons Acquitted'],label='Acquitted')
            mypy.legend()
            mypy.xticks(rotation=45,ha='right',fontsize=7)
            mypy.show()
        elif yn=='n' or yn=='N':
            print("Thank you! Returning to the Main Menu...\n")
        else:
            print("Invalid input; returning to the previous page...")
            return page6()
    else:
        print("Invalid input; returning to the previous page...")
        return page6()

while True:
    main_menu()
    opt=input("Enter the page number to continue: ")
    if opt=='1':
        page1()
    elif opt=='2':
        page2()
    elif opt=='3':
        page3()
    elif opt=='4':
        page4()
    elif opt=='5':
        page5()
    elif opt=='6':
        page6()
    elif opt=='7':
        print("Thank you for using the program. Exiting...")
        break
    else:
        print("Invalid input; please try again.\n\n")
