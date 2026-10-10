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
    for application in applications:
        print(application["Company"],"|",application["Role"],"|",application["Location"],"|",application["Status"],"|",application["Skills"])


def add_application(applications,company,role,location,status,skills):
    application={
        "Company": company.title(),
        "Role": role.title(),
        "Location": location.title(),
        "Status": status.title(),
        "Skills": skills
    }

    applications.append(application)

#DAY 2:Search and Update Status
def find_application(applications,search):
    for application in applications:
        if search.lower()==application["Company"].lower():
            return application

    return None


def search_application(applications):
    search = input("Enter the company to search:")

    application=find_application(applications,search)

    if application is not None:
        print("Application found!\n")
        display_application(application)
    else:
        print("No application found for this company!")


def update_status(applications):
    search=input("Enter the company to update:")

    application=find_application(applications,search)

    if application is not None:
        new_status=input("Enter new status:")

        application["Status"]=new_status.title()

        print("Status updated!\n")
        display_application(application)
    else:
        print("No application found for this company!")

#DAY 3: Count Applications by Status
def count_applications_by_status(applications):
    status_count={}

    for application in applications:

        status=application["Status"]

        if status in status_count:
           status_count[status]=status_count[status]+1
        else:
           status_count[status]=1

    print("Application count by status:")

    for current_status,count in status_count.items():
        print(current_status,":",count)

#DAY 4: Most Common Skill
def common_skills(applications):

    skill_count={}

    for application in applications:

        skills=application["Skills"].split(",")

        for skill in skills:
            skill=skill.strip()
            if skill in skill_count:
               skill_count[skill]=skill_count[skill]+1
            else:
               skill_count[skill]=1

    highest=0
    common_skill=""
    for skill,count in skill_count.items():
        if count>highest:
            highest=count
            common_skill=skill

    print("Most common skill:",common_skill)

#DAY 5:Readability
def display_application(application):

    print(
        "Company:", application["Company"], "\n",
        "Role:", application["Role"], "\n",
        "Location:", application["Location"], "\n",
        "Status:", application["Status"], "\n",
        "Skills:", application["Skills"], "\n",
        sep="")

#DAY 6:Input validation

def get_valid_input(field):
    value=input("Enter the " + field +":").strip()
    while value=="":
        print(field +" cannot be empty.")
        value=input("Enter the "+ field +":").strip()

    return value

def display_menu():
    print(""" 
================ Job Application Tracker ================

1.Add application
2.View application 
3.Search by Company 
4.Update Status 
5.Count Applications by Status 
6.Find most common skill 
7.Exit
""")


while True:
        display_menu()
        try:
            choice=int(input("Choose an option:"))

            if choice==1:

                company = get_valid_input("Company")
                role = get_valid_input("Role")
                location = get_valid_input("Location")
                status = get_valid_input("Status")
                skills = get_valid_input("Skills")

                add_application(applications, company, role, location, status, skills)

            elif choice==2:
                display_applications(applications)

            elif choice==3:
                search_application(applications)

            elif choice==4:
                update_status(applications)

            elif choice==5:
                count_applications_by_status(applications)

            elif choice==6:
                common_skills(applications)

            elif choice==7:
                break

            else:
                print("Invalid option. Please choose a number from 1 to 7.")

        except ValueError:
            print("Please enter a number from 1 to 7.")





