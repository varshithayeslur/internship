import time
import random as rn
import dbcontext as db
from models import Internship
from models import Student
from beautifultable import BeautifulTable

def _get_new_id():
    t_obj = time.localtime()
    new_id = rn.randint(1000,9900) + (t_obj.tm_min + t_obj.tm_hour + t_obj.tm_sec)
    return new_id

def add_internship(iname,company,i_year):
    id = _get_new_id()
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("insert into internship(id,iname,company,i_year,status) values(?,?,?,?,?)",(id,iname,company,i_year,1))
            print(f"Internship is added successfully with id:{id}")
    except Exception as e:
        print(str(e))

def view_all_internships():
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select id,iname,company,i_year,status from internship")
            rows = cursor.fetchall()
            intern_pro_lst = [Internship(*row) for row in rows]
            _view_internship_list(intern_pro_lst)
    except Exception as e:
        print(str(e))

def search_internship_by_name(name):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, iname, company, i_year, status FROM internship WHERE iname=?",(name,))
            rows = cursor.fetchall()
            if(rows):
                intern_pro_lst = [Internship(*row) for row in rows]
                _view_internship_list(intern_pro_lst)
            else:
                print(f"No internship found with name : {name} ")
    except Exception as e:
        print(str(e))


def change_status_internship(name):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT status from internship where iname=?",(name,))
            prev_status = cursor.fetchone()
            new_status=0
            if prev_status[0] == 0:
                new_status = 1
            elif prev_status[0] == 1:
                new_status = 0
            cursor.execute("UPDATE internship SET status=? WHERE iname=?",(new_status, name,))
    except Exception as e:
        print(str(e))

    
def delete_internship(id):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM internship where id=? ",(id,))
    except Exception as e:
        print(str(e))

def add_student(usn, name, sem, placed):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO student(usn, name, sem, placed) VALUES(?,?,?,?)",(usn, name, sem, placed))
    except Exception as e:
        print(str(e))

def view_all_students():
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT usn, name, sem, placed FROM student")
            rows = cursor.fetchall()
            student_list = [Student(*row) for row in rows]
            paint_student_list(student_list)
    except Exception as e:
        print(str(e))


def search_student_by_name(name):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT usn, name, sem, placed FROM student WHERE name like '%'?'%' ",(name,))
            rows = cursor.fetchall()
            if rows:
                student_list = [Student(*row) for row in rows]
                paint_student_list(student_list)
            else:
                print(f"No student exists with name : {name}")
    except Exception as e:
        print(str(e))

def update_student(usn,sem):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE student set sem=? WHERE usn=?",(sem, usn,))
    except Exception as e:
        print(str(e))   

def delete_student(usn):
    try:
        with db.DbContext() as Connection:
            cursor = Connection.cursor()
            cursor.execute("DELETE FROM student WHERE usn=?",(usn,))
    except Exception as e:
        print(str(e))

         
def reg_stu_internship(usn, iid, status):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO registration(iid, usn, status) VALUES(?,?,?)",(iid,usn, status))
    except Exception as e:
        print(str(e))


def update_stu_intership_status(usn, iid, status):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE registration set status=? WHERE usn=? and iid=?",(status,usn,iid))
    except Exception as e:
        print(str(e))


def company_ws_count():
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT company, count(*) from internship group by company ")
            rows = cursor.fetchall()
            table = BeautifulTable()
            table.column_headers = ["COMPANY", "COUNT"]
            for row in rows:
                table.append_row(row)
            print(table)
    except Exception as e:
        print(str(e))


def student_ws_count():
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT name, r.usn, count(*) from registration r JOIN student s on r.usn=s.usn group by r.usn ")
            rows = cursor.fetchall()
            table = BeautifulTable()
            table.column_headers = ["NAME", "USN", "COUNT"]
            for row in rows:
                table.append_row(row)
            print(table)
    except Exception as e:
        print(str(e))

def ws_student_reports():
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select r.usn, s.name, i.iname, i.company, i.i_year from registration r JOIN student s on (s.usn = r.usn) JOIN internship i on (i.id = r.iid) ")
            rows = cursor.fetchall()
            if(rows):
                paint_internship_report(rows)
            else:
                print("No students registered yet...\n")
    except Exception as e :
        print(str(e))


def _view_internship_list(lst):
    if lst and len(lst) > 0:
        table = BeautifulTable()
        table.column_headers = ["ID", "NAME", "COMPANAY", "YEAR","STATUS"]
        for l in lst:
            status = "Completed" if l.status == 0 else "Going on" 
            table.append_row([l.id, l.iname, l.company, l.i_year,status])
        print(table)
    else:
        print(f"There are no Intership programms, yet to add...")

def paint_student_list(lst):
    if lst and len(lst) > 0:
        table = BeautifulTable()
        table.column_headers = ["USN", "NAME", "SEM", "STATUS"]
        for l in lst:
            status = "Placed" if l.placed == 1 else "Not Placed"
            table.append_row([l.usn, l.name, l.sem, status])
        print(table)
    else:
        print("Student table is empty...")

def paint_internship_report(rows):
    table = BeautifulTable()
    table.column_headers = ["USN", "NAME", "INTERNSHIP_TITLE","COMPANY", "YEAR" ]
    for row in rows:
        table.append_row(row)
    print(table)
