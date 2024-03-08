import datetime
import re
class crowdfunding:
    def register(self):
        #------------------------------------------------------------------
        while True:
            firstname=input('please enter your first name :\n')
            if firstname.isalpha():
                break
            else:
                 print('please enter valid name :/n')
        while True:
            lastname=input('please enter your last name :\n')
            if lastname.isalpha():
                break
            else:
                print('please enter valid name :\n')
        while True:
            email=input('please enter your email :\n')
            email_regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.fullmatch(email_regex,email):
                break
            else:
                print('please enter valid email')
        while True:
            password=input('please enter new password :\n')
            pass_regex=r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d!#%*?&@$]{8,20}$"
            if re.fullmatch(pass_regex,password):
                break
            else:
                print('enter pass with at least one capital letter and one special charachter and one digit')
        while True:
            confirm=input('please confirm your password :\n')
            if confirm==password:
                break
            else:
                print('enter valid password')
       # while True:
           # phone=input('please enter your phone :\n')
           # phone_regex=r"^020?[10,11,12,15]\d{8}"
          #  if re.fullmatch(phone_regex,phone):
             #   break
          #  else:
              #
              # print('enter valid number')
    #------------------------------------------------------------------
        userdata = ",".join([firstname, lastname, email, password])
        userdata = userdata + "\n"   
    #-----------------------------------------------------
        readfile=open("usersfile.txt")
        data=readfile.readlines()

        users=[]
        for i in data:
            users.append(i.strip('\n'))  
        for user in users:
            userdetails = user.split(",")
            if userdetails[2] == email:
                print("Email Already Exits")
                readfile.close()
                self.register()
        else:
                readfile.close()  
                file = open("usersfile.txt", "a")
                file.write(userdata)
                file.close()
                print("Registration Successfully") 
    #----------------------------------------------------------  
    def login(self):
        while True:
            email = input("Please, Enter Your Email: \n")
            email_regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.fullmatch(email_regex, email):
                break
            else:
                print("Invalid Email")
        while True:
            password = input("Please, Enter Your Password: \n ")
            pass_regex=r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d!#%*?&@$]{8,20}$"
            mat = re.search(pass_regex, password)
            if mat:
                break
            else:
                print("Invalid Password ! please enter a valid Password")

        readfile = open("usersfile.txt")
        data = readfile.readlines()
        users = []
        for i in data:
            users.append(i.strip("\n"))
        for user in users:
            userdetails = user.split(",")
            if userdetails[2] == email and userdetails[3] == password:
                print("Logged in Successfully")
                mainMenu.projectmenu(email)
                readfile.close()
                break
        else:
            print("User Doesnt Exit")
            self.login()    
#crowd=crowdfunding()
#crowd.register()
#crowd.login()

#-------------------------------------------------



    def createproject(self,email):
        print("|--------------Create Project------------------|")
       
        while True:
            title = input("Please, Enter Project Title \n")
            if title.isalpha():
                break
            else:
                print("Invalid Title")
        while True:
            def is_valid_details(details):
                for char in details:
                   if not char.isalpha() and not char.isspace():
                      return False
                return True
            details = input("Please, Enter Project Details \n")
            if is_valid_details(details):
                break
            else:
                print("Invalid details")
        while True: 
            target = input("Please, Enter Project Target \n")
            if target.isdigit():
                break
            else:
                print("Invalid Target")

        while True:
            startdate = input("Please, Enter Project Start Date:\n")
            format = "%Y-%m-%d"
            try:
                datetime.datetime.strptime(str(startdate), format)
                break
            except ValueError:
                print("This is the incorrect date format ")
            
        while True:
            enddate = input("Please, Enter Project End Date:\n")
            format = "%Y-%m-%d"
            try:
                datetime.datetime.strptime(str(enddate), format)
                break
            except ValueError:
                print("This is the incorrect date format.")
            
    
        projectdata = ",".join([ title, details, target, startdate, enddate, email ])
        projectdata = projectdata + "\n"
        try:
            readfile = open("projects.txt")
        except:
            print("File not Exist")
        else:
           
            data = readfile.readlines()
            projects = []
            for i in data:
                projects.append(i.strip("\n"))
            for project in projects:
                projectsdetails = project.split(",")
                if projectsdetails[0] == id:
                    print("Project Already Exits")
                    readfile.close()
                    self.createproject(email)
            else:
                readfile.close()
                try:
                    file = open("projects.txt", "a")
                except:
                    print("File not Exit")
                else:
                    file.write(projectdata)
                    file.close()
                    print("Project Created Successfully")
                    mainMenu.projectmenu(email)


# ------------------------------------------------------------------------------------------ #
    def View(self,email):
        print("------------View Project----------------")
        try:
            readfile = open("projects.txt")
        except:
            print("File Not Exist")
        else:
            print("----------------Projects----------------") 
            data = readfile.readlines()
            projects = []
            for i in data:
                projects.append(i.strip("\n"))
            for project in projects:
                
                projectsdetails = project.split(",")
                
                if projectsdetails[5] == email:
                     
                    print(project)
            
            readfile.close()
            mainMenu.projectmenu(email)
           


# ------------------------------------------------------------------------------------------ #
    def Search(self,email):
        print("|------------Search Project----------------|")

        while True:      
            print(" Search By Date")
            try:
                    projectfile = open("projects.txt")
            except:
                    print("file not found")
            else:
                    data = projectfile.readlines()
                    projects = []
                    for item in data:
                        projects.append(item.strip("\n"))
                    project_start_date = input("enter start date \n")
                    project_end_date = input("enter end date \n")
                    for project in projects:
                        projectdetails = project.split(",")
                        if projectdetails[3] == project_start_date and projectdetails[4] == project_end_date:
                            if projectdetails[5] == email:
                                print(f"{project}")
                                projectfile.close()
                                break
                         
                    else:
                        print("## you entered wrong date of project search again ! ##")
                        self.Search(email)
            mainMenu.projectmenu(email)          
# ------------------------------------------------------------------- #
    def Delete(self,email):
        print("------------Delete Project----------------")
        while True:
            project_name = input("Please, Enter Project Name \n")
           
            if project_name.isalpha():
                break
            else:
                print("Invalid Title or Invalid Id")
        try:
            projectfile = open("projects.txt")
        except:
            print("file not found")
        else:
            data = projectfile.readlines()
            projects = []
            for item in data:
                projects.append(item.strip("\n"))
            for project in projects:
                projectdetails = project.split(",")
                if  projectdetails[5] == email:
                   # print(project)
                    projects.remove(project)
                    print("Project Has Been Deleted Successfully!")
                    projectfile.close()
                    file = open("projects.txt", "w")
                    for pro in projects:
                        file.write(pro + "\n")
                    file.close()
                    mainMenu.projectmenu(email)
            else:
               print("This Project Doesnt Exit")
               self.Delete(email)

crowd=crowdfunding()
class mainMenu:
    def main(self):
        print("------------------------------------------")
        print("---------------Crowd Funding--------------")
        while True:
            print("Please , Make Your Choice ")
            print("1- sign up")
            print("2- Log in")
            print("3- Exit")
            choice = int(input("so 1 or 2 or 3 \n"))
            if (choice == 1):
                 crowd.register()
                 break
            elif (choice == 2):
                crowd.login()
                break
            elif (choice == 3):
                exit()
            else:
                print("Wrong Data")

    def projectmenu(email):
        print("------------------------------------------")
        print("----------------Project Menu--------------")
        while True:
            print("Please , Make Your Choice ")
            print("1- Create Project")
            print("2- View Project")
            print("3- Search")
            print("4- Delete")
            choice = int(input("so 1 or 2 or 3 or 4 \n"))
            if (choice == 1):
                crowd.createproject(email)
                break
            elif (choice == 2):
                crowd.View(email)
                break
            elif (choice == 3):
                crowd.Search(email)
                break
            elif (choice == 4):
                crowd.Delete(email)
                break
           
            else:
                print("Wrong Data")
mainmenu = mainMenu()
mainmenu.main()

