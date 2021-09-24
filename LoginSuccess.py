# from _typeshed import Self
import re
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
from register_info import Info
from attendence_database import Attend
import datetime
import os
import cv2
import numpy as np
from PIL import Image
import datetime
import cryptocode
import os
from pathlib import Path


class Success:
    def __init__(self, window):
        # =======Creating_Geometry============================================================================================
        # ====================================================================================================================
        self.window = window
        self.window.title("Student Information")
        self.window.geometry('1500x810+0+0')
        self.window.resizable("false", "false")
        self.showLab = Label(self.window, text="WELCOME", bg="white", fg="green", font=("times new roman", 20, "bold"))
        self.showLab.place(x=575, y=8, width=250)

        self.userid = 78
        self.closecam = []

        self.info = Info()
        self.infoattend = Attend()
        # self.show_attendence_data()

        # self.info2=std_num()
        # print(self.info2.user_name_entry.get())
        with open('users.txt') as f:
            data = f.read()

        self.info.details_show(int(data))

        if os.path.exists("users.txt"):
            os.remove("users.txt")

        # for date
        self.e = datetime.datetime.now()
        self.date = "%s/%s/%s" % (self.e.day, self.e.month, self.e.year)
        self.time = "%s:%s:%s" % (self.e.hour, self.e.minute, self.e.second)

        self.namdekhanamdekha = self.info.manche
        self.namdekha2 = (self.namdekhanamdekha)
        print(self.namdekha2)
        self.nameforcam = self.namdekha2[0][4]
        self.idforcam = self.namdekha2[0][0]
        # print(self.nameforcam)
        print(len(self.idforcam))

        self.fordecid = self.namdekha2[0][4]

        self.fordecname = self.namdekha2[0][4]
        self.fordecphone = self.namdekha2[0][1]
        self.fordecgender = self.namdekha2[0][2]
        self.fordecaddress = self.namdekha2[0][3]
        self.fordecpass = self.namdekha2[0][5]

        self.decodedname = cryptocode.decrypt(self.fordecname, self.fordecpass)
        self.decodedphone = cryptocode.decrypt(self.fordecphone, self.fordecpass)
        self.decodedgender = cryptocode.decrypt(self.fordecgender, self.fordecpass)
        self.decodedaddress = cryptocode.decrypt(self.fordecaddress, self.fordecpass)
        print(self.decodedname)
        print(type(self.decodedname))

        self.san()


        self.showLab = Label(self.window, text="Name:", bg="white", fg="green", font=("times new roman", 20, "bold"))
        self.showLab.place(x=0, y=200, width=250)

        self.showLab = Label(self.window, text=self.decodedname, bg="white", fg="green",
                             font=("times new roman", 20, "bold"))
        self.showLab.place(x=325, y=200, width=250)

        self.showLab = Label(self.window, text="Student_Id:", bg="white", fg="green",
                             font=("times new roman", 20, "bold"))
        self.showLab.place(x=0, y=250, width=250)

        self.showLab = Label(self.window, text=self.idforcam, bg="white", fg="green",
                             font=("times new roman", 20, "bold"))
        self.showLab.place(x=325, y=250, width=250)

        self.showLab = Label(self.window, text="Phone:", bg="white", fg="green", font=("times new roman", 20, "bold"))
        self.showLab.place(x=0, y=300, width=250)

        self.showLab = Label(self.window, text=self.decodedphone, bg="white", fg="green",
                             font=("times new roman", 20, "bold"))
        self.showLab.place(x=325, y=300, width=250)

        self.showLab = Label(self.window, text="Gender:", bg="white", fg="green", font=("times new roman", 20, "bold"))
        self.showLab.place(x=0, y=350, width=250)

        self.showLab = Label(self.window, text=self.decodedgender, bg="white", fg="green",
                             font=("times new roman", 20, "bold"))
        self.showLab.place(x=325, y=350, width=250)

        self.showLab = Label(self.window, text="Address:", bg="white", fg="green", font=("times new roman", 20, "bold"))
        self.showLab.place(x=0, y=400, width=250)

        self.showLab = Label(self.window, text=self.decodedaddress, bg="white", fg="green",
                             font=("times new roman", 20, "bold"))
        self.showLab.place(x=325, y=400, width=250)

        self.bttn_attendence = Button(self.window, activeforeground="Red", activebackground="White",
                                      text="T a k e   A t t e n d e n c e", cursor="hand2", bg="White", borderwidth=0,
                                      font=("times new roman", 15, "bold"), command=self.attendence)
        self.bttn_attendence.place(x=650, y=550, width=300)

        self.e = Image.open(
            'D:\\downloads\\project\\RegistrantImages\\' + self.decodedname + "\\image." + self.idforcam + "." + "5" + ".jpg")
        self.resized = self.e.resize((90, 90), Image.ANTIALIAS)

        self.g = ImageTk.PhotoImage(self.resized)

        self.bb = Label(self.window, image=self.g).place(x=100, y=40)

        self.item_tree1 = ttk.Treeview(self.window, columns=('SN_NO', 'DATE', 'TIME'))
        self.item_tree1.place(x=720, y=100, width=600, height=440)
        self.item_tree1['show'] = 'headings'
        self.item_tree1.column('SN_NO', width=50)
        self.item_tree1.column('DATE', width=75)
        self.item_tree1.column('TIME', width=75)
        # self.item_tree1.column('STD_ID', width=100)
        # self.item_tree1.column('total_price', width=50)

        self.item_tree1.heading('SN_NO', text="Serial No")
        self.item_tree1.heading('DATE', text="Attend Date")
        self.item_tree1.heading('TIME', text="Attend Time")
        self.show_attendence_data()
        # self.item_tree1.heading('STD_ID', text="Student ID")
        # self.item_tree1.heading('total_price', text="Total_Price")

    def san(self):
        APP_FOLDER = ('D:/downloads/project/RegistrantImages/' + self.decodedname)

        totalFiles = 0
        totalDir = 0

        for base, dirs, files in os.walk(APP_FOLDER):
            print('Searching in : ', base)
            for directories in dirs:
                totalDir += 1
            for Files in files:
                totalFiles += 1

        s = totalFiles
        # print(s)
        #
        # print('Total number of files', totalFiles)
        # print('Total Number of directories', totalDir)
        # print('Total:', (totalDir + totalFiles))

        # j = 1
        for i in range(1,s+1):
            self.img_path = Path("D:\\downloads\\project\\RegistrantImages\\"+ self.decodedname+"\\image." + self.idforcam + "." + "5" + ".jpg")
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
            # j= j+1



    def show_attendence_data(self):
        self.item_tree1.delete(*self.item_tree1.get_children())
        data = self.infoattend.show_total_attendence(self.idforcam)
        for i in data:
            self.item_tree1.insert("", "end", text=i[0], value=(i[0], i[1], i[2]))

    def attendence(self):
        self.show_attendence_data()
        self.infoattend.FindDate(self.idforcam)
        if len(self.infoattend.already) == 1:
            self.runboun()
            self.infoattend.FindDate(int(10002457))
        elif self.infoattend.datesss != "":
            if self.date in self.infoattend.datesss:
                # print(self.infoattend.datesss[0])
                messagebox.showerror("Error", "Attendence was already taken!")

            # pass

    def runboun(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                id, pred = clf.predict(gray_img[y:y + h, x:x + w])
                confidence = int(100 * (1 - pred / 300))
                if confidence > 85 and id == int(self.idforcam):
                    # if id == int(self.idforcam) and :
                    cv2.putText(img, self.decodedname, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                    if cv2.waitKey(1) == 13:
                        self.infoattend.Attendence(self.date, self.time, self.idforcam)
                        messagebox.showinfo("Success", "Attendence taken successfully!")
                        self.show_attendence_data()
                        cv2.destroyAllWindows()
                        vide_capture.release()
                        cv2.destroyAllWindows()
                        self.closecam.append(4)

                else:
                    cv2.putText(img, "UNKNOWN", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
            return img

        faceCascade = cv2.CascadeClassifier("D:\\downloads\\project\\CascadeFile\\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(self.idforcam + ".xml")
        vide_capture = cv2.VideoCapture(0)
        while True:
            ret, img = vide_capture.read()
            img = draw_boundary(img, faceCascade, 1.3, 6, (255, 255, 255), "Face", clf)
            cv2.imshow("Face Detection", img)
            if 4 in self.closecam:
                vide_capture.release()
                cv2.destroyAllWindows()
                break
            if cv2.waitKey(1) == 13:
                break
        vide_capture.release()
        cv2.destroyAllWindows()




# # import re
# # from tkinter import *
# # from PIL import Image,ImageTk
# # from tkinter import ttk
# # from tkinter import messagebox
# # from register_info import Info
# # from attendence_database import Attend
# # import datetime
# # import os
# # import cv2
# # import numpy as np
# # from PIL import Image
# # import datetime
# # class Success:
# #     def __init__(self,window):
# # #=======Creating_Geometry============================================================================================
# # #====================================================================================================================
# #         self.window = window
# #         self.window.title("Student Information")
# #         self.window.geometry('1500x810+0+0')
# #         self.window.resizable("false","false")
# #         self.showLab = Label(self.window,text="WELCOME",bg="white",fg="green",font=("times new roman",20,"bold"))
# #         self.showLab.place(x=575,y=8,width=250)
# #
# #         self.userid = 78
# #         self.closecam = []
# #
# #         self.info=Info()
# #         self.infoattend = Attend()
# #
# #         # self.info2=std_num()
# #         # print(self.info2.user_name_entry.get())
# #         with open('users.txt') as f:
# #             data = f.read()
# #
# #         self.info.details_show(int(data))
# #
# #
# #         if os.path.exists("users.txt"):
# #             os.remove("users.txt")
# #
# #         # for date
# #         self.e = datetime.datetime.now()
# #         self.date = "%s/%s/%s" % (self.e.day, self.e.month, self.e.year)
# #         self.time = "%s:%s:%s" % (self.e.hour, self.e.minute, self.e.second)
# #
# #
# #
# #         self.namdekhanamdekha = self.info.manche
# #         self.namdekha2 = (self.namdekhanamdekha)
# #         print(self.namdekha2)
# #         self.nameforcam = self.namdekha2[0][4]
# #         self.idforcam = self.namdekha2[0][0]
# #         # print(self.nameforcam)
# #         print(len(self.idforcam))
# #
# #
# #         self.showLab = Label(self.window,text="Name:",bg="white",fg="green",font=("times new roman",20,"bold"))
# #         self.showLab.place(x=0,y=100,width=250)
# #
# #
# #         self.showLab = Label(self.window,text=self.namdekha2[0][4],bg="white",fg="green",font=("times new roman",20,"bold"))
# #         self.showLab.place(x=325,y=100,width=250)
# #
# #         self.showLab = Label(self.window,text="Student_Id:",bg="white",fg="green",font=("times new roman",20,"bold"))
# #         self.showLab.place(x=0,y=200,width=250)
# #
# #         self.showLab = Label(self.window,text=self.namdekha2[0][0],bg="white",fg="green",font=("times new roman",20,"bold"))
# #         self.showLab.place(x=325,y=200,width=250)
# #
# #         self.showLab = Label(self.window,text="Phone:",bg="white",fg="green",font=("times new roman",20,"bold"))
# #         self.showLab.place(x=0,y=300,width=250)
# #
# #         self.showLab = Label(self.window,text=self.namdekha2[0][1],bg="white",fg="green",font=("times new roman",20,"bold"))
# #         self.showLab.place(x=325,y=300,width=250)
# #
# #         self.showLab = Label(self.window,text="Gender:",bg="white",fg="green",font=("times new roman",20,"bold"))
# #         self.showLab.place(x=0,y=400,width=250)
# #
# #         self.showLab = Label(self.window,text=self.namdekha2[0][2],bg="white",fg="green",font=("times new roman",20,"bold"))
# #         self.showLab.place(x=325,y=400,width=250)
# #
# #         self.showLab = Label(self.window,text="Address:",bg="white",fg="green",font=("times new roman",20,"bold"))
# #         self.showLab.place(x=0,y=500,width=250)
# #
# #         self.showLab = Label(self.window,text=self.namdekha2[0][3],bg="white",fg="green",font=("times new roman",20,"bold"))
# #         self.showLab.place(x=325,y=500,width=250)
# #
# #         self.bttn_attendence = Button(self.window,activeforeground="Red",activebackground="White", text="T a k e   A t t e n d e n c e",cursor="hand2",bg="White",borderwidth=0,font=("times new roman", 15,"bold"),command=self.attendence)
# #         self.bttn_attendence.place(x=650, y=550, width=300)
# #
# #
# #         self.item_tree1 = ttk.Treeview(self.window, columns=('SN_NO', 'DATE', 'TIME', 'STD_ID'))
# #         self.item_tree1.place(x=650, y=100, width=800, height=440)
# #         self.item_tree1['show'] = 'headings'
# #         self.item_tree1.column('SN_NO', width=50)
# #         self.item_tree1.column('DATE', width=150)
# #         self.item_tree1.column('TIME', width=150)
# #         self.item_tree1.column('STD_ID', width=100)
# #         # self.item_tree1.column('total_price', width=50)
# #
# #         self.item_tree1.heading('SN_NO', text="Serial No")
# #         self.item_tree1.heading('DATE', text="Attend Date")
# #         self.item_tree1.heading('TIME', text="Attend Time")
# #         self.item_tree1.heading('STD_ID', text="Student ID")
# #         # self.item_tree1.heading('total_price', text="Total_Price")
# #
# #     def attendence(self):
# #         self.infoattend.FindDate(self.idforcam,self.date)
# #         self.attendcount = [self.infoattend.already]
# #         # print(self.infoattend.datesss[0][0])
# #         print(self.date)
# #         print(self.date)
# #
# #         # if self.infoattend.datesss == "":
# #         #     runboun()
# #
# #
# #         print(self.infoattend.datesss)
# #         print(self.infoattend.already)
# #         print(len(self.infoattend.already))
# #         if len(self.infoattend.already) == 1:
# #             self.runboun()
# #             # self.infoattend.already.clear
# #             self.infoattend.FindDate(int(10002457),self.date)
# #
# #         # if self.date not in self.infoattend.datesss:
# #         #     self.runboun()
# #         elif self.infoattend.datesss != "":
# #             if str(self.date) == str(self.infoattend.datesss[0][0]):
# #                 messagebox.showerror("Error","Attendence was already taken!")
# #
# #             # pass
# #     def runboun(self):
# #         def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
# #             gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #             features = classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)
# #             for (x,y,w,h) in features:
# #                 cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
# #                 id, pred = clf.predict(gray_img[y:y+h,x:x+w])
# #                 confidence = int(100*(1-pred/300))
# #                 if confidence>75:
# #                     if id == int(self.idforcam):
# #                         cv2.putText(img,self.nameforcam, (x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1,cv2.LINE_AA)
# #                         if cv2.waitKey(1) == 13:
# #                             self.infoattend.Attendence(self.date,self.time,self.idforcam)
# #                             messagebox.showinfo("Success","Attendence taken successfully!")
# #                             cv2.destroyAllWindows()
# #                             vide_capture.release()
# #                             cv2.destroyAllWindows()
# #                             self.closecam.append(4)
# #                             # vide_capture.release()
# #                             # cv2.destroyAllWindows()
# #                             # break
# #
# #                 else:
# #                     cv2.putText(img,"UNKNOWN", (x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),1,cv2.LINE_AA)
# #             return img
# #         faceCascade = cv2.CascadeClassifier("D:\\downloads\\project\\CascadeFile\\haarcascade_frontalface_default.xml")
# #         clf = cv2.face.LBPHFaceRecognizer_create()
# #         clf.read(self.idforcam+".xml")
# #         vide_capture = cv2.VideoCapture(0)
# #         while True:
# #             ret, img = vide_capture.read()
# #             # img = draw_boundary(img,faceCascade, 1.3,6,(255,255,255),"Face",clf)
# #             img = draw_boundary(img, faceCascade, 1.3, 6, (255, 255, 255), clf)
# #             cv2.imshow("Face Detection",img)
# #             if 4 in self.closecam:
# #                 vide_capture.release()
# #                 cv2.destroyAllWindows()
# #                 break
# #             if cv2.waitKey(1) == 13:
# #
# #                 break
# #         vide_capture.release()
# #         cv2.destroyAllWindows()
# #     # runboun()
# #     # self.runbown()
# #
# #
# #
# #
# # # def main():
# # #     window = Tk()
# # #     obj = Success(window)
# # #     window.mainloop()
# # # if __name__ == '__main__':
# # #     main()
#
#
# # from _typeshed import Self
# import re
#
# from tkinter import *
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
# from SignUps import SignUp
#
#
# class Success:
#     def __init__(self, window):
#         # =======Creating_Geometry============================================================================================
#         # ====================================================================================================================
#         self.window = window
#         self.window.title("Student Information")
#         self.window.geometry('1500x780')
#         # self.window.resizable("false", "false")
#         self.showLab = Label(self.window, text="WELCOME", bg="white", fg="green", font=("times new roman", 20, "bold"))
#         self.showLab.place(x=575, y=8, width=250)
#
#         self.userid = 78
#         self.closecam = []
#
#
#         self.info = Info()
#         self.infoattend = Attend()
#         # self.show_attendence_data()
#
#         # self.info2=std_num()
#         # print(self.info2.user_name_entry.get())
#         with open('users.txt') as f:
#             data = f.read()
#
#         self.info.details_show(int(data))
#
#         if os.path.exists("users.txt"):
#             os.remove("users.txt")
#
#         # for date
#         self.e = datetime.datetime.now()
#         self.date = "%s/%s/%s" % (self.e.day, self.e.month, self.e.year)
#         self.time = "%s:%s:%s" % (self.e.hour, self.e.minute, self.e.second)
#
#         self.namdekhanamdekha = self.info.manche
#         self.namdekha2 = self.namdekhanamdekha
#         print(self.namdekha2)
#         self.nameforcam = self.namdekha2[0][4]
#         self.idforcam = self.namdekha2[0][0]
#         # print(self.nameforcam)
#         print(len(self.idforcam))
#
#         self.showLab = Label(self.window, text="Name:", bg="white", fg="green", font=("times new roman", 20, "bold"))
#         self.showLab.place(x=0, y=200, width=250)
#
#         self.showLab = Label(self.window, text=self.namdekha2[0][4], bg="white", fg="green",
#                              font=("times new roman", 20, "bold"))
#         self.showLab.place(x=325, y=200, width=250)
#
#         self.showLab = Label(self.window, text="Student_Id:", bg="white", fg="green",
#                              font=("times new roman", 20, "bold"))
#         self.showLab.place(x=0, y=250, width=250)
#
#         self.showLab = Label(self.window, text=self.namdekha2[0][0], bg="white", fg="green",
#                              font=("times new roman", 20, "bold"))
#         self.showLab.place(x=325, y=250, width=250)
#
#         self.showLab = Label(self.window, text="Phone:", bg="white", fg="green", font=("times new roman", 20, "bold"))
#         self.showLab.place(x=0, y=300, width=250)
#
#         self.showLab = Label(self.window, text=self.namdekha2[0][1], bg="white", fg="green",
#                              font=("times new roman", 20, "bold"))
#         self.showLab.place(x=325, y=300, width=250)
#
#         self.showLab = Label(self.window, text="Gender:", bg="white", fg="green", font=("times new roman", 20, "bold"))
#         self.showLab.place(x=0, y=350, width=250)
#
#         self.showLab = Label(self.window, text=self.namdekha2[0][2], bg="white", fg="green",
#                              font=("times new roman", 20, "bold"))
#         self.showLab.place(x=325, y=350, width=250)
#
#         self.showLab = Label(self.window, text="Address:", bg="white", fg="green", font=("times new roman", 20, "bold"))
#         self.showLab.place(x=0, y=400, width=250)
#
#         self.showLab = Label(self.window, text=self.namdekha2[0][3], bg="white", fg="green",
#                              font=("times new roman", 20, "bold"))
#         self.showLab.place(x=325, y=400, width=250)
#
#         self.e = Image.open('D:/downloads/project/RegistrantImages/'+ self.namdekha2[0][4]+"/"+"image."+self.namdekha2[0][0]+"."+"5"+".jpg")
#         self.resized = self.e.resize((90, 90), Image.ANTIALIAS)
#
#         # self.g = ImageTk.PhotoImage(file=self.resized)
#         # bb = Label(root, image="D:\\downloads\\project\\RegistrantImages\\" + "image" + "." + "111" + "." + "3" + ".jpg").place(x=10, y=30, height=300, width=300)
#         # c = "D:\\downloads\\project\\RegistrantImages\\"+"image"+ "." + str(111)+"."+"3"+".jpg"
#         self.g = ImageTk.PhotoImage(self.resized)
#
#         self.bb = Label(self.window, image=self.g).place(x=100, y=40)
#
#
#         # a = "D:\\downloads\\project\\RegistrantImages\\" +self.namdekha2[0][4].get()+"\\"+self.namdekha2[0][0].get()+"."+str(1)+".png"
#         # a = "D:\\downloads\\project\\RegistrantImages\\" +"image"+"."+"111"+"."+"3"+".jpg"
#         # e = Image.open('D:/downloads/project/RegistrantImages/laa/s.jpg')
#         # self.e = Image.open(self.a)
#         # self.resized = self.e.resize((90,90), Image.ANTIALIAS)
#         # self.g = ImageTk.PhotoImage(file=self.resized)
#         # bb = Label(self.window, image=a).place(x=10, y=30, height=300,width=600)
#
#
#
#         self.bttn_attendence = Button(self.window, activeforeground="Red", activebackground="White",
#                                       text="T a k e   A t t e n d e n c e", cursor="hand2", bg="White", borderwidth=0,
#                                       font=("times new roman", 15, "bold"), command=self.attendence)
#         self.bttn_attendence.place(x=650, y=550, width=300)
#
#         self.item_tree1 = ttk.Treeview(self.window, columns=('SN_NO', 'DATE', 'TIME'))
#         self.item_tree1.place(x=720, y=100, width=600, height=440)
#         self.item_tree1['show'] = 'headings'
#         self.item_tree1.column('SN_NO', anchor=CENTER,width=50)
#         self.item_tree1.column('DATE', anchor=CENTER, width=75)
#         self.item_tree1.column('TIME', anchor=CENTER, width=75)
#         # self.item_tree1.column('STD_ID', width=100)
#         # self.item_tree1.column('total_price', width=50)
#
#         self.item_tree1.heading('SN_NO', text="Serial No")
#         self.item_tree1.heading('DATE', text="Attend Date")
#         self.item_tree1.heading('TIME', text="Attend Time")
#         self.show_attendence_data()
#
#
#         # self.item_tree1.heading('STD_ID', text="Student ID")
#         # self.item_tree1.heading('total_price', text="Total_Price")
#
#     def show_attendence_data(self):
#         self.item_tree1.delete(*self.item_tree1.get_children())
#         data = self.infoattend.show_total_attendence(self.idforcam)
#         for i in data:
#             self.item_tree1.insert("", "end", text=i[0], value=(i[0], i[1], i[2]))
#
#     # Self.show_attendence_data()
#     # self.item_tree1.bind("<Double-1>", self.on_foods_select)
#
#     def attendence(self):
#         # self.infoattend.FindDate(int(10002457),self.date)
#         self.show_attendence_data()
#         self.infoattend.FindDate(self.idforcam, self.date)
#         self.attendcount = [self.infoattend.already]
#         # print(self.infoattend.datesss[0][0])
#         # print(self.date)
#         # print(self.date)
#
#         # if self.infoattend.datesss == "":
#         #     runboun()
#
#         # print(self.infoattend.datesss)
#         # print(self.infoattend.already)
#         # print(len(self.infoattend.already))
#         if len(self.infoattend.already) == 1:
#             self.runboun()
#             # self.infoattend.already.clear
#             self.infoattend.FindDate(int(10002457), self.date)
#
#         # if self.date not in self.infoattend.datesss:
#         #     self.runboun()
#         elif self.infoattend.datesss != "":
#             if str(self.date) == str(self.infoattend.datesss[0]):
#                 print(self.infoattend.datesss[0])
#                 messagebox.showerror("Error", "Attendence was already taken!")
#
#             # pass
#
#     def runboun(self):
#         def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
#             gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
#             for (x, y, w, h) in features:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
#                 id, pred = clf.predict(gray_img[y:y + h, x:x + w])
#                 confidence = int(100 * (1 - pred / 300))
#                 if confidence > 75:
#                     if id == int(self.idforcam):
#                         cv2.putText(img, self.nameforcam, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1,
#                                     cv2.LINE_AA)
#                         if cv2.waitKey(1) == 13:
#                             self.infoattend.Attendence(self.date, self.time, self.idforcam)
#                             messagebox.showinfo("Success", "Attendence taken successfully!")
#                             cv2.destroyAllWindows()
#                             vide_capture.release()
#                             cv2.destroyAllWindows()
#                             self.closecam.append(4)
#                             # vide_capture.release()
#                             # cv2.destroyAllWindows()
#                             # break
#
#                 else:
#                     cv2.putText(img, "UNKNOWN", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
#             return img
#
#         faceCascade = cv2.CascadeClassifier("D:\\downloads\\project\\CascadeFile\\haarcascade_frontalface_default.xml")
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.read(self.idforcam + ".xml")
#         vide_capture = cv2.VideoCapture(0)
#         while True:
#             ret, img = vide_capture.read()
#             img = draw_boundary(img, faceCascade, 1.3, 6, (255, 255, 255), "Face", clf)
#             cv2.imshow("Face Detection", img)
#             if 4 in self.closecam:
#                 vide_capture.release()
#                 cv2.destroyAllWindows()
#                 break
#             if cv2.waitKey(1) == 13:
#                 break
#         vide_capture.release()
#         cv2.destroyAllWindows()
#     # runboun()
#     # self.runbown()
#
# # def main():
# #     window = Tk()
# #     obj = Success(window)
# #     window.mainloop()
# # if __name__ == '__main__':
# #     main()