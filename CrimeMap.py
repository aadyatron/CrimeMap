import pandas as pd
from matplotlib import pyplot as mypy


print("-------------------------------------------------------------------------------------------")
print("|                                         CrimeMap                                         |")
print("-------------------------------------------------------------------------------------------\n")

print("Welcome to CrimeMap - an intuitive platform to explore crime data, trends, and patterns by \nlocation and time, delivering clear, data-driven insights!\n")

print("                                          - MENU -                                         ")
print("1. View Overall Crime Statistics")
print("2. IPC Crimes Over The Years")
print("3. Crimes in Metropolitan Cities")
print("4. Metropolitan Cities - Statistics")
print("5. Search by Type of Crime (States & UTs)")
print("6. Arrests, Convictions & Acquittals (States & UTs)")
print("7. Exit\n")
      
opt=int(input("Enter the page number to continue: "))
print("\n")


if opt==1:                          #page1 - Crime Statistics All Over India
    print("--------------------------------- Overall Crime Statisics ---------------------------------\n")
    print("Cognizable crimes are categorized either under the 'Indian Penal Code (IPC)' or under the\n'Special and Local Laws (SLL)'. The Special and Local Laws identify criminal activities\nthat the state government frames for specific issues.\n")
    print("      1. IPC Crimes (2020-2022)")
    print("      2. SLL Crimes (2020-2022)")
    print("      3. Total Crimes - IPC & SLL (2020-2022)\n")
    choice=int(input("Enter sub-page number to continue: "))
    print("")

    if choice==1:
        data=pd.read_csv("IPC_crimes_total.csv")
        print("                     - IPC Crimes -                      ")
        print(data,"\n")
        yn=input("Do you wish to see the graphical representation of the above data? (y/n): ")

        if yn=='y' or yn=='Y':
            year=input("enter year (2020 to 2022): ")
            mypy.bar(data['State/UT'],data[year])
            mypy.xticks(rotation=45,ha='right',fontsize=7)
            mypy.show()
        if yn=='n' or yn=='N':
            print("Thank you! Exiting the program.")
        else:
            print("Invalid")

    if choice==2:
        data=pd.read_csv("SLL_crimes_total.csv")
        print("                     - SLL Crimes -                      ")
        print(data,"\n")
        yn=input("Do you wish to see the graphical representation of the above data? (y/n): ")

        if yn=='y' or yn=='Y':
            year=input("enter year (2020 to 2022): ")
            mypy.bar(data['State/UT'],data[year])
            mypy.xticks(rotation=45,ha='right',fontsize=7)
            mypy.show()
        if yn=='n' or yn=='N':
            print("Thank you! Exiting the program.")
        else:
            print("Invalid")

    if choice==3:
        data=pd.read_csv("total_crimes.csv")
        print("                     - Total Crimes -                      ")
        print(data,"\n")
        yn=input("Do you wish to see the graphical representation of the above data? (y/n): ")

        if yn=='y' or yn=='Y':
            year=input("enter year (2020 to 2022): ")
            mypy.bar(data['State/UT'],data[year])
            mypy.xticks(rotation=45,ha='right',fontsize=7)
            mypy.show()
        if yn=='n' or yn=='N':
            print("Thank you! Exiting the program.")
        else:
            print("Invalid")


if opt==2:                      #page2 - ICP Crimes (1981-2022)
    print("--------------------------------- IPC Crimes Over The Years ---------------------------------")
    print("                                         (1981-2022)\n")
    print("      1. Crime Incidences")
    print("      2. Crime Rate")
    print("      3. Charge-Sheeting Rate\n")
    choice=int(input("Enter sub-page number to continue: "))
    print("")
    data=pd.read_csv("IPC_crimes_years.csv")

    if choice==1:
        print("Do you wish to see the (a) numeric records, (b) line-plot, or (c) both?")
        ans=input("Please enter desired option: ")
        if ans=='a' or ans=='A':
            print("\n",data[["Year","Crime Incidences"]])  
        if ans=='b' or ans=='B':
            mypy.plot(data['Year'],data['Crime Incidences'])
            mypy.xticks(fontsize=7)
            mypy.xlabel("Years",fontsize=10)
            mypy.ylabel("Crime Incidence",fontsize=10)
            mypy.show()
        if ans=='c' or ans=='C':
            print("\n",data[["Year","Crime Incidences"]])
            
            mypy.plot(data['Year'],data['Crime Incidences'])
            mypy.xlabel("Years",fontsize=10)
            mypy.ylabel("Crime Incidence",fontsize=10)
            mypy.show()
        else:
            print("Invalid")

    if choice==2:
        mypy.plot(data["Year"],data["Crime Rate"])
        mypy.xlabel("Years",fontsize=10)
        mypy.title("Crime Rate (1981-2022)")
        mypy.show()

    if choice==3:
        mypy.plot(data["Year"],data["Charge-sheeting Rate"])
        mypy.xlabel("Years",fontsize=10)
        mypy.title("Charge-Sheeting Rate (1981-2022)")
        mypy.show()

if opt==3:                      #page3 - Crimes in Metropolitan Cities
    print("------------------------------- Crimes in Metropolitan Cities -------------------------------")
    print("                       (19 cities with more than 2 million population)\n")
    print("      1. IPC Crimes (2020-2022)")
    print("      2. SLL Crimes (2020-2022)")
    print("      3. Total IPC & SLL Crimes (2020-2022)\n")

    choice=int(input("Enter sub-page number to continue: "))
    print("")

    if choice==1:
        data=pd.read_csv("metropolitan_IPC.csv")
        print("                     - IPC Crimes -                      ")
        print(data,"\n")
        yn=input("Do you wish to see the graphical representation of the above data? (y/n): ")
        print("")

        if yn=='y' or yn=='Y':
            year=input("enter year (2020 to 2022): ")
            mypy.bar(data['City'],data[year])
            mypy.xticks(rotation=45,ha='right',fontsize=7)
            mypy.show()
        if yn=='n' or yn=='N':
            print("Thank you! Exiting the program.")
        else:
            print("Invalid")

    if choice==2:
        data=pd.read_csv("metropolitan_SLL.csv")
        print("                     - SLL Crimes -                      ")
        print(data,"\n")
        yn=input("Do you wish to see the graphical representation of the above data? (y/n): ")
        print("")

        if yn=='y' or yn=='Y':
            year=input("enter year (2020 to 2022): ")
            mypy.bar(data['City'],data[year])
            mypy.xticks(rotation=45,ha='right',fontsize=7)
            mypy.show()
        if yn=='n' or yn=='N':
            print("Thank you! Exiting the program.")
        else:
            print("Invalid")

    if choice==3:
        data=pd.read_csv("metropolitan_total.csv")
        print("                     - Total Crimes -                      ")
        print(data,"\n")
        yn=input("Do you wish to see the graphical representation of the above data? (y/n): ")
        print("")

        if yn=='y' or yn=='Y':
            year=input("enter year (2020 to 2022): ")
            mypy.bar(data['City'],data[year])
            mypy.xticks(rotation=45,ha='right',fontsize=7)
            mypy.show()
        if yn=='n' or yn=='N':
            print("Thank you! Exiting the program.")
        else:
            print("Invalid")

if opt==4:                      #page4 - Metropolitan Cities Crime Stats
    print("------------------------------ Metropolitan Cities - Statistics -------------------------------\n")
    print("      1. Rate of Cognizable Crimes (2022)")
    print("      2. Charge-Sheeting Rate (2022)\n")
    choice=int(input("Enter sub-page number to continue: "))

    data=pd.read_csv("metropolitan_total.csv")

    if choice==1:
        mypy.plot(data['City'],data["Rate of Cognizable Crime"])
        mypy.xticks(rotation=45,ha='right',fontsize=7)
        mypy.title("Rate of Cognizable Crime in Metropolitan Cities (2022)")
        mypy.show()

    if choice==2:
        mypy.plot(data['City'],data["Charge-Sheeting Rate"])
        mypy.xticks(rotation=45,ha='right',fontsize=7)
        mypy.title("Charge-Sheeting Rate in Metropolitan Cities (2022)")
        mypy.show()

if opt==5:                      #page5 - Search by Type of Crime
    print("------------------------------ Type of Crime (2022) -------------------------------\n")
    print("      1. Violent Crimes")
    print("      2. Murder")
    print("      3. Kidnapping & Abduction")
    print("      4. Crime Against Women")
    print("      5. Crime Against Children")
    print("      6. Cyber Crimes")
    print("      7. Human Trafficking")

    choice=int(input("Enter sub-page number to continue: "))
    
    crime_type={'1':'Violent Crimes',
                '2':'Murder',
                '3':'Kidnapping & Abduction',
                '4':'Crime Against Women',
                '5':'Crime Against Children',
                '6':'Cyber Crimes',
                '7':'Human Trafficking'}

    crime_num=pd.read_csv("crimewise_num.csv")
    crime_rate=pd.read_csv("crimewise_rate.csv")
    chargesheeting_rate=pd.read_csv("chargesheeting_rate_crimewise.csv")

    print("\nThe following pages are available for exploration:")
    print("         1. Number of",crime_type[str(choice)],"in 2022")
    print("         2. Rate of",crime_type[str(choice)])
    print("         3. Chargesheeting Rate\n")

    choice1=int(input("Please enter the desired page number to continue: "))

    if choice1==1:
        print("\n\n",crime_num[['State/UT',crime_type[str(choice)]]])

        yn=input("\nDo you wish to see the graphical representation of the above data? (y/n): ")

        if yn=='y' or yn=='Y':
            mypy.bar(crime_num['State/UT'],crime_num[crime_type[str(choice)]])
            mypy.xticks(rotation=45,ha='right',fontsize=7)
            mypy.ylabel(crime_type[str(choice)])
            mypy.show()
        if yn=='n' or yn=='N':
            print("Thank you! Exiting the program.")
        else:
            print("Invalid")

    if choice1==2:
        mypy.plot(crime_rate['State/UT'],crime_rate[crime_type[str(choice)]])
        mypy.xticks(rotation=45,ha='right',fontsize=7)
        mypy.grid()
        mypy.show()

    if choice1==3:
        mypy.plot(chargesheeting_rate['State/UT'],chargesheeting_rate[crime_type[str(choice)]])
        mypy.xticks(rotation=45,ha='right',fontsize=7)
        mypy.grid()
        mypy.show()

if opt==6:                      #page6 - Arrests, Convictions & Acquittals
    print("---------------------------- Arrests, Convictions & Acquittals -----------------------------\n")
    print("      1. Age Groups - Persons Arrested under IPC Crimes")
    print("      2. Gender-wise Persons Arrested under IPC Crimes")
    print("      3. Disposal of Persons Arrested Under IPC Crimes\n")

    choice=int(input("Please enter the desired page number to continue: "))

    if choice==1:
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
        if yn=='n' or yn=='N':
            print("Thank you! Exiting the program.")
        else:
            print("Invalid")

    if choice==2:
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
        if yn=='n' or yn=='N':
            print("Thank you! Exiting the program.")
        else:
            print("Invalid")

    if choice==3:
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
        if yn=='n' or yn=='N':
            print("Thank you! Exiting the program.")
        else:
            print("Invalid")

if opt==7:
    print("Thank you for your time! Have a great day ahead!")

        
