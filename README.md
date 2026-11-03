# COMP 3005 Assignment 3, Q1: 
Dadwynn Francois
101337345

## Overview
A command-line Python application that connects to a PostgreSQL database and performs CRUD operations on a `students` table.

## Video Link
You can access the demo video [here]()

## File Structure 
```
.
├── .env.example        # example of what database connection settings should look like
├── README.md
├── sql/
│   └── DDL_DML.sql     # creates the students table and inserts the initial data
└── app/
    └── initDB.py       # store helper function init() that initializes database
    └── CRUD.py         # database setup using initDB.py, CRUD function implementation and the menu loop for CLI

```

## Usage Flow

### 1. Prerequisites
- Python
- PostgreSQL 13 or newer, running locally
- A PostgreSQL user with permission to create databases
  
### 2. Install dependencies
```
pip install "psycopg[binary]"
```
 
### 3. Configure the connection
Create a `.env` file in the project root mirroring `.env.example` 

### 4. Run the application
```bash
python app/CRUD.py
```
On startup the `studentdb` database is dropped (if it exists), recreated and populated from `sql/DDL_DML.sql`. 
 
### 5. Use the menu
Follow the menu prompts to execute CRUD operations 

 
