import mysql.connector as sql
con = sql.connect(host='localhost', user='root', password='1234', database="quiz_game")
cur=con.cursor()
cur.execute("SELECT * FROM QUIZ")
rec=cur.fetchall()
print("\t\t\tWELCOME TO QUIZ GAME!!!!!!\n\n")
points=0
for i in range(len(rec)):
    ans=input(rec[i][1])
    if ans.upper()==rec[i][2]:
        print("CORRECT!!!")
        points+=1
    else:
        print("INCORRECT")
print("your total score is:", points)

