# from logging import info
# from tkinter.font import names
#
# from tkinter import *
# from tkinter import ttk
#
# from register_info import Info
# import os
# import cv2
#
#
# import sys
# import tkinter
#
# from PIL import Image,ImageTk
# import datetime
# from tkinter import messagebox
#
# import smtplib
# import random
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# import time
# import sys
# timeexcep = int(300)
# t = datetime.datetime.now()
# p = t.strftime("%X")
# onlyminute = t.minute
# name = "Softwarica College"
#
#
#
# class Sign:
#
#
#     def __init__(self,new_window):
#         self.closecam = []
#         self.noface = []
#         self.student_id = "random"
#
#         self.otp = random.randint(1000, 9999)
#         self.subj = "Email from Softwarica College [" + p + "]"
#         self.message_body = "Hello User!!!\n" + name + "\nTo authenticate, please use the following One Time password(OTP)\n" + str(
#             self.otp) + "\nIf you require any assistance, please contact" \
#                         " our 24 hr Customer Service"
#
#         #===Sign_In_Window====================================================================================================:
# #=======To_Close_Previous_Window======================================================================================
#         #self.window.withdraw()
#         self.new_window=new_window
#         self.new_window.title("Sign_in")
#         self.new_window.geometry('900x750+0+0')
#         self.new_window.resizable("false","false")
#
#
#         def time():
#             now = datetime.datetime.now()
#             self.date = (now.strftime("%I:%M:%S:%p"))
#             self.daa = (now.strftime("%H:%M:%S '/n' %d-%m-%y"))
#             self.clock_label = Label(self.new_window, font=('times new roman', 12), fg='black', bg="White", text=self.date)
#             self.clock_label.place(x=700, y=100)
#             self.clock_label.after(200, time)
#         time()
# #=======Importing_Class_Of_Register_Info=============================================================================
#         self.info=Info()
#         # self.suc = Success
#
#         # campicname = self.info.
#         # a = self.info.babu
#         # print(a)
# #=======For_Reset=====================================================================================================
#         self.user_reset = StringVar()
#         self.password_reset = StringVar()
#
# #=======Adding_Background_Image=======================================================================================
#         self.bg = ImageTk.PhotoImage(file="D:\\downloads\\project\\Images\\sign_in.jpg")
#         bg = Label(self.new_window, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
#
#         self.user_name_entry = Entry(self.new_window,font=("times new roman",15), highlightbackground="black",highlightthickness="1",textvariable=self.user_reset)
#         self.user_name_entry.place(x=380,y=490)
#
#         self.user_password_entry = Entry(self.new_window, font=("times new roman", 15), show='*',fg="red",highlightbackground='black',highlightthickness="1",textvariable=self.password_reset)
#         self.user_password_entry.place(x=380, y=575)
#
#         self.login_button = Button(self.new_window,cursor="hand2",text="L   o   g   i   n",borderwidth=0,bg="White",font=("times new roman",15,"bold"),command=self.Login)
#         self.login_button.place(x=560,y=630)
#
#         self.lb1 = Label(self.new_window,text="D o n ' t  h a v e   a c c o u n t ?",font=("times new roman",9),bg="White")
#         self.lb1.place(x=640,y=680)
#
#         self.sign_up = Button(self.new_window,cursor="hand2",text="S i g n  U p",borderwidth=0,bg="White",fg="Red",font=("times new roman",10,"bold"),command=self.sign_up)
#         self.sign_up.place(x=700,y=700)
#
#         def enter(e):
#             self.image2 = PhotoImage(file = "D:\\downloads\\project\\Images\\state2.png")
#             self.shy_label["image"] = self.image2
#             self.shy_label.image = self.image2
#         def enterpas(e):
#             self.image2 = PhotoImage(file="D:\\downloads\\project\\Images\\state3.png")
#             self.shy_label["image"] = self.image2
#             self.shy_label.image = self.image2
#         def leave(e):
#             self.image1 = PhotoImage(file="D:\\downloads\\project\\Images\\state1.png")
#             self.shy_label["image"] = self.image1
#             self.shy_label.image = self.image1
#
#         self.im = PhotoImage(file="D:\\downloads\\project\\Images\\state1.png")
#         self.shy_label = Label(self.new_window,image=self.im,bg="green",font=("times new roman",15,"bold"))
#         self.shy_label.image = self.im
#         self.shy_label.place(x=290,y=165,width=310,height=320)
#
#         self.user_name_entry.bind("<Enter>",enter)
#         self.user_name_entry.bind("<Leave>",leave)
#
#         self.user_password_entry.bind("<Enter>",enterpas)
#         self.user_password_entry.bind("<Leave>",leave)
#
#
#         self.reset_button = Button(self.new_window,cursor="hand2",text="R  e  s  e  t", bg="White",borderwidth=0, font=("times new roman", 15, "bold"),command=self.reset_signIn)
#         self.reset_button.place(x=280, y=630)
#
#         self.combo_box_usertypes = ttk.Combobox(self.new_window,font=("times new roman", 15),state="readonly",justify=CENTER)
#         self.combo_box_usertypes.place(x=350,y=130,width=210,height=30)
#         self.combo_box_usertypes["values"] = ("Select","Admin","Employment")
#
#
#         self.new_window.grab_set()
#
# #=======get()=========================================================================================================
#         self.user = self.user_name_entry.get()
#         self.pas = self.user_password_entry.get()
#
#     def Login(self):
#         if self.user_name_entry.get() == "" or self.user_password_entry.get() == "":
#             messagebox.showerror("Error","Please fill all the entries")
#             return TRUE
#         else:
#             if self.combo_box_usertypes.get() == "Employment":
#                 self.new_window.withdraw()
#                 self.nn = self.user_name_entry.get()
#                 password = self.user_password_entry.get()
#                 self.info.Login(self.nn,password)
#                 self.student_id = self.user_name_entry.get()
#
#                 file = open('users.txt','w')
#                 file.write(self.user_name_entry.get())
#                 file.close()
#
#                 # print(self.student_id)
#                 self.user_name_entry.delete(0,END)
#                 self.user_password_entry.delete(0,END)
#                 self.namdekhanamdekha = self.info.manche
#                 self.namdekha2 = str(self.namdekhanamdekha)
#                 self.create_otp_window()
#                 # print(self.namdekha2)
# #===========To_Open_Grocery_Management_System==========================================================================
#     def grocery(self):
#         print(self.info.otp_email_transfer)
#         print(self.info.otp_email_transfer[0][0][0])
#         # print(self.info.otp_email_transfer.split('')
#         self.new_window.withdraw()
#         from LoginSuccess import Success
#         self.success = Toplevel(self.new_window)
#         Success(self.success)
#                 # def grocery(self):
#                 #     self.new_window.withdraw()
#                 #     from LoginSuccess import Success
#                 #     self.success = Toplevel(self.new_window)
#                 #     Success(self.success)
#
#                     # LoginSuccessWindow = Toplevel(self.new_window)
#                     # messagebox.showinfo("Success","Welcome to ......................")
#                     # Success(LoginSuccessWindow)
#
#
#
#                 # return False
#
#
#                 # def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
#                 #     gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#                 #     features = classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)
#                 #     for (x,y,w,h) in features:
#                 #         cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
#                 #         id, pred = clf.predict(gray_img[y:y+h,x:x+w])
#                 #         confidence = int(100*(1-pred/300))
#                 #         if confidence>75 and id == int(name):
#                 #             cv2.putText(img,self.namdekha2, (x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1,cv2.LINE_AA)
#                 #             # cv2.waitKey(5000)
#                 #             # if cv2.waitKey(1) == 13:
#                 #             messagebox.showinfo("Verified","User verified")
#                 #             video_capture.release()
#                 #             cv2.destroyAllWindows()
#                 #             self.closecam.append(7)
#                 #             grocery()
#                 #
#                 #         else:
#                 #             cv2.putText(img,"Unknown", (x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1,cv2.LINE_AA)
#                 #             messagebox.showerror("Error","Unknown Faces")
#                 #             self.noface.append(4)
#                 #             sys.exit()
#                 #
#                 #     video_capture.release()
#                 #     cv2.destroyAllWindows()
#                 #     return img
#                 # faceCascade = cv2.CascadeClassifier("D:\\downloads\\project\\CascadeFile\\haarcascade_frontalface_default.xml")
#                 # clf = cv2.face.LBPHFaceRecognizer_create()
#                 # clf.read(name + ".xml")
#                 # # clf.read("9955.xml")
#                 # video_capture = cv2.VideoCapture(0)
#                 #
#                 # while True:
#                 #     ret, img = video_capture.read()
#                 #     img = draw_boundary(img,faceCascade, 1.3,6,(255,255,255),clf)
#                 #     cv2.imshow("Face Detection",img)
#                 #     if 7 in self.closecam:
#                 #         video_capture.release()
#                 #         cv2.destroyAllWindows()
#                 #         break
#                 #     if 7 not in self.closecam and 4 not in self.noface:
#                 #         video_capture.release()
#                 #         cv2.destroyAllWindows()
#                 #         messagebox.showerror("Error","No one's is in camera!")
#                 #         break
#                 #     if cv2.waitKey(1) == 13:
#                 #         break
#                 # video_capture.release()
#                 # cv2.destroyAllWindows()
#                 #
#                 #
#                 #
#
#     def reset_signIn(self):
#         self.user_reset.set('')
#         self.password_reset.set('')
#         self.combo_box_usertypes.set('')
#     def sign_up(self):
#         self.new_window.withdraw()
#         from SignUps import SignUp
#         self.sign = Toplevel(self.new_window)
#         SignUp(self.sign)
#
#     def create_otp_window(self):
#         # app = tkinter.Tk()
#         self.otp_wind = tkinter.Toplevel()
#         self.otp_wind.title("OTP")
#         # self.otp_wind.geometry('900x750+0+0')
#         self.otp_wind.resizable("false", "false")
#         self.otp_wind.grab_set()
#
#         self.OTP_MESSAGE()
#
#         self.label1 = Label(self.otp_wind, text="Enter the OTP send to the registered\nEmail!",
#                             font=("times new roman", 10))
#         self.label1.place(x=0, y=2)
#
#         self.otpent = Entry(self.otp_wind, font=("times new roman", 10), bg="White", highlightbackground='black',
#                             highlightthickness="1")
#         self.otpent.place(x=60, y=70, width=80)
#
#         self.bttn_verify = Button(self.otp_wind, text="V  e  r  i  f  y", cursor="hand2", fg="Red", borderwidth=0,
#                                   font=("times new roman", 14), command=self.cmd_verify)
#         self.bttn_verify.place(x=45, y=120)
#
#     def cmd_verify(self):
#         if self.otpent.get() == "":
#             messagebox.showerror("Excuse Me!", "Please fill the 4 digit OTP!")
#         elif len(self.otpent.get()) != 4:
#             messagebox.showerror("Failed", "OTP must be equal to 4 digit!!!! ")
#         elif str(self.otpent.get()) == str(self.otp):
#             # self.email_value = True
#             self.otpent.delete(0, END)
#             messagebox.showinfo("Verified!", "OTP Verified")
#             # self.email_value = True
#             self.otp_wind.destroy()
#
#             def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
#                 gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#                 features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
#                 for (x, y, w, h) in features:
#                     cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
#                     id, pred = clf.predict(gray_img[y:y + h, x:x + w])
#                     confidence = int(100 * (1 - pred / 300))
#                     if confidence > 75 and id == int(self.nn):
#                         cv2.putText(img, self.namdekha2, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1,
#                                     cv2.LINE_AA)
#                         # cv2.waitKey(5000)
#                         # if cv2.waitKey(1) == 13:
#                         messagebox.showinfo("Verified", "User verified")
#                         video_capture.release()
#                         cv2.destroyAllWindows()
#                         self.closecam.append(4)
#                         self.grocery()
#
#
#             # def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
#             #     gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             #     features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
#             #     for (x, y, w, h) in features:
#             #         cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
#             #         id, pred = clf.predict(gray_img[y:y + h, x:x + w])Dar
#             #         confidence = int(100 * (1 - pred / 300))
#             #         if confidence > 75 and id == int(self.name_id):
#             #             cv2.putText(img, self.namdekha2, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1,
#             #                         cv2.LINE_AA)
#             #             # cv2.waitKey(5000)
#             #             # if cv2.waitKey(1) == 13:
#             #             messagebox.showinfo("Verified", "User verified")
#             #             video_capture.release()
#             #             cv2.destroyAllWindows()
#             #
#             #             self.closecam.append(7)
#             #             self.grocery()
#                         # grocery()
#
#                     else:
#                         cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
#                         messagebox.showerror("Error", "Unknown Faces")
#                         self.noface.append(4)
#                         sys.exit()
#
#                 video_capture.release()
#                 cv2.destroyAllWindows()
#                 return img
#
#             faceCascade = cv2.CascadeClassifier(
#                 "D:\\downloads\\project\\CascadeFile\\haarcascade_frontalface_default.xml")
#             clf = cv2.face.LBPHFaceRecognizer_create()
#             # clf.read(name + ".xml")
#             clf.read("190113.xml")
#             video_capture = cv2.VideoCapture(0)
#
#             while True:
#                 ret, img = video_capture.read()
#                 img = draw_boundary(img, faceCascade, 1.3, 6, (255, 255, 255), clf)
#                 cv2.imshow("Face Detection", img)
#                 if 7 in self.closecam:
#                     video_capture.release()
#                     cv2.destroyAllWindows()
#                     break
#                 if 7 not in self.closecam and 4 not in self.noface:
#                     video_capture.release()
#                     cv2.destroyAllWindows()
#                     messagebox.showerror("Error", "No one's is in camera!")
#                     break
#                 if cv2.waitKey(1) == 13:
#                     break
#             video_capture.release()
#             cv2.destroyAllWindows()
#
#
#
#         elif str(self.otpent.get()) != str(self.otp):
#             # self.email_value = False
#             self.otpent.delete(0, END)
#             messagebox.showerror("Verify OTP!!!", "OTP Failed to Verify!!")
#             # print("Not verified!")
#
#     def OTP_MESSAGE(self):
#         self.fromaddr = "checkotp04@gmail.com"
#         self.password = "generationxpass"
#         self.toaddr = self.info.otp_email_transfer[0][0][0]
#         p = t.strftime("%X")
#         msg = MIMEMultipart()
#         msg['From'] = self.fromaddr
#         msg['To'] = self.toaddr
#         msg['Subject'] = self.subj
#         self.body = self.message_body
#         msg.attach(MIMEText(self.body, 'plain'))
#         self.filename = "test.jpg"
#         attachment = open(self.filename, "rb")
#         p = MIMEBase('application', 'octet-stream')
#         p.set_payload((attachment).read())
#         encoders.encode_base64(p)
#         p.add_header('Content-Disposition', "attachment; filename= %s" % self.filename)
#         msg.attach(p)
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(self.fromaddr, self.password)
#         text = msg.as_string()
#         server.send_message(msg)
#         server.quit()
#
#
# def main():
#     window = Tk()
#     obj = Sign(window)
#     window.mainloop()
# if __name__ == '__main__':
#     main()


from logging import info
import tkinter
from tkinter.font import names
# from LoginSuccess import Success
from tkinter import *
from tkinter import ttk
from register_info import Info
import os
import cv2
from PIL import Image
import numpy as np
import sys
import hashlib
from Crypto.Cipher import Salsa20
import cryptocode

# from interface.foods import fod
# from interface.Grocery import Grocery_System
# from interface.Admin import Admin_Systems
from PIL import Image, ImageTk
import datetime
from tkinter import messagebox

import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import sys

timeexcep = int(300)
t = datetime.datetime.now()
p = t.strftime("%X")
onlyminute = t.minute
name = "Softwarica College"


class Sign:

    def __init__(self, new_window):
        self.closecam = []
        self.noface = []
        self.student_id = "random"
        self.passget = []
        self.name_id = ""

        # self.email_value = ""

        self.otp = random.randint(1000, 9999)
        self.subj = "Email from Softwarica College [" + p + "]"
        self.message_body = "Hello User!!!\n" + name + "\nTo authenticate, please use the following One Time password(OTP)\n" + str(
            self.otp) + "\nIf you require any assistance, please contact" \
                        " our 24 hr Customer Service"

        # ===Sign_In_Window====================================================================================================:
        # =======To_Close_Previous_Window======================================================================================
        # self.window.withdraw()
        self.new_window = new_window
        self.new_window.title("Sign_in")
        self.new_window.geometry('900x750+0+0')
        self.new_window.resizable("false", "false")

        def time():
            now = datetime.datetime.now()
            self.date = (now.strftime("%I:%M:%S:%p"))
            self.daa = (now.strftime("%H:%M:%S '/n' %d-%m-%y"))
            self.clock_label = Label(self.new_window, font=('times new roman', 12), fg='black', bg="White",
                                     text=self.date)
            self.clock_label.place(x=700, y=100)
            self.clock_label.after(200, time)

        time()
        # =======Importing_Class_Of_Register_Info=============================================================================
        self.info = Info()
        # self.suc = Success

        # campicname = self.info.
        # a = self.info.babu
        # print(a)
        # =======For_Reset=====================================================================================================
        self.user_reset = StringVar()
        self.password_reset = StringVar()

        # =======Adding_Background_Image=======================================================================================
        self.bg = ImageTk.PhotoImage(file="D:\\downloads\\project\\Images\\sign_in.jpg")
        bg = Label(self.new_window, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.user_name_entry = Entry(self.new_window, font=("times new roman", 15), highlightbackground="black",
                                     highlightthickness="1", textvariable=self.user_reset)
        self.user_name_entry.place(x=380, y=490)

        self.user_password_entry = Entry(self.new_window, font=("times new roman", 15), show='*', fg="red",
                                         highlightbackground='black', highlightthickness="1",
                                         textvariable=self.password_reset)
        self.user_password_entry.place(x=380, y=575)

        self.login_button = Button(self.new_window, cursor="hand2", text="L   o   g   i   n", borderwidth=0, bg="White",
                                   font=("times new roman", 15, "bold"), command=self.Login)
        self.login_button.place(x=560, y=630)

        # self.windowexample = Button(self.new_window,cursor="hand2",text="window",borderwidth=0,bg="White",font=("times new roman",15,"bold"),command=self.create_otp_window)
        # self.windowexample.place(x=700,y=630)

        self.lb1 = Label(self.new_window, text="D o n ' t  h a v e   a c c o u n t ?", font=("times new roman", 9),
                         bg="White")
        self.lb1.place(x=640, y=680)

        self.sign_up = Button(self.new_window, cursor="hand2", text="S i g n  U p", borderwidth=0, bg="White", fg="Red",
                              font=("times new roman", 10, "bold"), command=self.sign_up)
        self.sign_up.place(x=700, y=700)

        def enter(e):
            self.image2 = PhotoImage(file="D:\\downloads\\project\\Images\\state2.png")
            self.shy_label["image"] = self.image2
            self.shy_label.image = self.image2

        def enterpas(e):
            self.image2 = PhotoImage(file="D:\\downloads\\project\\Images\\state3.png")
            self.shy_label["image"] = self.image2
            self.shy_label.image = self.image2

        def leave(e):
            self.image1 = PhotoImage(file="D:\\downloads\\project\\Images\\state1.png")
            self.shy_label["image"] = self.image1
            self.shy_label.image = self.image1

        self.im = PhotoImage(file="D:\\downloads\\project\\Images\\state1.png")
        self.shy_label = Label(self.new_window, image=self.im, bg="green", font=("times new roman", 15, "bold"))
        self.shy_label.image = self.im
        self.shy_label.place(x=290, y=165, width=310, height=320)

        self.user_name_entry.bind("<Enter>", enter)
        self.user_name_entry.bind("<Leave>", leave)

        self.user_password_entry.bind("<Enter>", enterpas)
        self.user_password_entry.bind("<Leave>", leave)

        self.reset_button = Button(self.new_window, cursor="hand2", text="R  e  s  e  t", bg="White", borderwidth=0,
                                   font=("times new roman", 15, "bold"), command=self.reset_signIn)
        self.reset_button.place(x=280, y=630)

        self.combo_box_usertypes = ttk.Combobox(self.new_window, font=("times new roman", 15), state="readonly",
                                                justify=CENTER)
        self.combo_box_usertypes.place(x=350, y=130, width=210, height=30)
        self.combo_box_usertypes["values"] = ("Select", "Admin", "Employment")

        # =======To_Focus_In_Only_One_Windows==================================================================================
        self.new_window.grab_set()

        # =======get()=========================================================================================================
        self.user = self.user_name_entry.get()
        self.pas = self.user_password_entry.get()

    def Login(self):
        if self.user_name_entry.get() == "" or self.user_password_entry.get() == "":
            messagebox.showerror("Error", "Please fill all the entries")
            return TRUE
        else:
            if self.combo_box_usertypes.get() == "Employment":
                self.new_window.withdraw()
                self.name_id = self.user_name_entry.get()
                self.password = self.user_password_entry.get()
                self.passget.clear()
                self.passget.append(self.password)

                self.hashedpass = self.password
                self.finalhashed = self.hashedpass.encode("utf-8")

                self.hash = hashlib.md5(self.finalhashed)
                self.hexa = self.hash.hexdigest()

                self.info.Login(self.name_id, self.hexa)
                self.student_id = self.user_name_entry.get()

                file = open('users.txt', 'w')
                file.write(self.user_name_entry.get())
                file.close()

                # print(self.student_id)
                self.user_name_entry.delete(0, END)
                self.user_password_entry.delete(0, END)
                self.namdekhanamdekha = self.info.manche
                self.namdekha2 = str(self.namdekhanamdekha)
                # print(self.namdekha2)
                self.create_otp_window()

    # ===========To_Open_Grocery_Management_System==========================================================================
    def grocery(self):
        print(self.info.otp_email_transfer)
        print(self.info.otp_email_transfer[0][0][0])
        # print(self.info.otp_email_transfer.split('')
        self.new_window.withdraw()
        from LoginSuccess import Success
        self.success = Toplevel(self.new_window)
        Success(self.success)

        # LoginSuccessWindow = Toplevel(self.new_window)
        # messagebox.showinfo("Success","Welcome to ......................")
        # Success(LoginSuccessWindow)

        # return False

        # if self.email_value == True:
        # def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
        #     gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #     features = classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)
        #     for (x,y,w,h) in features:
        #         cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        #         id, pred = clf.predict(gray_img[y:y+h,x:x+w])
        #         confidence = int(100*(1-pred/300))
        #         if confidence>75 and id == int(name):
        #             cv2.putText(img,self.namdekha2, (x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1,cv2.LINE_AA)
        #             # cv2.waitKey(5000)
        #             # if cv2.waitKey(1) == 13:
        #             messagebox.showinfo("Verified","User verified")
        #             video_capture.release()
        #             cv2.destroyAllWindows()

        #             self.closecam.append(7)
        #             grocery()

        #         else:
        #             cv2.putText(img,"Unknown", (x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1,cv2.LINE_AA)
        #             messagebox.showerror("Error","Unknown Faces")
        #             self.noface.append(4)
        #             sys.exit()

        #     video_capture.release()
        #     cv2.destroyAllWindows()
        #     return img
        # faceCascade = cv2.CascadeClassifier("C:\\Users\\Dell\\Music\\NowBegins\\CascadeFile\\haarcascade_frontalface_default.xml")
        # clf = cv2.face.LBPHFaceRecognizer_create()
        # clf.read(name + ".xml")
        # video_capture = cv2.VideoCapture(0)

        # while True:
        #     ret, img = video_capture.read()
        #     img = draw_boundary(img,faceCascade, 1.3,6,(255,255,255),clf)
        #     cv2.imshow("Face Detection",img)
        #     if 7 in self.closecam:
        #         video_capture.release()
        #         cv2.destroyAllWindows()
        #         break
        #     if 7 not in self.closecam and 4 not in self.noface:
        #         video_capture.release()
        #         cv2.destroyAllWindows()
        #         messagebox.showerror("Error","No one's is in camera!")
        #         break
        #     if cv2.waitKey(1) == 13:
        #         break
        # video_capture.release()
        # cv2.destroyAllWindows()

    def reset_signIn(self):
        self.user_reset.set('')
        self.password_reset.set('')
        self.combo_box_usertypes.set('')

    def sign_up(self):
        self.new_window.withdraw()
        from SignUps import SignUp
        self.sign = Toplevel(self.new_window)
        SignUp(self.sign)

    def create_otp_window(self):
        # app = tkinter.Tk()
        self.otp_wind = tkinter.Toplevel()
        self.otp_wind.title("OTP")
        # self.otp_wind.geometry('900x750+0+0')
        self.otp_wind.resizable("false", "false")
        self.otp_wind.grab_set()

        self.OTP_MESSAGE()

        self.label1 = Label(self.otp_wind, text="Enter the OTP send to the registered\nEmail!",
                            font=("times new roman", 10))
        self.label1.place(x=0, y=2)

        self.otpent = Entry(self.otp_wind, font=("times new roman", 10), bg="White", highlightbackground='black',
                            highlightthickness="1")
        self.otpent.place(x=60, y=70, width=80)

        self.bttn_verify = Button(self.otp_wind, text="V  e  r  i  f  y", cursor="hand2", fg="Red", borderwidth=0,
                                  font=("times new roman", 14), command=self.cmd_verify)
        self.bttn_verify.place(x=45, y=120)

    def cmd_verify(self):
        if self.otpent.get() == "":
            messagebox.showerror("Excuse Me!", "Please fill the 4 digit OTP!")
        elif len(self.otpent.get()) != 4:
            messagebox.showerror("Failed", "OTP must be equal to 4 digit!!!! ")
        elif str(self.otpent.get()) == str(self.otp):
            # self.email_value = True
            self.otpent.delete(0, END)
            messagebox.showinfo("Verified!", "OTP Verified")
            # self.email_value = True
            self.otp_wind.destroy()

            def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
                gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
                for (x, y, w, h) in features:
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                    id, pred = clf.predict(gray_img[y:y + h, x:x + w])
                    confidence = int(100 * (1 - pred / 300))
                    if confidence > 75 and id == int(self.name_id):
                        cv2.putText(img, self.namdekha2, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1,
                                    cv2.LINE_AA)
                        # cv2.waitKey(5000)
                        # if cv2.waitKey(1) == 13:
                        messagebox.showinfo("Verified", "User verified")
                        video_capture.release()
                        cv2.destroyAllWindows()

                        self.closecam.append(7)
                        self.grocery()
                        # grocery()

                    else:
                        cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                        messagebox.showerror("Error", "Unknown Faces")
                        self.noface.append(4)
                        sys.exit()

                video_capture.release()
                cv2.destroyAllWindows()
                return img

            faceCascade = cv2.CascadeClassifier(
                "D:\\downloads\\project\\CascadeFile\\haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("D:\\downloads\\project\\Code\\"+self.name_id + ".xml")
            # clf.read("D:\\downloads\\project\\Code\\" + "98.xml")
            # clf.read("98.xml")
            video_capture = cv2.VideoCapture(0)
            # print(name)

            while True:
                ret, img = video_capture.read()
                img = draw_boundary(img, faceCascade, 1.3, 6, (255, 255, 255), clf)
                cv2.imshow("Face Detection", img)
                if 7 in self.closecam:
                    video_capture.release()
                    cv2.destroyAllWindows()
                    break
                if 7 not in self.closecam and 4 not in self.noface:
                    video_capture.release()
                    cv2.destroyAllWindows()
                    messagebox.showerror("Error", "No one's is in camera!")
                    break
                if cv2.waitKey(1) == 13:
                    break
            video_capture.release()
            cv2.destroyAllWindows()

            # return self.email_value

            # print("Verified! Verified!!")


        elif str(self.otpent.get()) != str(self.otp):
            # self.email_value = False
            self.otpent.delete(0, END)
            messagebox.showerror("Verify OTP!!!", "OTP Failed to Verify!!")
            # print("Not verified!")


    def OTP_MESSAGE(self):
        self.fromaddr = "checkotp04@gmail.com"
        self.password = "generationxpass"

        self.hashedpass = self.passget[0]
        self.finalhashed = self.hashedpass.encode("utf-8")

        self.hash = hashlib.md5(self.finalhashed)
        self.hexa = self.hash.hexdigest()
        print("4444444444444444444444444444444444")
        print(self.passget[0])
        print(self.hexa)

        self.finalhashed = self.hexa

        # self.hash = hashlib.md5(self.finalhashed)
        # self.hexapass = self.hash.hexdigest()

        self.passlen = self.finalhashed[0:16]
        self.passbyteconvertedfinal = bytes(self.passlen, 'utf-8')

        self.emaildecry = self.info.otp_email_transfer[0][0][0]
        # b = self.emaildecry.encode('utf-8')
        # print(b)
        # print(self.emaildecry)\
        # print(type(self.emaildecry))
        # bb = bytes(self.emaildecry)
        # print(type(bb))
        # print(bb)
        # print(bb)
        # # print(bb)
        # print("4654654654654654654654654564154")
        # print(type(self.emaildecry))
        # print(".........")
        # print(self.emaildecry)
        # print(".........")
        # self.emailbyteconv = self.emaildecry
        # print(self.emailbyteconv)

        # # self.emailconvertbyte = self.emailbyteconv#b"\xbfp\xf3\x9eT\t\xef\xe81\xb5\x8a6\x88\x10`\x83\x02N\x18G#2x\x1e\xceA>\x9d\xb0\x11\xae"
        # # print(self.emailconvertbyte)
        # print("*************22222222**")
        # planeeee = b"'"+"\x07\x02$ \xc2\xaf\xc2\xa9\xc3\x9bT\xc3\xa0T~B\xc3\x8c\xc2\x9c\xc2\x87\xc2\xb7\xc2\x9e$f\xc3\xad\xc2\x93\xc3\xbc\xc2\x86*\xc3\xae]\xc3\xb4\xc3\x86\xc3\xb6\xc3\xbb0"+"'"
        # print(type(planeeee))
        # paspos = bytes(self.emaildecry,'utf-8')
        # print("///////////////////////////////////////")
        # print(type(paspos))
        # print(paspos)

        # self.secretkey = self.passbyteconvertedfinal
        # self.email_nonce = planeeee[:8]
        # self.ciphertextofemail = planeeee[8:]
        # cipher = Salsa20.new(key=self.secretkey, nonce=self.email_nonce)
        # self.plaintext = cipher.decrypt(self.ciphertextofemail)
        # print(self.plaintext)

        # # self.orgiemailconvtd = str(self.plaintext)

        # # self.emaillen = len(self.orgiemailconvtd)-1

        # # self.finalemail = self.orgiemailconvtd[2:self.emaillen]
        # # print(self.finalemail)
        # # # print(plaintext)

        emaildecoded = cryptocode.decrypt(self.emaildecry, self.finalhashed)
        print(self.emaildecry)
        print(emaildecoded)
        print(type(emaildecoded))

        # self.toaddr = self.info.otp_email_transfer[0][0][0]
        p = t.strftime("%X")
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = emaildecoded
        msg['Subject'] = self.subj
        self.body = self.message_body
        msg.attach(MIMEText(self.body, 'plain'))
        self.filename = "test.jpg"
        attachment = open(self.filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % self.filename)
        msg.attach(p)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.fromaddr, self.password)
        text = msg.as_string()
        server.send_message(msg)
        server.quit()


def main():
    window = Tk()
    obj = Sign(window)
    window.mainloop()


if __name__ == '__main__':
    main()

