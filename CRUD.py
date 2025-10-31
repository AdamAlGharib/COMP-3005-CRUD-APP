from connect import get_conn

conn = get_conn()

def getAllStudents():
    sql= "select * from students"
    cur = conn.cursor()

    cur.execute(sql)

    rows = cur.fetchall()
    for row in rows:
        print(f"  ID: {row[0]}, Name: {row[1]} {row[2]}, Email: {row[3]}, Enrollment Date: {row[4]}")
    cur.close()

def addStudent(first_name, last_name, email, enrollment_date):
    sql="insert into students (first_name, last_name, email, enrollment_date) values (%s, %s, %s, %s)"

    cur = conn.cursor()

    cur.execute(sql,(first_name, last_name, email, enrollment_date))
    print(f"added student {first_name} {last_name}")
    conn.commit()
    cur.close()

def updateStudentEmail(student_id, new_email: str):
    sql = "update students set email = %s where student_id = %s"

    cur = conn.cursor()

    cur.execute(sql, (new_email, student_id))
    print(f"student with ID: {student_id}'s email has been updated to: {new_email} ")
    conn.commit()
    cur.close()


def deleteStudent(student_id):
    sql="delete from students where student_id = %s;"

    cur = conn.cursor()

    cur.execute(sql,(student_id, ))
    print(f"deleted student with ID {student_id}")
    conn.commit()
    cur.close()

