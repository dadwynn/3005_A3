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
    └── initDB.py       # contains helper function: init() that initializes database
    └── CRUD.py         # contains database setup using initDB.py, CRUD function implementations and the menu loop for CLI

```

## Usage Flow

### 1. Prerequisites
- Python
- PostgreSQL 13 or newer, running locally
- A PostgreSQL user with permission to create databases
  
### 2. Install dependencies
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
On startup the `studentdb` database is dropped (if it exists) so make sure you are connected when this happens. Database is then recreated and populated from `sql/DDL_DML.sql`. 
 
### 5. Use the menu
Follow the menu prompts to execute CRUD operations 

 
