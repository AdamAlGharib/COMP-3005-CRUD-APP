# Database Interaction with PostgreSQL and Python

## Objective

This project demonstrates basic **CRUD (Create, Read, Update, Delete)** operations on a PostgreSQL database using Python and the `psycopg2` library.


## Database Setup

1. Create a PostgreSQL database named **`assignment2`**.  
2. Run the provided **`schema.sql`** file to create and populate the `students` table:

```sql
CREATE TABLE students (
    student_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
```


## Python files

connect.py 
    Handles the PostgreSQL database connection.

CRUD.py
    Contains all CRUD operations for interacting with the students table.

main.py 
    Contains an interactive application that invoke the crud functions


## HOW TO RUN


- Make sure PostgreSQL server is running.

- Update connection settings in connect.py if needed.

- Run your schema scripts to create and populate the dataset:

- python main.py


## Demo Video

link: https://youtu.be/6zuiEmEF1ZY