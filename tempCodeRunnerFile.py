ab = b'X\\xc2\\xad\\xb1\\xf0t\\xaf\\x0f?\\x8b\\xa3\\xcb+.m\\xa2\\xe1\\xe1\\x99Q\\xf7J-h\\x83\\xf4\\xa2\\x93\\xf2\\nA'
val = b'x'
vvv = b'v'
if val in ab:
    # print("HOHO")
    ab.replace(val,vvv)
    print(ab)
# for val in ab:
#     ab.replace(val,vvv)
# # for val in ab:
#     ab.replace(val,vvv)
#     print(ab)


#
#
#
# # def main():
# #     window = Tk()
#
#
# from tkinter import *
# from PIL import ImageTk, Image
#
# root = Tk()
# root.title("ss")
# root.geometry("800x780")
#
# # a = "D:\\downloads\\project\\RegistrantImages\\" + "image" + "." + "111" + "." + "3" + ".jpg"
# f = 'laa/s.jpg'
# e = Image.open('D:/downloads/project/RegistrantImages/f')
#
# resized = e.resize((90,90), Image.ANTIALIAS)
#
# # self.g = ImageTk.PhotoImage(file=self.resized)
# # bb = Label(root, image="D:\\downloads\\project\\RegistrantImages\\" + "image" + "." + "111" + "." + "3" + ".jpg").place(x=10, y=30, height=300, width=300)
# # c = "D:\\downloads\\project\\RegistrantImages\\"+"image"+ "." + str(111)+"."+"3"+".jpg"
# g = ImageTk.PhotoImage(resized)
#
# bb = Label(root, image=g).place(x=80, y=30)
#
# # my = Image.open(c)
# # r = my.resize((300,300), Image.ANTIALIAS)
# # mi = ImageTk.PhotoImage(file="c")
# # l = Label(root, image=mi, height = 300, width=225).place(x = 30, y=30)
#
# root.mainloop()
#
