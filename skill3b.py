import mysql.connector
class DBconnect:
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="password123",
                                         database="employee"
                                        )
        print("DB connected")

    def create_account(self,name,address,phonno,emailid):
        cur=self.con.cursor()
        sql="insert into account(acholdername ,address ,phno ,emailid,acbalence) values('{}','{}',{},'{}',{})".format(name,address,phonno,emailid,0)
        cur.execute(sql)
        self.con.commit()
        sql="select * from account where phno=%s"
        val=(phonno,)
        cur.execute(sql,val)
        row = cur.fetchone()
        res = row[0]
        return res
    def check_balance(self,acno):
        cur=self.con.cursor()
        sql = "select acbalence from account where acno=%s"
        val = (acno,)
        cur.execute(sql, val)
        row=cur.fetchone()
        res = row[0]
        return res
    def update_balance(self,acno,amount,type):
        cur = self.con.cursor()
        sql = "select acbalence from account where acno=%s"
        val = (acno,)
        cur.execute(sql, val)
        row = cur.fetchone()
        res = row[0]
        if(type=="D"):
            res=res+amount
            print("Your Amount Deposited successfully")
        else:
            if(res<amount):
                print("You dont have sufficient balance")
                return res
            else:
                res=res-amount
        sql = "update account set acbalence= %s where acno= %s"
        val = (res,acno,)
        cur.execute(sql, val)
        self.con.commit()
        return res
    def closeDB(self):
        self.con.close()
        print("DB connection Closed")