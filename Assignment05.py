# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Lora Berger,2024-11-13, Updated script to use JSON file
# ------------------------------------------------------------------------------------------ #
#import modules
import json
import io as _io

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds dict data for json format
file = _io.TextIOWrapper  # File handler
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e: #If file not found error comes up the below messaging will appear
    print(f"{FILE_NAME} file not found. Please ensure that file exists before running this script.\n")
    print("-- Technical Error Message --")
    print(e,e.__doc__, type(e), sep='\n') #gives detailed system error info
except Exception as e: #If any other error comes up the below messaging will appear
    print("There was a non-specific error.\n")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n') #gives detailed system error info
finally: #This is the make sure the file is closed even when there are errors
    if file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Student's first name should only contain letters, no numbers or symbols")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Student's last name should only contain letters, no numbers or symbols")

            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName":  course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e: #If value error occurs, display the following messages
            print(e) #displays message set above depending on where error occurred
            print("-- Technical Error Message --")
            print(e.__doc__)
        except Exception as e:
            print("There was a non-specific error.\n")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')  # gives detailed system error info
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file) #write the students json formated data to the file
            file.close()
            print(f"The following data was saved to the {FILE_NAME} file!")
            for student in students:
                print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        except TypeError as e: #If a type error occurs due to data set up incorrectly for the file type
            print(f"Please make sure that the data is in a valid JSON format before writing to {FILE_NAME} file.\n")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')  # gives detailed system error info
        except Exception as e:
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')  # gives detailed system error info
        finally: #This is the make sure the file is closed even when there are errors
            if file.closed == False:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
