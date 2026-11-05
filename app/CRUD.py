import psycopg
from datetime import date
from initDB import init, DB_INFO

DB_NAME = os.getenv("DB_NAME")

def getAllStudents(): #Retrieves and displays all records from the students table.
    with psycopg.connect(**DB_INFO, dbname=DB_NAME) as conn:
        rows = conn.execute("SELECT * FROM students").fetchall()
        print("Students: \n")

        print(f"{'student_id':>12}  {'first_name':20} {'last_name':20} {'email':40} {'enrollment_date':20}")
        print("-" * 72)
        for id, first, last, email, enrolled in rows:
            print(f"{id:>12}  {first:20} {last:20} {email:40} {enrolled!s:20}")

    return


def addStudent(first_name, last_name, email, enrollment_date): #Inserts a new student record into the students table.
    with psycopg.connect(**DB_INFO, dbname=DB_NAME) as conn:
        conn.execute("""
                    INSERT INTO students(first_name, last_name, email, enrollment_date)
                    VALUES (%s, %s, %s, %s)
                    """, 
                    (first_name, last_name, email, enrollment_date))
    
    return


def updateStudentEmail(student_id, new_email): #Updates the email address for a student with the specified student_id.
    with psycopg.connect(**DB_INFO, dbname=DB_NAME) as conn:
        result = conn.execute("""
                    UPDATE students
                    SET email = %s
                    WHERE student_id = %s
                    """, 
                    (email, student_id))
    
    return result.rowcount #number of rows deleted, if student doesnt exist, value will be zero


deleteStudent(student_id): #Deletes the record of the student with the specified student_id.
    with psycopg.connect(**DB_INFO, dbname=DB_NAME) as conn:
        result = conn.execute("""
                    DELETE FROM students
                    WHERE student_id = %s
                    """, 
                    (student_id))

        return result.rowcount 



def main():
    init()

    choice = -1
    while choice!=0:
        print("\n(1) CREATE\n (2) RETRIEVE\n (3) UPDATE\n (4) DELETE\n (0) EXIT\n ")
        

        try:
            choice = int(input("\nWhich CRUD operation do you want to execute: "))
        except ValueError:
            print("Please enter a number")
            continue

        match choice:
            case 0:
                print("Exiting program...")
            case 1:

                #getting user input
                first_name = input("First Name: ").strip()
                last_name = input("Last Name: ").strip()
                email = input("Email: ").strip()
                enrollment = input("Enrollment Date (YYYY-MM-DD): ").strip() 

                try:
                    enrollment_date = date.fromisoformat(enrollment)  # ensures date is in proper format

                except ValueError:
                    print("Invalid date, use YYYY-MM-DD")
                    continue

    
                try:
                    addStudent(first_name, last_name, email, enrollment_date)
                    print(f"Added {first_name} {last_name}")

                except psycopg.errors.UniqueViolation:
                    print(f"A student with email {email} already exists")

                except psycopg.Error as err:
                    print("Insert failed:", err)
            
            case 2:    
                try:
                    getAllStudents()

                except psycopg.Error:
                    print("Error retrieving students)

            case 3:
                #get user input
                try:
                    student_id = int(input("Student ID: "))
                except ValueError:
                    print("Student ID must be a number")
                    continue

                new_email = input("New Email: ").strip()

                try: 
                    if updateStudentEmail(student_id, new_email):
                        print(f"Changed student {student_id} email to {new_email}")

                    else:
                        print(f"No student with ID {student_id}")

                except psycopg.errors.UniqueViolation:
                    print(f"A student with email {email} already exists")

                except psycopg.Error as err:
                    print("Update failed:", err)

            case 4:
                # get user input
                try:
                    student_id = int(input("Student ID: "))
                except ValueError:
                    print("Student ID must be a number")
                    continue

                try:
                    if deleteStudent(student_id):
                        print(f"Student {student_id} deleted")
                    else:
                        print(f"No student with ID {student_id}")
                except psycopg.Error as err:
                    print("Delete failed:", err)


            case_:
                print("This option does not exist")


if __name__ == "__main__":
    main()