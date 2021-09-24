# from register_database import MyDb
# from tkinter import messagebox
# import sys
# from tkinter import *
# import mysql.connector
# class Info:
#     def __init__(self):
#         self.my_db = MyDb()
#         self.manche = []
#         self.name = []
#         self.address = []
#         self.phone = []
#         self.gender = []
#         self.otp_email_transfer = []
#
#     def binary_search_iterative(self,list, key):
#         start = 0
#         end = len(list) -1
#         while start <= end:
#             mid = (start+end) // 2
#             if list[mid][0] == key:
#                 messagebox.showerror("Error", "user name already exists! Try different one!")
#                 sys.exit()
#             elif list[mid][0] > key:
#                 end = mid -1
#             else:
#                 start = mid + 1
#         #return messagebox.showinfo("Successs","no such username exists so, congratulation you are logged in!!")
#
#     def find_user(self,name):
#         qry = "SELECT username from sign_up_info order by username"
#         self.data = self.my_db.show_data(qry)
#         self.binary_search_iterative(self.data,name)
#
#     def Register(self,name, phone, cmbo_box, address, password,username,email):
#         #qry = "CREATE DATABASE final_project"
#         #qry = "CREATE TABLE items (id int PRIMARY KEY AUTO_INCREMENT, name varchar(100), type varchar(100), price double)"
#         # qry = "INSERT INTO register_info (User Name) VALUES ('momo')"
#         # #for_security_reason
#         qry = "INSERT INTO sign_up_info (User, Phone, Gender, Address, Password, username,email) VALUES (%s,%s,%s,%s,%s,%s,%s)"
#         values = (name, phone, cmbo_box, address, password,username,email)
#         self.my_db.iud(qry,values)
#         return True
#
#
#
#
#
#
#
#
#
# # pos = -1
# # qry = "SELECT User from sign_up_info order by User"
# # list2 =[qry]
# # def binary_search_iterative(list2, n):
# #     l = 0
# #     u = len(list2)-1
# #     while l <=u:
# #         mid = (l+u) // 2
# #
# #         if list2[mid] == n:
# #             globals()['pos'] = mid
# #             return True
# #         else:
# #             if list2[mid] < n:
# #                 l = mid;
# #             else:
# #                 u = mid;
# #
# # num = input("Enter the number to search: ")
# # n = (num)
# # if binary_search_iterative(list2,n):
# #     print("Found at ",pos+1)
#
#     # def image():
#     #     manche = []
#
#
#
#     def Login(self,name,password):
#         connection = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
#         cur = connection.cursor()
#         query = "SELECT username,Password FROM sign_up_info"
#         self.Name = name
#         self.Psswd = password
#         cur.execute(query)
#         # def
#         # manche = []
#
#         for (user, pas) in cur:
#             if self.Name == user and self.Psswd == pas:
#                 self.login = True
#                 break
#             else:
#                 self.login = False
# #=======================(.split("@")[0])===============================================================================
#         self.username = (self.Name)
#
#         if self.login == True:
#
#             self.otp_email_transfer.clear()
#             # messagebox.showinfo("Welcome","Welcome to Kollywood Grocery Store, " + self.username)
#             connection = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
#             connection2 = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
#             cur2 = connection.cursor()
#             cur3 = connection2.cursor()
#             query2 = "SELECT username, Phone, Gender, Address, User, Password,email FROM sign_up_info WHERE username = " + str(
#                 self.Name)
#             query3 = "SELECT email FROM sign_up_info WHERE username = " + str(self.Name)
#             cur2.execute(query2)
#             cur3.execute(query3)
#             data = cur2.fetchall()
#             data2 = cur3.fetchall()
#             if self.login == True:
#                 # for email in data2:
#                 self.otp_email_transfer.clear()
#                 self.otp_email_transfer.append(data2)
#
#             # messagebox.showinfo("Welcome","Welcome to Kollywood Grocery Store, " + self.username)
#             # connection = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
#             # cur2 = connection.cursor()
#             # query2 = "SELECT username, Phone, Gender, Address, User, Password FROM sign_up_info WHERE username = " + str(self.Name)
#             # cur2.execute(query2)
#             # data = cur2.fetchall()
#             #
#
#             for std_id in data:
#                 # def photoimage1():
#                     self.manche.append(std_id)
#
#
#
#
#                 # photoimage1()
#             # for std_phone in data:
#             #     self.phone.append(std_phone)
#
#             # for std_gender in data:
#             #      self.gender.append(std_gender)
#
#             # for std_address in data:
#             #     self.address.append(std_address)
#
#             # for std_name in data:
#             #     self.name.append(std_name)
#             return True
#
#
#         elif self.login == False:
#             messagebox.showerror("Error","UserName or Password is Incorrect!!!!")
#             sys.exit()
#         cur.close()
#         connection.close()
#
#     def details_show(self,std_id):
#         connection = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
#         cur = connection.cursor()
#         self.student_id = std_id
#         connection = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
#         cur2 = connection.cursor()
#         query2 = "SELECT username, Phone, Gender, Address, User, Password FROM sign_up_info WHERE username = " + str(self.student_id)
#         cur2.execute(query2)
#         data = cur2.fetchall()
#         for std_phone in data:
#             self.phone.append(std_phone)
#
#         for std_gender in data:
#             self.gender.append(std_gender)
#
#         for std_address in data:
#             self.address.append(std_address)
#
#         for std_name in data:
#             self.name.append(std_name)
#         for std_id in data:
#             self.manche.append(std_id)
#         return True
#
#
#
#
# #===For_Admin_Connection===============================================================================================
#     def ADMIN(self, name, password):
#         connection = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
#         cur = connection.cursor()
#         query = "SELECT User,Password FROM Admin"
#         self.USER = name
#         self.PASSWD = password
#         cur.execute(query)
#
#         for (user, pas) in cur:
#             if self.USER == user and self.PASSWD == pas:
#                 self.login = True
#                 break
#
#             else:
#                 self.login = False
# #=======================(.split("@")[0])===============================================================================
#         self.username = (self.USER)
#
#         if self.login == True:
#             messagebox.showinfo("Welcome", "Welcome to Kollywood Grocery Store, " + self.username)
#             return True
#
#         elif self.login == False:
#             messagebox.showerror("Error", "UserName or Password is Incorrect!!!!")
#             sys.exit()
#         cur.close()
#         connection.close()
#
# # connection = mysql.connector.connect(host="localhost", user="root", password="root", database="project")
# # cur2 = connection.cursor()
# # query2 = "SELECT User FROM sign_up_info WHERE username = " + str("asdf")
# # cur2.execute(query2)
# # data = cur2.fetchall()
# # for row in data:
# #     print(row)
# # # for manche in cur2:
#
# # # print(query2)


from register_database import MyDb
from tkinter import messagebox
import sys
from tkinter import *
import mysql.connector


class Info:
    def __init__(self):
        self.my_db = MyDb()
        self.manche = []
        self.name = []
        self.address = []
        self.phone = []
        self.gender = []
        self.otp_email_transfer = []

    def binary_search_iterative(self, list, key):
        start = 0
        end = len(list) - 1
        while start <= end:
            mid = (start + end) // 2
            if list[mid][0] == key:
                messagebox.showerror("Error", "user name already exists! Try different one!")
                sys.exit()
            elif list[mid][0] > key:
                end = mid - 1
            else:
                start = mid + 1
        # return messagebox.showinfo("Successs","no such username exists so, congratulation you are logged in!!")

    def find_user(self, name):
        qry = "SELECT username from sign_up_info order by username"
        self.data = self.my_db.show_data(qry)
        self.binary_search_iterative(self.data, name)

    def Register(self, name, phone, cmbo_box, address, password, username, email):
        # qry = "CREATE DATABASE final_project"
        # qry = "CREATE TABLE items (id int PRIMARY KEY AUTO_INCREMENT, name varchar(100), type varchar(100), price double)"
        # qry = "INSERT INTO register_info (User Name) VALUES ('momo')"
        # #for_security_reason
        qry = "INSERT INTO sign_up_info (User, Phone, Gender, Address, Password, username,email) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = (name, phone, cmbo_box, address, password, username, email)
        self.my_db.iud(qry, values)
        return True

    def Login(self, name, password):
        connection = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
        cur = connection.cursor()
        query = "SELECT username,Password FROM sign_up_info"
        self.Name = name
        self.Psswd = password
        cur.execute(query)
        # def
        # manche = []

        for (user, pas) in cur:
            if self.Name == user and self.Psswd == pas:
                self.login = True
                break
            else:
                self.login = False
        # =======================(.split("@")[0])===============================================================================
        self.username = (self.Name)

        if self.login == True:
            self.otp_email_transfer.clear()
            # messagebox.showinfo("Welcome","Welcome to Kollywood Grocery Store, " + self.username)
            connection = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
            connection2 = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
            cur2 = connection.cursor()
            cur3 = connection2.cursor()
            query2 = "SELECT username, Phone, Gender, Address, User, Password,email FROM sign_up_info WHERE username = " + str(
                self.Name)
            query3 = "SELECT email FROM sign_up_info WHERE username = " + str(self.Name)
            cur2.execute(query2)
            cur3.execute(query3)
            data = cur2.fetchall()
            data2 = cur3.fetchall()
            if self.login == True:
                # for email in data2:
                self.otp_email_transfer.clear()
                self.otp_email_transfer.append(data2)
            for std_id in data:
                # def photoimage1():
                self.manche.append(std_id)

            return True


        elif self.login == False:
            messagebox.showerror("Error", "UserName or Password is Incorrect!!!!")
            sys.exit()
        cur.close()
        connection.close()

    def details_show(self, std_id):
        connection = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
        cur = connection.cursor()
        self.student_id = std_id
        connection = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
        cur2 = connection.cursor()
        query2 = "SELECT username, Phone, Gender, Address, User, Password FROM sign_up_info WHERE username = " + str(
            self.student_id)
        cur2.execute(query2)
        data = cur2.fetchall()
        for std_phone in data:
            self.phone.append(std_phone)

        for std_gender in data:
            self.gender.append(std_gender)

        for std_address in data:
            self.address.append(std_address)

        for std_name in data:
            self.name.append(std_name)
        for std_id in data:
            self.manche.append(std_id)
        return True

    # ===For_Admin_Connection===============================================================================================
    def ADMIN(self, name, password):
        connection = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
        cur = connection.cursor()
        query = "SELECT User,Password FROM Admin"
        self.USER = name
        self.PASSWD = password
        cur.execute(query)

        for (user, pas) in cur:
            if self.USER == user and self.PASSWD == pas:
                self.login = True
                break

            else:
                self.login = False
        # =======================(.split("@")[0])===============================================================================
        self.username = (self.USER)

        if self.login == True:
            messagebox.showinfo("Welcome", "Welcome to Kollywood Grocery Store, " + self.username)
            return True

        elif self.login == False:
            messagebox.showerror("Error", "UserName or Password is Incorrect!!!!")
            sys.exit()
        cur.close()
        connection.close()
