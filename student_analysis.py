#Variable Declaration
# I used snake_case for variable names as required 
student_name = "Olanipekun Iyanuoluwa"  # String 
matric_number = "22/10AQ090"    # String 
age = 19                        # Integer 
cgpa = 3.85                     # Float 
is_active = True                # Boolean 
courses_registered = ["AFS 301", "AFS 303", "AFS 305"] # List 
grades = {"AFS 301": "A", "AFS 303": "A", "AFS 305": "B"} # Dictionary 

#Data Structures in Action 

# 1. List of student names 
student_names = [
    "Olanipekun Iyanuoluwa", "Bello Musa", "Chukwuma Ada", "Abubakar Idris", "Fatima Yusuf"
]

#List of dictionaries for student profiles 
students = [
    {
        "name": "Olanipekun Iyanuoluwa",
        "matric": "22/10AQ090",
        "age": 19,
        "cgpa": 3.85,
        "is_active": True,
        "courses": ["AFS 301", "AFS 303", "AFS 305"],
        "grades": {"AFS 301": "A", "AFS 303": "A", "AFS 305": "B"}
    },
    {
        "name": "Bello Musa",
        "matric": "22/10AQ091",
        "age": 21,
        "cgpa": 4.20,
        "is_active": True,
        "courses": ["AFS 307", "AFS 309", "AHE 301"],
        "grades": {"AFS 307": "B", "AFS 309": "A", "AHE 301": "C"}
    },
    {
        "name": "Chukwuma Ada",
        "matric": "22/10AQ092",
        "age": 20,
        "cgpa": 2.40,
        "is_active": True,
        "courses": ["AHE 311", "AHE 309", "AFS 301"],
        "grades": {"AHE 311": "C", "AHE 309": "D", "AFS 301": "B"}
    },
    {
        "name": "Abubakar Idris",
        "matric": "22/10AQ093",
        "age": 22,
        "cgpa": 4.75,
        "is_active": False,
        "courses": ["AFS 303", "AFS 305", "AHE 311"],
        "grades": {"AFS 303": "A", "AFS 305": "A", "AHE 311": "A"}
    },
    {
        "name": "Fatima Yusuf",
        "matric": "22/10AQ094",
        "age": 23,
        "cgpa": 3.10,
        "is_active": True,
        "courses": ["AFS 309", "AHE 301", "AHE 309"],
        "grades": {"AFS 309": "B", "AHE 301": "B", "AHE 309": "C"}
    }
]

#A set storing the unique courses offered in the department
department_courses = {
    "AFS 301", "AFS 303", "AFS 305", "AFS 307", "AFS 309", 
    "AHE 301", "AHE 311", "AHE 309"
}

#A tuple for fixed department information 
dept_info = ("Food Science Department", "Faculty of Agriculture", 2025)


#Conditional Statements for Grading
def calculate_grade(score):
    # Determine the grade based on the score
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"
    
    # Using MATCH CASE to print feedback 
    match grade:
        case "A":
            print("Feedback: Excellent! You are a top Student.")
        case "B":
            print("Feedback: Very Good! Keep maintaining this standard, you can do more.")
        case "C":
            print("Feedback: Good effort, but you can do better.")
        case "D" | "E":
            print("Feedback: Pass. You need to work harder.")
        case "F":
            print("Feedback: Fail. Please see your level adviser or the faculty counsellor.")
            
    return grade


#Type Conversion and Validation
def get_validated_input():
    try:
        # Ask user for input 
        age_input = input("Enter student age: ")
        cgpa_input = input("Enter student CGPA: ")
        
        # Convert strings to int and float (Requirement 34)
        age = int(age_input)
        cgpa = float(cgpa_input)
        
        # Validate ranges (Requirement 35)
        # Age must be 16-40, CGPA must be 0.0-5.0
        if 16 <= age <= 40 and 0.0 <= cgpa <= 5.0:
            print(f"Validated: Age {age}, CGPA {cgpa}")
            return age, cgpa
        else:
            print("Validation Error: Age must be 16-40 and CGPA 0.0-5.0.")
            return None

    except ValueError:
        # Handle invalid input 
        print("Error: Invalid input! Please enter numeric values for age and CGPA.")
        return None
    
  
  #List Operations and Slicing
# A list of 10 assignment scores
assignment_scores = [85, 92, 78, 90, 88, 76, 95, 89, 82, 91]

#Extracting the top 3 scores using slicing 
top_3 = assignment_scores[:3] 

#Extracting the last 5 scores using negative indexing
last_five = assignment_scores[-5:]

#Extracting every other score using step slicing 
# The ::2 tells Python to start at the beginning and jump by 2
every_other = assignment_scores[::2]

#Slicing operations worked


#Set Operations 

#Defining the sets based on my student records
# These are students who passed AFS 301 
set_pass = {"Olanipekun Iyanuoluwa", "Bello Musa", "Fatima Yusuf"}

#These are students with CGPA above 4.0 
set_merit = {"Bello Musa", "Abubakar Idris"}

#Find students who passed AND have merit (Intersection)
# This finds names that appear in BOTH sets 
pass_and_merit = set_pass.intersection(set_merit)

#Find all distinct students in both sets 
# This combines both sets but removes duplicates 
all_distinct_students = set_pass.union(set_merit)

#Find students who passed but do NOT have merit 
# This removes merit students from the pass list 
pass_no_merit = set_pass.difference(set_merit)

#Checking for Eligibility 
def check_graduation_eligibility(student):
    # A student is eligible if:
    # 1. CGPA is 2.5 or above 
    # 2. No outstanding courses 
    # 3. Is_active is True 
    
    # Logic: Checking if they have at least 3 courses as a 'mock' requirement
    has_cgpa = student["cgpa"] >= 2.5
    is_active = student["is_active"]
    no_outstanding = len(student["courses"]) >= 3 
    
    #Using logical operator 'and' 
    if has_cgpa and is_active and no_outstanding:
        return True, f"Success: {student['name']} meets all requirements for graduation."
    else:
        return False, f"Notice: {student['name']} is not yet eligible for graduation."

#The Menu Loop
def run_system():
    while True:
        print("\n============================================")
        print("   Student Academic Performance System")
        print("============================================")
        print("1. View all students")
        print("2. Add new student")
        print("3. Check eligibility for graduation")
        print("4. Find top performer")
        print("5. Run Advanced Analysis") #Im doing d optional task
        print("6. Exit")
        print("--------------------------------------------")
        
        choice = input("Enter your choice: ")
        
        #Using MATCH CASE as required
        match choice:
            case "1":
                print("\nList of Students:")
                for i, s in enumerate(students, 1):
                    print(f"{i}. {s['name']} (Matric: {s['matric']})")
            
            case "2":
                print("\nAdd New Student")
                #Using our validation function
                name = input("Enter name: ")
                matric = input("Enter matric number: ")
                input_data = get_validated_input() #Calling function from Part 2
                
                if input_data:
                    age, cgpa = input_data
                    status = input("Is the student active (yes/no): ").lower()
                    active_bool = status == "yes"
                    courses = input("Enter courses (comma separated): ").split(",")
                    
                    #Storing a new profile
                    new_student = {
                        "name": name,
                        "matric": matric,
                        "age": age,
                        "cgpa": cgpa,
                        "is_active": active_bool,
                        "courses": [c.strip() for c in courses],
                        "grades": {}
                    }
                    students.append(new_student)
                    print("Student record added successfully.")
            
            case "3":
                search_name = input("Enter student name: ")
                found = False
                for s in students:
                    if s["name"].lower() == search_name.lower():
                        status, message = check_graduation_eligibility(s)
                        print(message)
                        found = True
                        break
                if not found:
                    print("Student not found.")
            
            case "4":
                #Finding the highest CGPA in the list
                top_student = max(students, key=lambda x: x['cgpa'])
                print(f"\nTop Performer: {top_student['name']}")
                print(f"CGPA: {top_student['cgpa']}")
            
            case "5":
                # This calls the two advanced functions for d optional q 5
                advanced_analysis() 
                print("\n--- Type Detection Demo ---")
                # Detecting data types....
                print(check_type_summary(students)) 
                print(check_type_summary(4.5))
                print("Exiting the system... Goodbye!")
                break
            case "6":
                print("Exiting the system... Goodbye!")
                break
                
            
            case _:
                print("Invalid choice! Please select 1-5.")


#Nested Data Processing 
def advanced_analysis():
    print("\n--- Advanced Average Score Analysis ---")
    # Using a nested dictionary as required
    nested_data = {
        "Olanipekun Iyanuoluwa": {"AFS 301": 85, "AFS 303": 90, "AFS 305": 78},
        "Bello Musa": {"AFS 307": 65, "AFS 309": 88, "AHE 301": 72},
        "Abubakar Idris": {"AFS 303": 95, "AFS 305": 92, "AHE 311": 89}
    }
    
    for name, courses in nested_data.items():
        scores = courses.values()
        average = sum(scores) / len(scores)
        print(f"{name}: Average = {average:.2f}")
        
        # Check if all scores are above 70
        if all(s > 70 for s in scores):
            print(f"  -> Excellence Award: {name} scored above 70 in all courses!")

#Pattern Matching
def check_type_summary(data):
    match data:
        case int():
            return f"Summary: This is an Integer with value {data}"
        case float():
            return f"Summary: This is a Float with value {data}"
        case list():
            return f"Summary: This is a List containing {len(data)} items"
        case dict():
            return f"Summary: This is a Dictionary with {len(data)} keys"
        case str():
            return f"Summary: This is a String: '{data}'"


# This line actually is to triggers the menu to start
if __name__ == "__main__":
    run_system()