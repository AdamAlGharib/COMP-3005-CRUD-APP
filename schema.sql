create table students (
    student_id int generated always as identity primary key,
    first_name text not Null,
    last_name text not Null,
    email text not null unique,
    enrollment_date date
);

insert into students (first_name, last_name, email, enrollment_date) values
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');