import mysql.connector
mydb=mysql.connector.connect(
    host="localhost", 
    user="root",
    password="Shwe@2309",
    database="onlineticketbooking_db"
)
mycursor=mydb.cursor()
def booking_tickets(movie_name,movie_time,total_amount):
  sql="insert into online_tickets(movie_name,move_time,total_amount) values (%s,%s,%s)"
  val=(movie_name,movie_time,total_amount)
  mycursor.execute(sql,val)
  mydb.commit()
  print("ticket booked sucessfully")
user=int(input("enter the number:"))
def view_data():
    mycursor.execute("select * from onlineticketbooking_db")
    result=mycursor.fetchall()
    for i in result:
        print(i)
def check_moviescreen():
    mycursor.execute("ALTER TABLE online_tickets ADD movie_screen varchar(255)")
    mydb.commit()
    print("column added successfully")
def display_moviename():
    movie_name="your movie name is displayed"
    mycursor.execute(movie_name)
    mydb.commit()

if user==1:
     movie_name=input("enter movie name:")
     mov_timimg=input("enter the movie timing:")
     total_amount=int(input("enter total amount:"))
     booking_tickets(movie_name,total_amount)
elif user==2:
    view_data()
elif user==3:
    check_moviescreen()
elif user==4:
    display_moviename()
else:print("you booking is cancelled")    
    
