from register_database import MyDb
from tkinter import messagebox
import sys
from tkinter import *
import mysql.connector
import datetime


class Attend:
    def __init__(self):
        self.my_db = MyDb()

        self.datesss = []
        self.already = []

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

    def FindDate(self, std_id):
        connection = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
        cur2 = connection.cursor()
        qry = "SELECT DATE from attendence WHERE ID = " + str(std_id)
        cur2.execute(qry)
        data = cur2.fetchall()
        self.e = datetime.datetime.now()
        self.datenow = "%s/%s/%s" % (self.e.day, self.e.month, self.e.year)
        self.datenow2 = "%s/%s/%s" % (self.e.day, self.e.month, self.e.year)
        if self.datenow in str(data):
            print("Hello")

        if self.datenow not in str(data):
            self.already.append("7")
        elif self.datenow in str(data):
            self.datesss.append(self.datenow)

        if std_id == 10002457:
            self.already.clear()

    def Attendence(self, date, time, id):
        qry = "INSERT INTO attendence (DATE, TIME, ID) VALUES (%s,%s,%s)"
        values = (date, time, id)
        self.my_db.iud(qry, values)
        return True

    def show_total_attendence(self, std_id):
        qry = "SELECT * FROM attendence where ID = " + str(std_id)
        all_items = self.show_data(qry)
        return all_items

    def show_data(self, qry):
        self.my_connection = mysql.connector.connect(user="root", password="Mysql1234!@#$", host="localhost", database='project')
        self.my_cursor = self.my_connection.cursor()
        self.my_cursor.execute(qry)
        data = self.my_cursor.fetchall()
        return data

# # from register_database import MyDb
# # from tkinter import messagebox
# # import sys
# # from tkinter import *
# # import mysql.connector
# # import datetime
# # class Attend:
# #     def __init__(self):
# #         self.my_db = MyDb()
# #
# #         self.datesss = []
# #         self.already = []
# #
# #     def binary_search_iterative(self,list, key):
# #         start = 0
# #         end = len(list) -1
# #         while start <= end:
# #             mid = (start+end) // 2
# #             if list[mid][0] == key:
# #                 messagebox.showerror("Error", "user name already exists! Try different one!")
# #                 sys.exit()
# #             elif list[mid][0] > key:
# #                 end = mid -1
# #             else:
# #                 start = mid + 1
# #         #return messagebox.showinfo("Successs","no such username exists so, congratulation you are logged in!!")
# #
# #     def FindDate(self,std_id,DATE):
# #         connection = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
# #         cur2 = connection.cursor()
# #         qry = "SELECT DATE from attendence WHERE ID = " + str(std_id)
# #         cur2.execute(qry)
# #         data = cur2.fetchall()
# #         self.e = datetime.datetime.now()
# #         self.datenow = "%s/%s/%s" % (self.e.day, self.e.month, self.e.year)
# #         # self.time = "%s:%s:%s" % (self.e.hour, self.e.minute, self.e.second)
# #         for self.datenow in data:
# #            self.datesss.append(self.datenow)
# #            print(self.datesss[0])
# #         if self.datenow not in data:
# #             self.already.append(7)
# #         if std_id == 10002457:
# #             self.already.clear()
# #             # exit
# #         # for self.datenow not in data:
# #         #     self.datesss
# #         # #    exit(0)
# #
# #     def Attendence(self,date, time, id):
# #         qry = "INSERT INTO attendence (DATE, TIME, ID) VALUES (%s,%s,%s)"
# #         values = (date,time,id)
# #         self.my_db.iud(qry,values)
# #         return True
#
#
# from register_database import MyDb
# from tkinter import messagebox
# import sys
# from tkinter import *
# import mysql.connector
# import datetime
#
#
# class Attend:
#     def __init__(self):
#         self.my_db = MyDb()
#
#         self.datesss = []
#         self.already = []
#
#     def binary_search_iterative(self, list, key):
#         start = 0
#         end = len(list) - 1
#         while start <= end:
#             mid = (start + end) // 2
#             if list[mid][0] == key:
#                 messagebox.showerror("Error", "user name already exists! Try different one!")
#                 sys.exit()
#             elif list[mid][0] > key:
#                 end = mid - 1
#             else:
#                 start = mid + 1
#         # return messagebox.showinfo("Successs","no such username exists so, congratulation you are logged in!!")
#
#     def FindDate(self, std_id, DATE):
#         connection = mysql.connector.connect(host="localhost", user="root", password="Mysql1234!@#$", database="project")
#         cur2 = connection.cursor()
#         qry = "SELECT DATE from attendence WHERE ID = " + str(std_id)
#         cur2.execute(qry)
#         data = cur2.fetchall()
#         self.e = datetime.datetime.now()
#         self.datenow = "%s/%s/%s" % (self.e.day, self.e.month, self.e.year)
#         self.datenow2 = "%s/%s/%s" % (self.e.day, self.e.month, self.e.year)
#         # self.time = "%s:%s:%s" % (self.e.hour, self.e.minute, self.e.second)
#         # if self.datenow not in data:
#         #     # print(self.datenow)
#         #     print("Nothing!!!!!")
#         #     print(data)
#         #     self.datesss.append(self.datenow)
#         #     print(self.datesss)
#         #     # pass
#         # else:
#         #     print("CHA")
#         for self.datenow in data:
#             self.datesss.append(self.datenow2)
#             print(self.datesss[0])
#             print(self.datesss)
#
#         if self.datenow not in data:
#             self.already.append(7)
#             print(self.already)
#         if std_id == 10002457:
#             self.already.clear()
#             # exit
#         # for self.datenow not in data:
#         #     self.datesss
#         # #    exit(0)
#
#     def Attendence(self, date, time, id):
#         qry = "INSERT INTO attendence (DATE, TIME, ID) VALUES (%s,%s,%s)"
#         values = (date, time, id)
#         self.my_db.iud(qry, values)
#         return True
#
#     def show_total_attendence(self, std_id):
#         qry = "SELECT * FROM attendence where ID = " + str(std_id)
#         all_items = self.show_data(qry)
#         print(all_items)
#         return all_items
#
#
#     def show_data(self, qry):
#         self.my_connection = mysql.connector.connect(user="root", password="Mysql1234!@#$", host="localhost", database='project')
#         self.my_cursor = self.my_connection.cursor()
#         self.my_cursor.execute(qry)
#         data = self.my_cursor.fetchall()
#         print(data)
#         return data
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
# # def image():
# #     manche = []
#
#
# #     def Login(self,name,password):
# #         connection = mysql.connector.connect(host="localhost", user="root", password="root", database="project")
# #         cur = connection.cursor()
# #         query = "SELECT username,Password FROM sign_up_info"
# #         self.Name = name
# #         self.Psswd = password
# #         cur.execute(query)
# #         # def
# #         # manche = []
#
# #         for (user, pas) in cur:
# #             if self.Name == user and self.Psswd == pas:
# #                 self.login = True
# #                 break
# #             else:
# #                 self.login = False
# # #=======================(.split("@")[0])===============================================================================
# #         self.username = (self.Name)
#
# #         if self.login == True:
# #             # messagebox.showinfo("Welcome","Welcome to Kollywood Grocery Store, " + self.username)
# #             connection = mysql.connector.connect(host="localhost", user="root", password="root", database="project")
# #             cur2 = connection.cursor()
# #             query2 = "SELECT username, Phone, Gender, Address, User, Password FROM sign_up_info WHERE username = " + str(self.Name)
# #             cur2.execute(query2)
# #             data = cur2.fetchall()
# #             for std_id in data:
# #                 # def photoimage1():
# #                     self.manche.append(std_id)
#
#
# #                 # photoimage1()
# #             # for std_phone in data:
# #             #     self.phone.append(std_phone)
#
# #             # for std_gender in data:
# #             #      self.gender.append(std_gender)
#
# #             # for std_address in data:
# #             #     self.address.append(std_address)
#
# #             # for std_name in data:
# #             #     self.name.append(std_name)
# #             return True
#
#
# #         elif self.login == False:
# #             messagebox.showerror("Error","UserName or Password is Incorrect!!!!")
# #             sys.exit()
# #         cur.close()
# #         connection.close()
#
# #     def details_show(self,std_id):
# #         connection = mysql.connector.connect(host="localhost", user="root", password="root", database="project")
# #         cur = connection.cursor()
# #         self.student_id = std_id
# #         connection = mysql.connector.connect(host="localhost", user="root", password="root", database="project")
# #         cur2 = connection.cursor()
# #         query2 = "SELECT username, Phone, Gender, Address, User, Password FROM sign_up_info WHERE username = " + str(self.student_id)
# #         cur2.execute(query2)
# #         data = cur2.fetchall()
# #         for std_phone in data:
# #             self.phone.append(std_phone)
#
# #         for std_gender in data:
# #             self.gender.append(std_gender)
#
# #         for std_address in data:
# #             self.address.append(std_address)
#
# #         for std_name in data:
# #             self.name.append(std_name)
# #         for std_id in data:
# #             self.manche.append(std_id)
# #         return True
#
#
# # #===For_Admin_Connection===============================================================================================
# #     def ADMIN(self, name, password):
# #         connection = mysql.connector.connect(host="localhost", user="root", password="root", database="project")
# #         cur = connection.cursor()
# #         query = "SELECT User,Password FROM Admin"
# #         self.USER = name
# #         self.PASSWD = password
# #         cur.execute(query)
#
# #         for (user, pas) in cur:
# #             if self.USER == user and self.PASSWD == pas:
# #                 self.login = True
# #                 break
#
# #             else:
# #                 self.login = False
# # #=======================(.split("@")[0])===============================================================================
# #         self.username = (self.USER)
#
# #         if self.login == True:
# #             messagebox.showinfo("Welcome", "Welcome to Kollywood Grocery Store, " + self.username)
# #             return True
#
# #         elif self.login == False:
# #             messagebox.showerror("Error", "UserName or Password is Incorrect!!!!")
# #             sys.exit()
# #         cur.close()
# #         connection.close()
#
# # # connection = mysql.connector.connect(host="localhost", user="root", password="root", database="project")
# # # cur2 = connection.cursor()
# # # query2 = "SELECT User FROM sign_up_info WHERE username = " + str("asdf")
# # # cur2.execute(query2)
# # # data = cur2.fetchall()
# # # for row in data:
# # #     print(row)
# # # # for manche in cur2:
#
# # # # print(query2)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
# #     def Login(self,name,password):
# #         connection = mysql.connector.connect(host="localhost", user="root", password="root", database="project")
# #         cur = connection.cursor()
# #         query = "SELECT username,Password FROM sign_up_info"
# #         self.Name = name
# #         self.Psswd = password
# #         cur.execute(query)
# #         # def
# #         # manche = []
#
# #         for (user, pas) in cur:
# #             if self.Name == user and self.Psswd == pas:
# #                 self.login = True
# #                 break
# #             else:
# #                 self.login = False
# # #=======================(.split("@")[0])===============================================================================
# #         self.username = (self.Name)
#
# #         if self.login == True:
# #             # messagebox.showinfo("Welcome","Welcome to Kollywood Grocery Store, " + self.username)
# #             connection = mysql.connector.connect(host="localhost", user="root", password="root", database="project")
# #             cur2 = connection.cursor()
# #             query2 = "SELECT username, Phone, Gender, Address, User, Password FROM sign_up_info WHERE username = " + str(self.Name)
# #             cur2.execute(query2)
# #             data = cur2.fetchall()
# #             for std_id in data:
# #                 # def photoimage1():
# #                     self.manche.append(std_id)
#
#
#
#
# #                 # photoimage1()
# #             # for std_phone in data:
# #             #     self.phone.append(std_phone)
#
# #             # for std_gender in data:
# #             #      self.gender.append(std_gender)
#
# #             # for std_address in data:
# #             #     self.address.append(std_address)
#
# #             # for std_name in data:
# #             #     self.name.append(std_name)
# #             return True
#
#
# #         elif self.login == False:
# #             messagebox.showerror("Error","UserName or Password is Incorrect!!!!")
# #             sys.exit()
# #         cur.close()
# #         connection.close()
#
# #     def details_show(self,std_id):
# #         connection = mysql.connector.connect(host="localhost", user="root", password="root", database="project")
# #         cur = connection.cursor()
# #         self.student_id = std_id
# #         connection = mysql.connector.connect(host="localhost", user="root", password="root", database="project")
# #         cur2 = connection.cursor()
# #         query2 = "SELECT username, Phone, Gender, Address, User, Password FROM sign_up_info WHERE username = " + str(self.student_id)
# #         cur2.execute(query2)
# #         data = cur2.fetchall()
# #         for std_phone in data:
# #             self.phone.append(std_phone)
#
# #         for std_gender in data:
# #             self.gender.append(std_gender)
#
# #         for std_address in data:
# #             self.address.append(std_address)
#
# #         for std_name in data:
# #             self.name.append(std_name)
# #         for std_id in data:
# #             self.manche.append(std_id)
# #         return True
#
#
#
#
# # #===For_Admin_Connection===============================================================================================
# #     def ADMIN(self, name, password):
# #         connection = mysql.connector.connect(host="localhost", user="root", password="root", database="project")
# #         cur = connection.cursor()
# #         query = "SELECT User,Password FROM Admin"
# #         self.USER = name
# #         self.PASSWD = password
# #         cur.execute(query)
#
# #         for (user, pas) in cur:
# #             if self.USER == user and self.PASSWD == pas:
# #                 self.login = True
# #                 break
#
# #             else:
# #                 self.login = False
# # #=======================(.split("@")[0])===============================================================================
# #         self.username = (self.USER)
#
# #         if self.login == True:
# #             messagebox.showinfo("Welcome", "Welcome to Kollywood Grocery Store, " + self.username)
# #             return True
#
# #         elif self.login == False:
# #             messagebox.showerror("Error", "UserName or Password is Incorrect!!!!")
# #             sys.exit()
# #         cur.close()
# #         connection.close()
#
# # # connection = mysql.connector.connect(host="localhost", user="root", password="root", database="project")
# # # cur2 = connection.cursor()
# # # query2 = "SELECT User FROM sign_up_info WHERE username = " + str("asdf")
# # # cur2.execute(query2)
# # # data = cur2.fetchall()
# # # for row in data:
# # #     print(row)
# # # # for manche in cur2:
#
# # # # print(query2)