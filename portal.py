import os
import quiz

def register():
    print("Create a new student account.")
    username = input("Enter username: ")
    
    if os.path.exists('students.txt'):
        f = open('students.txt', 'r')
        for line in f:
            if line.split(',')[1].strip() == username: 
                print("Username is already taken. Please try another.")
                f.close()
                return
        f.close()
    
    full_name = input("Enter Full name ")
    password = input("Create a password ")
    college = input("Enter College/Institute/University ")
    enrollment_no = input("Enter Enrollment number ")
    course = input("Which course are you in? ")
    email = input("Enter E-mail address ")
    phone = input("Enter Phone number ")
    dob = input("Enter Date-Of-Birth (DD-MM-YYYY)? ")
    gender = input("Gender: ")
    guardian_name = input("Guardian's name ")
    
    f = open('students.txt', 'a') 
    f.write(f"{full_name.strip()},{username.strip()},{password.strip()},{college.strip()},{enrollment_no.strip()},{course.strip()},{email.strip()},{phone.strip()},{dob.strip()},{gender.strip()},{guardian_name.strip()}\n")
    f.close()
    print("Successfully Registered.")

def login():
    print("Log In ")
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "admin123":
        print("Admin Login Successful. Welcome!")
        return "ADMIN", "admin"

    if not os.path.exists('students.txt'):
        print("No one has registered yet.")
        return None,None
    
    f = open('students.txt', 'r')
    for line in f:
        data = line.strip().split(',')
        if data[1] == username and data[2] == password:
            print(f"Login Successful. Welcome, {data[0]}!")
            f.close()
            return "USER", username
    f.close()
    
    print("Incorrect Username or password. Please try again.")
    return None,None

def show_profile(logged_user):
    if not logged_user:
        print("Not logged in.")
        return None

    print(f"Your Profile ({logged_user})")
    
    if not os.path.exists('students.txt'):
        print("Data not found.")
        return None

    f = open('students.txt', 'r')
    user_found = False
    for line in f:
        data = line.strip().split(',')
        if data[1] == logged_user:
            print(f"  Full Name:       {data[0]}")
            print(f"  Username:        {data[1]}")
            print(f"  Enrollment No:   {data[4]}")
            print(f"  Course:          {data[5]}")
            print(f"  Email:           {data[6]}")
            print(f"  Phone:           {data[7]}")
            print(f"  Date of Birth:   {data[8]}")
            print(f"  Gender:          {data[9]}")
            print(f"  Guardian's Name: {data[10]}")
            user_found = True
            f.close()
            return data[4]
    
    f.close()
    if not user_found:
        print("Could not find profile data.")
    return None

def update_profile(logged_user):
    if not logged_user:
        print("Log in ")
        return

    print("Update Your Profile")
    print("Current details:")
    show_profile(logged_user) 
    
    fields_to_update = {
        '1': ("Full Name", 0),
        '2': ("Password", 2),
        '3': ("Course", 5),
        '4': ("Email", 6),
        '5': ("Phone", 7),
        '6': ("Date of Birth", 8),
        '7': ("Guardian's Name", 10)
    }
    print("Fields to update:")
    for key, value in fields_to_update.items():
        print(f" {key}. {value[0]}")
    choice = input("Choose an option: ")
    
    if choice not in fields_to_update:
        print("Invalid selection.")
        return
        
    field_name, field_index = fields_to_update[choice]
    new_value = input(f"Enter the new value for {field_name}: ")
    
    if not os.path.exists('students.txt'):
        print("Data not found.")
        return

    f_read = open('students.txt', 'r')
    lines = f_read.readlines()
    f_read.close()
    
    f_write = open('students.txt', 'w') 
    for line in lines:
        data = line.strip().split(',')
        if data[1] == logged_user:
            data[field_index] = new_value.strip()
            updated_line = ",".join(data)
            f_write.write(updated_line + "\n")
        else:
            f_write.write(line)
    f_write.close()
    print("Profile updated successfully!")

def terminate():
    print("Program has been terminated!")
    exit()

def main():
    
    logged_in_user = None
    user_type = None

    while True:
        
        if user_type == "USER":
            print(f" Student Portal (Logged in as {logged_in_user})")
            print("1. Attempt Quiz")
            print("2. View My Profile")
            print("3. Update My Profile")
            print("4. Log Out")
            response = input("Please choose an option: ")
            
            if response == '1':
                user_enrollment = show_profile(logged_in_user)
                if user_enrollment:
                    input("Press Enter to confirm details and start quiz")
                    quiz.run_quiz(user_enrollment)
                else:
                    print("Could not get enrollment number.")
            elif response == '2':
                show_profile(logged_in_user)
            elif response == '3':
                update_profile(logged_in_user)
            elif response == '4':
                print("Logged out.")
                logged_in_user = None
                user_type = None
            else:
                print("Invalid response. Choose a number from 1 to 4.")

        elif user_type == "ADMIN":
            print("Admin Dashboard")
            print("1. View All Quiz Scores (Current Session)")
            print("2. Log Out")
            response = input("Please choose an option: ")
            
            if response == '1':
                quiz.view_all_scores()
            elif response == '2':
                print("Logged out.")
                logged_in_user = None
                user_type = None
            else:
                print("Invalid response. Choose 1 or 2.")

        else:
            print("Welcome to the Student Portal")
            print("1. Create an Account (Register)")
            print("2. Log In (User or Admin)")
            print("3. Exit")
            response = input("Please choose an option: ")

            if response == '1':
                register()
            elif response == '2':
                user_type, logged_in_user = login() 
            elif response == '3':
                terminate()
            else:
                print("Invalid response. Choose a number from 1 to 3.")

if __name__ == "__main__":
    main()