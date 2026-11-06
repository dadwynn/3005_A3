# COMP 3005 Assignment 3, Q1: 
Dadwynn Francois
101337345

## Overview
A command-line Python application that connects to a PostgreSQL database and performs CRUD operations on a `students` table.

## Video Link
You can access the demo video [here](https://www.loom.com/share/a555a30cf947433195c180345d9429ab)

## File Structure 
```
.
├── .env.example        # example of what database connection settings should look like
├── README.md
├── sql/
│   └── DDL_DML.sql     # creates the students table and inserts the initial data
└── app/
    ├── initDB.py       # contains helper function: init() that initializes database
    └── CRUD.py         # contains database setup using initDB.py, CRUD function implementations and the menu loop for CLI
```

## Usage Flow

### 1. Prerequisites
- Python
- PostgreSQL running locally
- A PostgreSQL user with permission to create databases
  
### 2. Install dependencies
Python database driver and library that loads environment variables from a `.env` file into python
```
pip install "psycopg[binary]" python-dotenv
```
 
### 3. Configure the connection
Create a `.env` file in the project root mirroring `.env.example` 

### 4. Run the application

Navigate to the project root and run the following command:
```bash
python app/CRUD.py
```
*Note: On startup, the `studentdb` database is dropped (if it exists) so make sure to close any other connections to studentdb before running, or the drop will fail. Afterwards, database is recreated and populated from `sql/DDL_DML.sql`.*
 
### 5. Use the menu
Follow the menu prompts to execute CRUD operations 
   - **(1) CREATE**     <-- `addStudent(first_name, last_name, email, enrollment_date)`: Inserts a new student record into the students table.
   - **(2) RETRIEVE** <-- `getAllStudents()`: Retrieves and displays all records from the students table.  
   - **(3) UPDATE**   <-- `updateStudentEmail(student_id, new_email)`: Updates the email address for a student with the specified student_id.
   - **(4) DELETE**    <-- `deleteStudent(student_id)`: Deletes the record of the student with the specified student_id.
   - **(0) EXIT**         <-- quit the program
 
