import customtkinter as CTK
from tkinter import CENTER  
from threading import Thread
from PIL import Image, ImageTk

def main():
    def LoadFrame_anim():
        while True:
            anim_label.configure(image0)
            anim_label.configure(image1)
            anim_label.configure(image2)
            anim_label.configure(image3)
            anim_label.configure(image4)
            anim_label.configure(image5)
            anim_label.configure(image6)

    MainWindow = CTK.CTk()
    MainWindow.geometry("300x768")

    #frames------------------------------------
    LoadFrame = CTK.CTkFrame(master=MainWindow, width=300, height=768)
    LoadFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    SystemFrame = CTK.CTkFrame(master=MainWindow, width=300, height=768)
    OptionsFrame = CTK.CTkFrame(master=MainWindow, width=300, height=768)

    #helps dir---------------------------------
    dir_anim = "/Users/admin/Downloads/Anim_load.png/"

#animation load frame--------------------------
    #anim_image--------------------------------
    image0 = ImageTk.PhotoImage(Image.open(dir_anim + "0.png"))
    image1 = ImageTk.PhotoImage(Image.open(dir_anim + "1.png"))
    image2 = ImageTk.PhotoImage(Image.open(dir_anim + "2.png"))
    image3 = ImageTk.PhotoImage(Image.open(dir_anim + "3.png"))
    image4 = ImageTk.PhotoImage(Image.open(dir_anim + "4.png"))
    image5 = ImageTk.PhotoImage(Image.open(dir_anim + "5.png"))
    image6 = ImageTk.PhotoImage(Image.open(dir_anim + "6.png"))

    #anim_label-------------------------------
    anim_label = CTK.CTkLabel(master=LoadFrame, image=image0, text="", width=50, height=50)
    anim_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    t1 = Thread(target=LoadFrame_anim)
    t1.run()

    MainWindow.mainloop()

if __name__ == "__main__":
    main()