# ATM-machine-management-system


import mysql.connector
mydb=mysql.connector.connect(
    host="localhost", 
    user="root",
    password="Shwe@2309",
    database="atmcard_db"
)
mycursor=mydb.cursor()
def insert_card(acc_holder,acc_type,pin_no):
  sql="insert into atm_machine(acc_holder,acc_type,pin_no) values (%s,%s,%s)"
  val=(acc_holder,acc_type,pin_no)
  mycursor.execute(sql,val)
  mydb.commit()
  print("data inserted sucessfully")
user=int(input("enter the number:"))
def view_data():
    mycursor.execute("select * from atm_machine")
    result=mycursor.fetchall()
    for i in result:
        print(i)
def check_balance():
    mycursor.execute("ALTER TABLE atm_machine ADD balance varchar(255)")
    mydb.commit()
    print("column added successfully")
def display_balance():
    balance_statement="your balance is displayed"
    mycursor.execute(balance_statement)
    mydb.commit()

    if user==1:
     acc_holder=input("enter account holder name:")
     acc_type=input("enter the account type:")
     pin_no=int(input("enter your pin number:"))
     insert_card(acc_holder,acc_type,pin_no)
    elif user==2:
        view_data()
    elif user==3:
        check_balance()
    elif user==4:
        display_balance()
    else:print("you transaction is cancelled")    
