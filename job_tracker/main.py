#DAY 1: Basic Job Application Tracker

application1={
    "Company":"TCS",
     "Role":"Data Analyst",
    "Location":"Pune",
     "Status":"Applied",
    "Skills":"Python,SQL,Power BI"
}

application2={
     "Company":"Infosys",
     "Role":"Python Developer",
    "Location":"Bengaluru",
     "Status":"Interview",
    "Skills":"Python,SQL"

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
    "Skills":"Python,ML"

}

application5={
    "Company":"Cognizant",
    "Role":"Python Developer",
    "Location":"Hyderabad",
    "Status":"Applied",
    "Skills":"Python,SQL,Git"
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

#DAY 2:Search and Update Status
def search_application(applications):
    search = input("Search the name of the company:")

    found=False

    for x in applications:
        if search.lower() == x["Company"].lower():
            print("Company application exists!\n",x)
            found=True

    if not found:
        print("Oops.Company doesn't exist!")


def update_status(applications):
    search=input("Enter the company name to update the status:")

    found=False

    for x in applications:
        if x["Company"].lower() == search.lower():
            new_status=input("Enter new status:")
            x["Status"]=new_status.title()
            print("Status updated",x)
            found=True

    if not found:
        print("Company doesn't exist!")

#DAY 3: Count Applications by Status
def count_applications_by_status(applications):
    status_count={}

    for x in applications:

        status=x["Status"]

        if status in status_count:
           status_count[status]=status_count[status]+1
        else:
           status_count[status]=1

    print("Application count by status:")

    for x,y in status_count.items():
        print(x,":",y)

#DAY 4: Most Common Skill
def common_skills(applications):

    skill_count={}

    for x in applications:

        skills=x["Skills"].split(",")

        for i in skills:
            if i in skill_count:
               skill_count[i]=skill_count[i]+1
            else:
               skill_count[i]=1

    highest=0
    for x,y in skill_count.items():
        if y>highest:
            highest=y
            name=x

    print("Most common skill:",name)



user=int(input("1.Add application 2.View application 3.Search by Company 4.Update Status 5.Count Applications by Status 6.Find most common skill 7.Exit \n"))

while user!=7:
    if user==1:
        Company = input("Enter name of the company:")
        Role = input("Enter name of the role:")
        Location = input("Enter name of the location:")
        Status = input("Enter name of the status:")
        Skills = input("Enter name of the skills:")
        add_application(Company, Role, Location, Status, Skills)

    elif user==2:
        display_applications(applications)

    elif user==3:
        search_application(applications)

    elif user==4:
        update_status(applications)

    elif user==5:
        count_applications_by_status(applications)

    elif user==6:
        common_skills(applications)

    else:
        print("Invalid input!!!")

    user = int(input("\n1.Add application 2.View application 3.Search by Company 4.Update Status 5.Count Applications by Status 6.Find most common skill 7.Exit\n"))






