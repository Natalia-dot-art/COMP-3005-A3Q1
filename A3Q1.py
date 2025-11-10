import psycopg2

# Connect to an existing database
conn = psycopg2.connect(dbname="A3DB", user="postgres", password="postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Retrieves and displays all records from the students table.
def getAllStudents():

    cur.execute("SELECT * FROM students;")
    return print(cur.fetchall())

# Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date):

    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s,%s,%s,%s);", (first_name, last_name, email, enrollment_date))
    conn.commit()

# Updates the email address for a student with the specified student_id.
def updateStudentEmail(student_id, new_email):

    cur.execute("UPDATE students SET email=%s WHERE student_id=%s", (new_email, student_id))
    conn.commit()
    # Deletes the record of the student with the specified student_id
def deleteStudent(student_id):
    cur.execute("DELETE FROM students WHERE student_id=%s", student_id)
    conn.commit()

def main():

    while True:

        # main menu
        print("----------------------------")
        print("STUDENT DATABASE OPERATIONS")
        print()
        print("1) Get all students")
        print("2) Add a student")
        print("3) Update student email")
        print("4) Delete student")
        print("5) Exit")
        print()
        print("YOUR CHOICE:")
        choice = input()

        if choice == "1":
            getAllStudents()

        if choice == "2":
            print("provide a first name, last name, email, and enrollment date YYYY-MM-DD separately")
            answer = []

            answer.append(str(input()))
            answer.append(str(input()))
            answer.append(str(input()))
            answer.append(str(input()))
            addStudent(answer[0], answer[1], answer[2], answer[3])

            print(answer[0] + " " + "student added!")

        if choice == "3":
            print("provide the student ID:")
            student_id = int(input())

            print("provide the new email:")
            n_email = str(input())
            updateStudentEmail(student_id, n_email)
            print("updated student email successfully!")

        if choice == "4":
            print("provide the student ID:")
            input_id = input()
            deleteStudent(input_id)
            print("deleted student successfully!")

        if choice == "5":
            # Make the changes to the database persistent
            conn.commit()
            # Close communication with the database
            cur.close()
            conn.close()
            print("goodbye!")
            break
        if int(choice) > 5 or int(choice) < 1:
            print("invalid choice. Try again.")

# run main
if __name__ == "__main__":
    main()

