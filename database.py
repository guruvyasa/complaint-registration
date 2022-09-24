import sqlite3
def createTables():
    try:
        conn=sqlite3.connect("data.db")
        query='''create table user(
                id  integer primary key,
                name varchar(50) not null,
                password varchar(50) not null,
                role int(1) not null default 0,
                phone varchar(10) not null unique)'''
        conn.execute(query)
        conn.commit()
        query=''' create table department(
                    id integer primary key,
                    name varchar(50) not null)'''
        conn.execute(query)
        conn.commit()
        query=''' create table complaint(
                    id integer primary key,
                    user_id integer not null,
                    dept_id integer not null,
                    description text not null,
                    complaint_date varchar(10) not null,
                    foreign key(user_id) references user(id) on delete cascade,
                    foreign key(dept_id) references department(id) on delete cascade)'''
        conn.execute(query)
        conn.commit()
        print("Tables executed")
    except Exception as e:
        print("connnection is not successfull")
        print(e)

def addUser(name,phone,password,role=0):
    try:
        conn=sqlite3.connect("data.db")
        query='''insert into user(name,phone,password,role) values (?,?,?,?)'''
        conn.execute(query,(name,phone,password,role))
        conn.commit()
        return "Table User Added"
    except Exception as e:
        print(e)
        return "Table User not added"


def addDept(id,name):
    try:
        conn=sqlite3.connect("data.db")
        query='''insert into department(id,name)values(?,?)'''
        conn.execute(query,(id,name))
        conn.commit()
        print("Table Department Added")
    except Exception as e:
        print(e)

def addComplaint(id,user_id,dept_id,description,complaint_date):
    try:
        conn=sqlite3.connect("data.db")
        query='''insert into complaint(id,user_id,dept_id,description,complaint_date)values(?,?,?,?,?)'''
        conn.execute(query,(id,user_id,dept_id,description,complaint_date))
        conn.commit()
        return  "Table Complaint Added"
    except Exception as e:
        print(e)
        return "failure"

def getUser(phone, password):
    try:
        conn=sqlite3.connect("data.db")
        query=''' select * from user where phone=? and password=?'''
        user=conn.execute(query,(phone,password))
        return user.fetchall()
    except Exception as e:
        print(e)
        return []



def getUsers():
    try:
        conn=sqlite3.connect("data.db")
        query=''' select * from user'''
        users=conn.execute(query)
        return users.fetchall()
    except Exception as e:
        print(e)

def getDept():
    try:
        conn=sqlite3.connect("data.db")
        query=''' select * from department'''
        users=conn.execute(query)
        return users.fetchall()
    except Exception as e:
        print(e)

def getComplaint():
    try:
        conn=sqlite3.connect("data.db")
        query=''' select complaint.id,user.name,department.name,description,complaint_date from complaint inner join department on complaint.dept_id = department.id inner join user on user.id = complaint.user_id'''
        users=conn.execute(query)
        return users.fetchall()
    except Exception as e:
        print(e)
        return []


if __name__=='__main__':
        createTables()
        addUser('sahana','6362811346','1234','user')
        addUser('aishwarya','9742157032','1111','user')
        addUser('priyanka','9731433266','12121212','user')
        addUser('sushma','8888899999','222222','admin')
        addDept(101,'Department of Power')
        addDept(102,'Department of Road transport and Highways')
        addDept(103,'Department of Water Resources')
        addDept(104,'Department of Financial Services')
        addDept(105,'Department of Railways')
        addComplaint(501,1,101,'HESCOM is not providing proper power facilities near akshay park.Power is removed frequently in a day',"12/2/2021")
        addComplaint(502,1,105,'Trains are not following alloted timings.Its too difficult to manage when most of the trains are stopped in the outer before reaching Hubballi station','29/4/2022')
        addComplaint(503,2,102,'Its has been more than a year,but the roads near ravinagar are underconstruction.Progress is too slow','13/5/2021')
        addComplaint(504,2,104,'Loan sanction in SBI bank is very slow.It has been 3 months but the loan is not sanctioned','31/3/2022')
        addComplaint(505,3,103,'Its been 10 days and the water near shirur park road is not being provided at the allocated days','25/6/2022')
        addComplaint(506,3,104,'Pan card and aadhar has been provided during the opening of savings account yet BOI asks to submit Pan frequently','2/5/2022')
        addComplaint(507,1,104,'Most of the atms of Canara bank in hubballi are out of order','22/4/2022')
        addComplaint(508,2,102,'Progress of flyover work near Hosur is very slow and there is disturbance to the transportation of public','18/07/2022')
        addComplaint(509,3,103,'Drinking water near shirur park is provided for just 1 hr which is insufficient of the public','16/08/2022')
        addComplaint(510,4,101,'Street lights at Lingaraj nagar near banashankari temple lane are not working','23/2/2022')
        print(getUsers())
        print(getDept())
        print(getComplaint())




    

