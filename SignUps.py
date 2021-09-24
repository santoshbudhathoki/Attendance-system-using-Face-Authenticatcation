from base64 import encode
from tkinter import *
from register_info import Info
from Login import Sign
# from classes.Admin_infp import food_info
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import datetime
# from datetime  import date, time, datetime
import cv2
import os
from PIL import Image
import numpy as np
import hashlib
from pathlib import Path
from Crypto.Cipher import Salsa20
import cryptocode

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


class SignUp:
    def __init__(self, window):
        # =======Creating_Geometry============================================================================================
        # ====================================================================================================================
        self.window = window
        self.window.title("User Registration")
        self.window.geometry('1150x700+0+0')
        self.window.resizable("false", "false")

        self.email_value = ""
        self.usernamegetbefore = ""
        self.namegetbefore = ""
        self.savecon = ""

        self.otp = random.randint(1000, 9999)
        self.subj = "Email from Softwarica College [" + p + "]"
        self.message_body = "Hello User!!!\n" + name + "\nTo authenticate, please use the following One Time password(OTP)\n" + str(
            self.otp) + "\nIf you require any assistance, please contact" \
                        " our 24 hr Customer Service"

        def time():
            now = datetime.datetime.now()
            self.date = (now.strftime("%I:%M:%S:%p"))
            self.daa = (now.strftime("%H:%M:%S '/n' %d-%m-%y"))
            self.clock_label = Label(self.window, font=('times new roman', 12), fg='black', bg="White", text=self.date)
            self.clock_label.place(x=1010, y=115)
            self.clock_label.after(200, time)

        time()

        # =======Importing_Class_Of_Register_Info=============================================================================
        # ====================================================================================================================
        self.info = Info()

        # =======Adding_Bg_Image==============================================================================================
        # ====================================================================================================================
        self.bg2 = ImageTk.PhotoImage(file="D:\\downloads\\project\\Images\\user_registration.jpg")
        bg = Label(self.window, bg="black", image=self.bg2).place(x=0, y=0, relwidth=1, relheight=1)

        # =======Left_Image===================================================================================================
        # ====================================================================================================================
        self.left = ImageTk.PhotoImage(file="D:\\downloads\\project\\Images\\frame1.jpg")
        # left = Label(self.window,image=self.left,bg="white").place(x=20,y=100,width=400,height=500)

        self.lbl = Label(self.window, image=self.left)
        self.lbl.place(x=420, y=100, width=700, height=500)

        # =======Frame_1======================================================================================================
        # ====================================================================================================================
        # self.self.lbl=Frame(self.window,bg="white")
        # self.self.lbl.place(x=420,y=100,width=700,height=500)

        # =======For_Reset_Button==============================================================================================
        # ====================================================================================================================
        self.Name = StringVar()
        self.Phone = StringVar()
        self.Email = StringVar()
        self.Adress = StringVar()
        self.Password = StringVar()
        self.Repassword = StringVar()
        self.emailsss = StringVar()

        # =======Label_And_Entry_For_Registration==============================================================================
        # ===================================================================================================================
        # self.name = Label(self.lbl,text="Full Name",bg="white",fg="green",font=("times new roman",20,"bold"))
        # self.name.place(x=0,y=8,width=250)

        self.name_entry = Entry(self.lbl, font=("times new roman", 15), bg="White", highlightbackground='black',
                                highlightthickness="1", textvariable=self.Name)
        self.name_entry.place(x=10, y=50, width=250)

        # self.phone = Label(self.lbl, text="Phone No", bg="white", fg="green", font=("times new roman", 20, "bold"))
        # self.phone.place(x=350, y=8,width=250)

        self.phone_entry = Entry(self.lbl, font=("times new roman", 15), bg="White", highlightbackground='black',
                                 highlightthickness="1", textvariable=self.Phone)
        self.phone_entry.place(x=350, y=50, width=250)
        #
        # self.email = Label(self.lbl, text="Email", bg="white", fg="green", font=("times new roman", 20, "bold"))
        # self.email.place(x=0, y=90,width=250)

        self.email_entry = Entry(self.lbl, font=("times new roman", 15), bg="White", highlightbackground='black',
                                 highlightthickness="1", textvariable=self.Email)
        self.email_entry.place(x=10, y=130, width=250)

        self.real_email_entry = Entry(self.lbl, font=("times new roman", 15), bg="White", highlightbackground='black',
                                      highlightthickness="1", textvariable=self.emailsss)
        self.real_email_entry.place(x=0, y=350, width=250)

        self.bttn_verify = Button(self.lbl, text="V e r i f y", cursor="hand2", fg="Red", bg="White", borderwidth=0,
                                  font=("times new roman", 12), command=self.cmd_verify)
        self.bttn_verify.place(x=500, y=350)

        self.bttn_send = Button(self.lbl, text="Send", cursor="hand2", fg="Red", bg="White", borderwidth=0,
                                font=("times new roman", 12), command=self.OTP_MESSAGE)
        self.bttn_send.place(x=260, y=350)

        self.otpent = Entry(self.lbl, font=("times new roman", 15), bg="White", highlightbackground='black',
                            highlightthickness="1")
        self.otpent.place(x=500, y=325, width=80)

        # self.gender = Label(self.lbl, text="Gender", bg="white", fg="green", font=("times new roman", 20, "bold"))
        # self.gender.place(x=335, y=88, width=250)

        self.combo_box_gender = ttk.Combobox(self.lbl, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.combo_box_gender.place(x=350, y=130, width=250, height=30)
        self.combo_box_gender["values"] = ("Select", "Male", "Female")

        # self.adress = Label(self.lbl, text="Address", bg="white", fg="green", font=("times new roman", 20, "bold"))
        # self.adress.place(x=0,y=170,width=250)

        self.adress_entry = Entry(self.lbl, font=("times new roman", 15), bg="White", highlightbackground='black',
                                  highlightthickness="1", textvariable=self.Adress)
        self.adress_entry.place(x=10, y=210, width=250)

        # self.password = Label(self.lbl, text="Password", bg="white", fg="green", font=("times new roman", 20, "bold"))
        # self.password.place(x=350,y=172,width=250)

        self.password_entry = Entry(self.lbl, font=("times new roman", 15), bg="White", show="*", fg="red",
                                    highlightbackground='black', highlightthickness="1", textvariable=self.Password)
        self.password_entry.place(x=350, y=210, width=250)

        # self.re_password = Label(self.lbl, text="Re Enter Password", bg="white", fg="green",font=("times new roman", 20, "bold"))
        # self.re_password.place(x=0, y=250, width=250)

        self.re_password_entry = Entry(self.lbl, font=("times new roman", 15), bg="White", show="*", fg="red",
                                       highlightbackground='black', highlightthickness="1",
                                       textvariable=self.Repassword)
        self.re_password_entry.place(x=6, y=290, width=250)

        # =======Buttons=======================================================================================================
        # ====================================================================================================================
        self.bttn_signin = Button(self.window, text="S i g n   I n", cursor="hand2", fg="Red", bg="White",
                                  borderwidth=0, font=("times new roman", 12), command=self.sign_in)
        self.bttn_signin.place(x=540, y=565)

        # self.bttn_capcam = Button(self.window,text="C a p t u r e",cursor="hand2",fg="Red",bg="White",borderwidth=0,font=("times new roman",12),command=self.generate_dataset)
        # self.bttn_capcam.place(x=620,y=565)

        self.bttn_reset = Button(self.lbl, activeforeground="Red", activebackground="White",
                                 text="R    e    s    e    t", cursor="hand2", borderwidth=0, bg="White",
                                 font=("times new roman", 15), command=self.reset)
        self.bttn_reset.place(x=350, y=280, width=250)

        self.bttn_register = Button(self.lbl, activeforeground="Red", activebackground="White",
                                    text="R  e  g  i  s  t  e  r", cursor="hand2", bg="White", borderwidth=0,
                                    font=("times new roman", 15, "bold"), command=self.Register)
        self.bttn_register.place(x=380, y=450, width=300)

        self.lb2 = Label(self.window, text="A  l  r  e  a  d  y    h  a  v  e    a  c  c  o  u  n  t ?",
                         font=("times new roman", 9), bg="White")
        self.lb2.place(x=460, y=546)

        # self.bttn_exit = Button(self.lbl, text="Exit", font=("times new roman", 15),bg="red",command=self.window.quit)
        # self.bttn_exit.place(x=590, y=460, width=100)

        # =======For_Check_Buttons=============================================================================================
        # ====================================================================================================================
        self.variable2 = IntVar()
        self.check_button = Checkbutton(self.lbl, text="I Agree The Terms & Conditions",
                                        font=("times new roman", 15, "bold"), variable=self.variable2, onvalue=1,
                                        offvalue=0, bg="white")
        self.check_button.place(x=260, y=370)

    # ===DIFFERENT FUNCTIONS===============================================================================================
    # ===Reset=============================================================================================================
    # =====================================================================================================================
    # ====================================================================================================================
    def reset(self):
        self.Name.set('')
        self.Phone.set('')
        self.Email.set('')
        self.Adress.set('')
        self.Password.set('')
        self.Repassword.set('')
        self.combo_box_gender.set('')
        self.emailsss.set('')

    def OTP_MESSAGE(self):
        if self.real_email_entry.get() == "":
            messagebox.showerror("Email Empty", "Please Enter the email to verify")
        else:
            self.fromaddr = "checkotp04@gmail.com"
            self.password = "generationxpass"
            self.toaddr = self.real_email_entry.get()
            p = t.strftime("%X")
            msg = MIMEMultipart()
            msg['From'] = self.fromaddr
            msg['To'] = self.toaddr
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

    # ===Sign_In_Window====================================================================================================
    # =====================================================================================================================
    def sign_in(self):

        # self.san()

        # =======To_Close_Previous_Window======================================================================================
        # ====================================================================================================================
        self.window.withdraw()
        # =======T0_Open_Login_Window==========================================================================================
        # ====================================================================================================================
        self.top = Toplevel(self.window)
        Sign(self.top)

    def Register(self):
        nam = self.name_entry.get()
        pas = self.password_entry.get()

        # ======To_Create_Different_Exceptions=================================================================================
        # ====================================================================================================================
        def exception():
            try:
                self.string_answer = self.phone_entry.get()
                self.std_id = self.email_entry.get()
                self.int_answer = int(self.string_answer)
                self.int_id = int(self.std_id)
                self.count = len(self.string_answer)
                if self.count != int(10):
                    messagebox.showerror("Error", "Phone numbers must be equals to 10!")
                    return TRUE
                if self.email_entry == str():
                    messagebox.showerror("Student Id can't be string")
            except ValueError:
                messagebox.showerror("Error", "Number or Id can't includes string values!")
                return TRUE

        # =======Psswd=["/","!","_"]===========================================================================================
        # ====================================================================================================================
        if self.name_entry.get() == "" or self.phone_entry.get() == "" or self.adress_entry.get() == "" or self.password_entry.get() == "" or self.re_password_entry.get() == "" or self.real_email_entry.get() == "":
            messagebox.showerror("Error", "please fill all the entries!")

        elif self.password_entry.get() != self.re_password_entry.get():
            messagebox.showerror("Error", "your password did not match!")

        elif exception():
            return TRUE

        elif self.variable2.get() == 0:
            messagebox.showerror("Error", "Please Accept Terms & Conditions!")

        else:
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            address = self.adress_entry.get()
            password = self.password_entry.get()
            cmbo_box = self.combo_box_gender.get()
            username = self.email_entry.get()
            email = self.real_email_entry.get()

            self.hashedpass = password
            self.finalhashed = self.hashedpass.encode("utf-8")

            self.hash = hashlib.md5(self.finalhashed)
            self.hexa = self.hash.hexdigest()

            encoded = cryptocode.encrypt("hello my name is saurav pokhrel", "03c7c0ace395d80182db07ae2c30f034")
            print(encoded)
            print(type(encoded))
            ## And then to decode it:
            decoded = cryptocode.decrypt(encoded, "03c7c0ace395d80182db07ae2c30f034")
            print(decoded)
            print(type(decoded))

            encodedname = cryptocode.encrypt(name, self.hexa)
            encodedemail = cryptocode.encrypt(email, self.hexa)
            encodedaddress = cryptocode.encrypt(address, self.hexa)
            encodedgender = cryptocode.encrypt(cmbo_box, self.hexa)
            encodedphone = cryptocode.encrypt(phone, self.hexa)
            # encoded = cryptocode.encrypt(name,self.hexa)

            # kkkk = self.hexa
            # lenkk = kkkk[0:16]
            # kkkbyteconv = bytes(lenkk,'utf-8')

            # self.namvankhate = self.name_entry.get()
            # self.emailvan = self.real_email_entry.get()
            # self.addressvan = self.adress_entry.get()
            # self.gendervan = self.combo_box_gender.get()
            # self.phonevan = self.phone_entry.get()

            # self.emailconbyte = bytes(self.emailvan,'utf-8')
            # self.namconvbyte = bytes(self.namvankhate,'utf-8')

            # self.addressconbyte = bytes(self.addressvan,'utf-8')

            # self.genderconbyte = bytes(self.gendervan,'utf-8')

            # self.phoneconbyte = bytes(self.phonevan,'utf-8')

            # plaintext = self.namconvbyte
            # plaintext1 = self.emailconbyte
            # plaintext2 = self.addressconbyte
            # plaintext3 = self.genderconbyte
            # plaintext4 = self.phoneconbyte

            # secret = kkkbyteconv
            # cipher = Salsa20.new(key=secret)
            # cipher1 = Salsa20.new(key=secret)
            # cipher2 = Salsa20.new(key=secret)
            # cipher3 = Salsa20.new(key=secret)
            # cipher4 = Salsa20.new(key=secret)

            # self.msg = cipher.nonce + cipher.encrypt(plaintext)
            # self.msg1 = cipher1.nonce + cipher1.encrypt(plaintext1)
            # self.msg2 = cipher2.nonce + cipher2.encrypt(plaintext2)
            # self.msg3 = cipher3.nonce + cipher3.encrypt(plaintext3)
            # self.msg4 = cipher4.nonce + cipher4.encrypt(plaintext4)

            # print(self.msg)

            # msgname = str(self.msg)
            # print("**************************************")
            # msgemail = str(self.msg1)
            # msgaddress = str(self.msg2)
            # msggender = str(self.msg3)
            # msgphone = str(self.msg4)

            # msgnamelen = len(msgname)-1
            # msgemaillen = len(msgemail)-1
            # msgaddresslen = len(msgaddress)-1
            # msggenderlen = len(msggender)-1
            # msgphonelen = len(msgphone)-1

            # print("...............................")
            # self.nampatha = msgname[2:msgnamelen]
            # self.emailpatha = msgemail[2:msgemaillen]
            # self.addresspatha = msgaddress[2:msgaddresslen]
            # self.genderpatha = msggender[2:msggenderlen]
            # self.phonepatha = msgphone[2:msgphonelen]

            # print(self.nampatha)
            # print(self.emailpatha)
            # print(self.addresspatha)
            # print(self.genderpatha)
            # print(self.phonepatha)

            if self.info.find_user(username):
                print("ooooo")
            if self.email_value == False or self.email_value == "":
                messagebox.showerror("Verify OTP", "First verify the 4 digit OTP!")
            elif self.email_value == True:
                # messagebox.showinfo("Verified","OTP verified!\nNow Click on")
                self.info.Register(str(encodedname), str(encodedphone), str(encodedgender), str(encodedaddress),
                                   self.hexa, username, str(encodedemail))
                self.generate_dataset()
                self.savecon = True
                if self.savecon == True:
                    messagebox.showinfo("Congratulation", "Registration Successfull !")
                    self.encrypt()
                    # else:
                #     self.info.Register(name, phone, cmbo_box, address, password,username,email)
                #     self.generate_dataset()

                #     messagebox.showinfo("Congratulation","Registration Successfull !")

                # ===============To_Delete_Entries_Fill_After_Register_Button_Is_Clicked===============================================
                # =====================================================================================================================
                self.name_entry.delete(0, END)
                self.phone_entry.delete(0, END)
                self.email_entry.delete(0, END)
                self.adress_entry.delete(0, END)
                self.password_entry.delete(0, END)
                self.re_password_entry.delete(0, END)
                self.real_email_entry.delete(0, END)

    def cmd_verify(self):
        if self.otpent.get() == "":
            messagebox.showerror("Excuse Me!", "Please fill the 4 digit OTP!")
        elif len(self.otpent.get()) != 4:
            messagebox.showerror("Failed", "OTP must be equal to 4 digit!!!! ")
        elif str(self.otpent.get()) == str(self.otp):
            self.email_value = True
            self.otpent.delete(0, END)
            messagebox.showinfo("Verified!", "OTP Verified")
            self.usernamegetbefore = self.email_entry.get()
            self.namegetbefore = self.name_entry.get()
            print("Verified! Verified!!")


        elif str(self.otpent.get()) != str(self.otp):
            self.email_value = False
            self.otpent.delete(0, END)
            messagebox.showerror("Verify OTP!!!", "OTP Failed to Verify!!")
            print("Not verified!")

    def generate_dataset(self):
        if not os.path.exists("D:\\downloads\\project\\RegistrantImages\\" + self.name_entry.get()):
            b = os.makedirs("D:\\downloads\\project\\RegistrantImages\\" + self.name_entry.get())
        # Create folder of person (IF NOT EXISTS) in the images folder
        # Path("images/" + self.name.get()).mkdir(parents=True, exist_ok=True)

        # Obtain the number of photos already in the folder
        numberOfFile = len([filename for filename in
                            os.listdir("D:\\downloads\\project\\\RegistrantImages\\" + self.name_entry.get())
                            if os.path.isfile(
                os.path.join("D:\\downloads\\project\\RegistrantImages\\" + self.name_entry.get(),
                             filename))])
        # Add 1 because we start at 1
        numberOfFile += 1
        print(numberOfFile)
        face_classifier = cv2.CascadeClassifier(
            "D:\\downloads\\project\\CascadeFile\\haarcascade_frontalface_default.xml")

        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.1, 4)

            if faces is ():
                return None
            for (x, y, w, h) in faces:
                cropped_face = img[y:y + h, x:x + w]
            return cropped_face

        cap = cv2.VideoCapture(0)
        id = self.email_entry.get()
        img_id = 0
        while True:
            ret, frame = cap.read()
            if face_cropped(frame) is not None:
                img_id += 1
                face = cv2.resize(face_cropped(frame), (500, 500))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                cv2.imwrite(str(id) + "." + str(img_id) + ".jpg",
                            face)
                os.replace(str(id) + "." + str(img_id) + ".jpg",
                           "D:\\downloads\\project\\RegistrantImages\\" + self.name_entry.get() + "\\image." + str(
                               id) + "." + str(img_id) + ".jpg")
                cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Cropped Face", face)

                # file_name_path = "C:\\Users\\Dell\\Music\\NowBegins\\RegistrantImages\\image."+str(id)+"."+str(img_id)+".jpg"
                # cv2.imwrite(file_name_path,face)
                # cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                # cv2.imshow("Cropped Face", face)
            if cv2.waitKey(1) == 13 or int(img_id) == 200:
                break
        cap.release()
        cv2.destroyAllWindows()
        print("Collecting sample is completed")
        m = "D:\\downloads\\project\\RegistrantImages\\" + str(self.name_entry.get())

        def train_classifier(data_dir):
            path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]

            faces = []
            ids = []

            for image in path:
                img = Image.open(image).convert('L')
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split(".")[1])
                faces.append(imageNp)
                ids.append(id)
            ids = np.array(tuple(ids))

            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            # individualclassifier_path = "C:\\Users\Dell\\Music\\NowBegins\\IndividualClassifier" + self.email_entry.get() + ".xml"
            clf.write(self.email_entry.get() + ".xml")

        train_classifier(m)





    # def san(self):


        # from PIL import Image, ImageTk
        # from tkinter import ttk
        # from tkinter import messagebox
        # from register_info import Info
        # from attendence_database import Attend
        # import datetime
        # import os
        # import cv2
        # import numpy as np
        # from PIL import Image
        # import datetime
        # import cryptocode
        # import os
        # from pathlib import Path
        #
        # self.userid = 78
        # self.closecam = []
        #
        # self.info = Info()
        # self.infoattend = Attend()
        # # self.show_attendence_data()
        #
        # # self.info2=std_num()
        # # print(self.info2.user_name_entry.get())
        # # with open('users.txt') as f:
        # #     data = f.read()
        # #
        # # self.info.details_show(int(data))
        #
        #
        #
        # # for date
        #
        #
        # self.namdekhanamdekha = self.info.manche
        # self.namdekha2 = (self.namdekhanamdekha)
        # print(self.namdekha2)
        # self.nameforcam = self.namdekha2[0][4]
        # self.idforcam = self.namdekha2[0][0]
        # # print(self.nameforcam)
        # print(len(self.idforcam))
        #
        # self.fordecid = self.namdekha2[0][4]
        #
        # self.fordecname = self.namdekha2[0][4]
        # # self.fordecphone = self.namdekha2[0][1]
        # # self.fordecgender = self.namdekha2[0][2]
        # # self.fordecaddress = self.namdekha2[0][3]
        # self.fordecpass = self.namdekha2[0][5]
        #
        # self.decodedname = cryptocode.decrypt(self.fordecname, self.fordecpass)
        # # self.decodedphone = cryptocode.decrypt(self.fordecphone, self.fordecpass)
        # # self.decodedgender = cryptocode.decrypt(self.fordecgender, self.fordecpass)
        # # self.decodedaddress = cryptocode.decrypt(self.fordecaddress, self.fordecpass)
        # print(self.decodedname)



        # print(s)
        #
        # print('Total number of files', totalFiles)
        # print('Total Number of directories', totalDir)
        # print('Total:', (totalDir + totalFiles))
    def encrypt(self):
        APP_FOLDER = ('D:/downloads/project/RegistrantImages/' +self.namegetbefore)

        totalFiles = 0
        totalDir = 0

        for base, dirs, files in os.walk(APP_FOLDER):
            print('Searching in : ', base)
            for directories in dirs:
                totalDir += 1
            for Files in files:
                totalFiles += 1

        s = totalFiles

        j = 1
        print(self.namegetbefore)
        for i in range(1,s+1):
            self.img_path = Path("D:\\downloads\\project\\RegistrantImages\\"+self.namegetbefore+"\\"+"image"+"."+ self.usernamegetbefore + "." + str(j) + ".jpg")
            # take input key for an image incryption
            key = 1

            # open file to read data
            self.f = open(self.img_path, 'rb')

            # storing image data in image variable
            self.image = self.f.read()
            self.f.close()

            # converting image into byte array to
            # perform encryption on it's data
            self.image1 = bytearray(self.image)
            # perform XOR operation on each value of bytearray
            for index, values in enumerate(self.image1):
                self.image1[index] = values ^ key
            # open file to write data
            self.f1 = open(self.img_path, 'wb')

            # write encrypted data of image1
            self.f1.write(self.image1)
            self.f1.close()
            print('Encryption or Decryption Done...')
            print('Encryption or Decryption key is: ', key)
            j= j+1



# from tkinter import *
# from register_info import Info
# from Login import Sign
# # from classes.Admin_infp import food_info
# from PIL import Image,ImageTk
# from tkinter import ttk
# from tkinter import messagebox
# import datetime
# import cv2
# import os
# from pathlib import Path
# from PIL import Image
# import numpy as np
#
#
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
#
#
# class SignUp:
#     def __init__(self,window):
# #=======Creating_Geometry============================================================================================
# #====================================================================================================================
#         self.window = window
#         self.window.title("User Registration")
#         self.window.geometry('1150x700+0+0')
#         self.window.resizable("false","false")
#
#         self.email_value = ""
#         self.otp = random.randint(1000,9999)
#
#
#         self.subj = "Email from Softwarica College [" + p + "]"
#
#         self.message_body = "Hello User!!!\n" + name + "\nTo authenticate, please use the following One Time password(OTP)\n" + str(self.otp) + "\nIf you require any assistance, please contact" \
#                                                                                                           " our 24 hr Customer Service"
#
#
#         def time():
#             now = datetime.datetime.now()
#             self.date = (now.strftime("%I:%M:%S:%p"))
#             self.daa = (now.strftime("%H:%M:%S '/n' %d-%m-%y"))
#             self.clock_label = Label(self.window, font=('times new roman', 12), fg='black', bg="White",text=self.date)
#             self.clock_label.place(x=1010, y=115)
#             self.clock_label.after(200, time)
#         time()
#
# #=======Importing_Class_Of_Register_Info=============================================================================
# #====================================================================================================================
#         self.info = Info()
#
# #=======Adding_Bg_Image==============================================================================================
# #====================================================================================================================
#         self.bg2 = ImageTk.PhotoImage(file="D:\\downloads\\project\\Images\\user_registration.jpg")
#         bg = Label(self.window,bg="black",image=self.bg2).place(x=0,y=0,relwidth=1,relheight=1)
#
# #=======Left_Image===================================================================================================
# #====================================================================================================================
#         self.left = ImageTk.PhotoImage(file="D:\\downloads\\project\\Images\\frame1.jpg")
#         # left = Label(self.window,image=self.left,bg="white").place(x=20,y=100,width=400,height=500)
#
#         self.lbl = Label(self.window,image=self.left)
#         self.lbl.place(x=420,y=100,width=700,height=500)
#
#
# #=======Frame_1======================================================================================================
# #====================================================================================================================
#         # self.self.lbl=Frame(self.window,bg="white")
#         # self.self.lbl.place(x=420,y=100,width=700,height=500)
#
# #=======For_Reset_Button==============================================================================================
# #====================================================================================================================
#         self.Name = StringVar()
#         self.Phone = StringVar()
#         self.Email = StringVar()
#         self.Adress = StringVar()
#         self.Password = StringVar()
#         self.Repassword = StringVar()
#         self.emailsss = StringVar()
#
# #=======Label_And_Entry_For_Registration==============================================================================
# #===================================================================================================================
#         # self.name = Label(self.lbl,text="Full Name",bg="white",fg="green",font=("times new roman",20,"bold"))
#         # self.name.place(x=0,y=8,width=250)
#
#         self.name_entry = Entry(self.lbl,font=("times new roman",15),bg="White",highlightbackground='black',highlightthickness="1",textvariable=self.Name)
#         self.name_entry.place(x=10,y=50,width=250)
#
#         # self.phone = Label(self.lbl, text="Phone No", bg="white", fg="green", font=("times new roman", 20, "bold"))
#         # self.phone.place(x=350, y=8,width=250)
#
#         self.phone_entry = Entry(self.lbl, font=("times new roman", 15), bg="White",highlightbackground='black',highlightthickness="1",textvariable=self.Phone)
#         self.phone_entry.place(x=350, y=50,width=250)
#         #
#         # self.email = Label(self.lbl, text="Email", bg="white", fg="green", font=("times new roman", 20, "bold"))
#         # self.email.place(x=0, y=90,width=250)
#
#         self.email_entry = Entry(self.lbl, font=("times new roman", 15), bg="White",highlightbackground='black',highlightthickness="1",textvariable=self.Email)
#         self.email_entry.place(x=10, y=130,width=250)
#
#         # self.gender = Label(self.lbl, text="Gender", bg="white", fg="green", font=("times new roman", 20, "bold"))
#         # self.gender.place(x=335, y=88, width=250)
#
#         self.combo_box_gender = ttk.Combobox(self.lbl,font=("times new roman", 15),state="readonly",justify=CENTER)
#         self.combo_box_gender.place(x=350,y=130,width=250,height=30)
#         self.combo_box_gender["values"] = ("Select","Male","Female")
#
#         # self.adress = Label(self.lbl, text="Address", bg="white", fg="green", font=("times new roman", 20, "bold"))
#         # self.adress.place(x=0,y=170,width=250)
#
#         self.adress_entry = Entry(self.lbl, font=("times new roman", 15), bg="White",highlightbackground='black',highlightthickness="1",textvariable=self.Adress)
#         self.adress_entry.place(x=10,y=210,width=250)
#
#         # self.password = Label(self.lbl, text="Password", bg="white", fg="green", font=("times new roman", 20, "bold"))
#         # self.password.place(x=350,y=172,width=250)
#
#         self.password_entry = Entry(self.lbl, font=("times new roman", 15), bg="White",show="*",fg="red",highlightbackground='black',highlightthickness="1",textvariable=self.Password)
#         self.password_entry.place(x=350, y=210, width=250)
#
#
#
#         self.re_password_entry = Entry(self.lbl, font=("times new roman", 15), bg="White",show="*",fg="red",highlightbackground='black',highlightthickness="1",textvariable=self.Repassword)
#         self.re_password_entry.place(x=6, y=290, width=250)
#
#
#         self.ema_password = Label(self.lbl, text="Email", bg="white", fg="Black",
#                          font=("times new roman", 17, "bold"))
#         self.ema_password.place(x=0, y=320, width=200)
#
#
#         self.bttn_verify = Button(self.lbl, text="V e r i f y", cursor="hand2", fg="Red", bg="White", borderwidth=0,
#                           font=("times new roman", 12), command=self.cmd_verify)
#         self.bttn_verify.place(x=500, y=350)
#
#         self.real_email_entry = Entry(self.lbl, font=("times new roman", 15), bg="White", highlightbackground='black',
#                               highlightthickness="1", textvariable=self.emailsss)
#         self.real_email_entry.place(x=0, y=350, width=250)
#
# #=======Buttons=======================================================================================================
# #====================================================================================================================
#
#         self.bttn_send = Button(self.lbl, text="Send", cursor="hand2", fg="Red", bg="White", borderwidth=0,
#                         font=("times new roman", 12), command=self.OTP_MESSAGE)
#         self.bttn_send.place(x=260, y=350)
#
#
#         self.otpent = Entry(self.lbl, font=("times new roman", 15), bg="White", highlightbackground='black',
#                     highlightthickness="1")
#         self.otpent.place(x=500, y=325, width=80)
#
#         self.bttn_signin = Button(self.window,text="S i g n   I n",cursor="hand2",fg="Red",bg="White",borderwidth=0,font=("times new roman",12),command=self.sign_in)
#         self.bttn_signin.place(x=540,y=565)
#
#         # self.bttn_capcam = Button(self.window,text="C a p t u r e",cursor="hand2",fg="Red",bg="White",borderwidth=0,font=("times new roman",12),command=self.generate_dataset)
#         # self.bttn_capcam.place(x=620,y=565)
#
#         self.bttn_reset = Button(self.lbl,activeforeground="Red",activebackground="White", text="R    e    s    e    t",cursor="hand2",borderwidth=0,bg="White", font=("times new roman", 15),command=self.reset)
#         self.bttn_reset.place(x=350, y=280,width=250)
#
#         self.bttn_register = Button(self.lbl,activeforeground="Red",activebackground="White", text="R  e  g  i  s  t  e  r",cursor="hand2",bg="White",borderwidth=0,font=("times new roman", 15,"bold"),command=self.Register)
#         self.bttn_register.place(x=380, y=450, width=300)
#
#         self.lb2 = Label(self.window,text="A  l  r  e  a  d  y    h  a  v  e    a  c  c  o  u  n  t ?",font=("times new roman",9),bg="White")
#         self.lb2.place(x=460,y=546)
#
#         # self.bttn_exit = Button(self.lbl, text="Exit", font=("times new roman", 15),bg="red",command=self.window.quit)
#         # self.bttn_exit.place(x=590, y=460, width=100)
#
# #=======For_Check_Buttons=============================================================================================
# #====================================================================================================================
#         self.variable2 = IntVar()
#         self.check_button = Checkbutton(self.lbl,text="I Agree The Terms & Conditions",font=("times new roman",15,"bold"),variable=self.variable2,onvalue=1,offvalue=0,bg="white")
#         self.check_button.place(x=260,y=400)
# #===DIFFERENT FUNCTIONS===============================================================================================
# #===Reset=============================================================================================================
# #=====================================================================================================================
# #====================================================================================================================
#     def reset(self):
#         self.Name.set('')
#         self.Phone.set('')
#         self.Email.set('')
#         self.Adress.set('')
#         self.Password.set('')
#         self.Repassword.set('')
#         self.combo_box_gender.set('')
#
#
#
#
#     def OTP_MESSAGE(self):
#         if self.real_email_entry.get() == "":
#             messagebox.showerror("Email Empty","Please Enter the email to verify")
#         else:
#             self.fromaddr = "checkotp04@gmail.com"
#             self.password = "generationxpass"
#             self.toaddr = self.real_email_entry.get()
#             p = t.strftime("%X")
#             msg = MIMEMultipart()
#             msg['From'] = self.fromaddr
#             msg['To'] = self.toaddr
#             msg['Subject'] = self.subj
#             self.body = self.message_body
#             msg.attach(MIMEText(self.body, 'plain'))
#             self.filename = "test.jpg"
#             attachment = open(self.filename, "rb")
#             p = MIMEBase('application', 'octet-stream')
#             p.set_payload((attachment).read())
#             encoders.encode_base64(p)
#             p.add_header('Content-Disposition', "attachment; filename= %s" % self.filename)
#             msg.attach(p)
#             server = smtplib.SMTP('smtp.gmail.com', 587)
#             server.starttls()
#             server.login(self.fromaddr,self.password)
#             text = msg.as_string()
#             server.send_message(msg)
#             server.quit()
#
# #===Sign_In_Window====================================================================================================
# #=====================================================================================================================
#     def sign_in(self):
# #=======To_Close_Previous_Window======================================================================================
# #====================================================================================================================
#         self.window.withdraw()
# #=======T0_Open_Login_Window==========================================================================================
# #====================================================================================================================
#         self.top = Toplevel(self.window)
#         Sign(self.top)
#
#     def Register(self):
#         nam = self.name_entry.get()
#         pas = self.password_entry.get()
# #======To_Create_Different_Exceptions=================================================================================
# #====================================================================================================================
#         def exception():
#             try:
#                 self.string_answer = self.phone_entry.get()
#                 self.std_id = self.email_entry.get()
#                 self.int_answer = int(self.string_answer)
#                 self.int_id = int(self.std_id)
#                 self.count = len(self.string_answer)
#                 if self.count != int(10):
#                     messagebox.showerror("Error","Phone numbers must be equals to 10!")
#                     return TRUE
#                 if self.email_entry == str():
#                     messagebox.showerror("Student Id can't be string")
#             except ValueError:
#                 messagebox.showerror("Error","Number or Id can't includes string values!")
#                 return TRUE
#
# #=======Psswd=["/","!","_"]===========================================================================================
# #====================================================================================================================
#         if self.name_entry.get() == "" or self.phone_entry.get() == "" or self.adress_entry.get() == "" or self.password_entry.get() == "" or self.re_password_entry.get() == "":
#             messagebox.showerror("Error","please fill all the entries!")
#
#         elif self.password_entry.get() != self.re_password_entry.get():
#             messagebox.showerror("Error","your password did not match!")
#
#         elif exception():
#             return TRUE
#
#         elif self.variable2.get() == 0:
#             messagebox.showerror("Error","Please Accept Terms & Conditions!")
#
#         else:
#             name = self.name_entry.get()
#             phone = self.phone_entry.get()
#             address = self.adress_entry.get()
#             password = self.password_entry.get()
#             cmbo_box = self.combo_box_gender.get()
#             username = self.email_entry.get()
#             email = self.real_email_entry.get()
#
#             if self.info.find_user(username):
#                 print("ooooo")
#
#             else:
#                 self.info.Register(name, phone, cmbo_box, address, password,username,email)
#                 self.generate_dataset()
#
#                 messagebox.showinfo("Congratulation","Registration Successfull !")
#
# #===============To_Delete_Entries_Fill_After_Register_Button_Is_Clicked===============================================
# #=====================================================================================================================
#                 self.name_entry.delete(0,END)
#                 self.phone_entry.delete(0,END)
#                 self.email_entry.delete(0,END)
#                 self.adress_entry.delete(0,END)
#                 self.password_entry.delete(0,END)
#                 self.re_password_entry.delete(0,END)
#
#     def cmd_verify(self):
#         if self.otpent.get() == "":
#             messagebox.showerror("Excuse Me!", "Please fill the 4 digit OTP!")
#         elif len(self.otpent.get()) != 4:
#             messagebox.showerror("Failed", "OTP must be equal to 4 digit!!!! ")
#         elif str(self.otpent.get()) == str(self.otp):
#             self.email_value = True
#             self.otpent.delete(0, END)
#             messagebox.showinfo("Verified!", "OTP Verified")
#             print("Verified! Verified!!")
#
#
#         elif str(self.otpent.get()) != str(self.otp):
#             self.email_value = False
#             self.otpent.delete(0, END)
#             messagebox.showerror("Verify OTP!!!", "OTP Failed to Verify!!")
#             print("Not verified!")
#
#
#             # Obtain the number of photos already in the folder
#
#
#     def generate_dataset(self):
#
#
#
#         if not os.path.exists("D:\\downloads\project\\RegistrantImages\\"+ self.name_entry.get()):
#             b = os.makedirs("D:\\downloads\project\\RegistrantImages\\"+ self.name_entry.get())
#         # Create folder of person (IF NOT EXISTS) in the images folder
#         # Path("images/" + self.name.get()).mkdir(parents=True, exist_ok=True)
#
#
#         # Obtain the number of photos already in the folder
#         numberOfFile = len([filename for filename in os.listdir("D:\\downloads\\project\\RegistrantImages\\" + self.name_entry.get())
#                             if os.path.isfile(os.path.join("D:\\downloads\\project\\RegistrantImages\\" + self.name_entry.get(), filename))])
#         # Add 1 because we start at 1
#         numberOfFile += 1
#         print(numberOfFile)
#         # Create folder of person (IF NOT EXISTS) in the images folder
#         # Path("RegistrantImages\\" + self.name_entry.get()).mkdir(parents=True, exist_ok=True)
#
#         face_classifier = cv2.CascadeClassifier("D:\\downloads\\project\\CascadeFile\\haarcascade_frontalface_default.xml")
#         def face_cropped(img):
#             gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#             faces = face_classifier.detectMultiScale(gray, 1.1, 4)
#
#             if faces is ():
#                 return None
#             for (x,y,w,h) in faces:
#                 cropped_face = img[y:y+h,x:x+w]
#             return cropped_face
#         cap = cv2.VideoCapture(0)
#         id = self.email_entry.get()
#         img_id = 0
#         while True:
#             ret, frame = cap.read()
#             if face_cropped(frame) is not None:
#                 img_id+=1
#                 face = cv2.resize(face_cropped(frame),(500,500))
#                 face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
#
#                 # cv2.imwrite( id+ "." + str(numberOfFile) + ".jpg",
#                 #             frame[y:y + h, x:x + w])
#                 # os.replace(id+ "."+str(numberOfFile) + ".jpg",
#                 #            "images/" + self.name.get().lower() + "/" +id+ "."+ str(numberOfFile) + ".png")
#                 # # display the frame
#
#
#                 # file_name_path = str(id)+"."+str(img_id)+".jpg"
#                 cv2.imwrite(str(id)+"."+str(img_id)+".jpg",
#                             face)
#                 os.replace(str(id)+"."+str(img_id)+".jpg",
#                            "D:\\downloads\\project\\RegistrantImages\\" + self.name_entry.get()+"\\image."+str(id)+"."+str(img_id)+".jpg")
#                 cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
#                 cv2.imshow("Cropped Face", face)
#
#                 # file_name_path = str(id)+"."+str(img_id)+".jpg"
#                 # cv2.imwrite(str(id)+"."+str(img_id)+str(numberOfFile)+".jpg",face)
#                 # os.replace(str(id)+"."+str(img_id)+".jpg",
#                 #            "D:\\downloads\\project\\RegistrantImages\\"+self.name_entry.get()+ "\\"+str(id)+"."+str(numberOfFile)+"."+str(img_id)+".jpg")
#                 # cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
#                 # cv2.imshow("Cropped Face", face)
#             if cv2.waitKey(1)==13 or int(img_id) == 200:
#                 break
#         cap.release()
#         cv2.destroyAllWindows()
#         print("Collecting sample is completed")
#         m = "D:\\downloads\\project\\RegistrantImages\\" + str(self.name_entry.get())
#         def train_classifier(data_dir):
#             path = [os.path.join(data_dir,f) for f in os.listdir(data_dir)]
#
#             faces = []
#             ids = []
#
#             for image in path:
#                 img = Image.open(image).convert('L')
#                 imageNp = np.array(img,'uint8')
#                 id = int(os.path.split(image)[1].split(".")[1])
#                 faces.append(imageNp)
#                 ids.append(id)
#             ids = np.array(tuple(ids))
#
#             clf = cv2.face.LBPHFaceRecognizer_create()
#             clf.train(faces,ids)
#             # individualclassifier_path = "C:\\Users\Dell\\Music\\NowBegins\\IndividualClassifier" + self.email_entry.get() + ".xml"
#             clf.write(self.email_entry.get()+".xml")
#         train_classifier(m)