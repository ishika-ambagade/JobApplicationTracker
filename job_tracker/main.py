#DAY-1

application1={
    "Company":"TCS",
     "Role":"Data Analyst",
    "Location":"Pune",
     "Status":"Applied",
    "Skills":"Python, SQL, Power BI"
}

application2={
     "Company":"Infosys",
     "Role":"Python Developer",
    "Location":"Bengaluru",
     "Status":"Interview",
    "Skills":"Python, SQL"

}

application3 ={
     "Company":"Wipro",
     "Role":"Data Analyst",
    "Location":"Mumbai",
     "Status":"Rejected",
    "Skills":"Python,Excel"

}

application4 ={
     "Company":"Accenture",
     "Role":"AI Intern",
    "Location":"Pune",
     "Status":"Applied",
    "Skills":"Python, ML"

}

application5={
    "Company":"Cognizant",
    "Role": "Python Developer",
    "Location": "Hyderabad",
    "Status": "Applied",
    "Skills": "Python, SQL, Git"
}

applications=[application1,application2,application3,application4,application5]

def display_applications(applications):
    for x in applications:
        print(x["Company"],"|",x["Role"],"|",x["Location"],"|",x["Status"])



def add_application(company,role,location,status,skills):
    application={
        "Company": company.title(),
        "Role": role.title(),
        "Location": location.title(),
        "Status": status.title(),
        "Skills": skills.title()
    }

    applications.append(application)



user=int(input("1.Add application 2.View application 3.Exit \n"))

while user!=3:
    if user==1:
        Company = input("Enter name of the company:")
        Role = input("Enter name of the role:")
        Location = input("Enter name of the location:")
        Status = input("Enter name of the status:")
        Skills = input("Enter name of the skills:")
        add_application(Company, Role, Location, Status, Skills)

    elif user==2:
        display_applications(applications)

    else:
        print("Invalid input!!!")

    user = int(input("1.Add application 2.View application 3.Exit"))





