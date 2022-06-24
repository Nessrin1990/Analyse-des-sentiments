from tkinter import *

import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import webbrowser
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# =================================================class Window1===================================================


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title(" Authentification")
        self.master.geometry("800x800")
        self.master.config(bg='black')

        self.frame = Frame(self.master, bg='grey')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text=' Authentification', font=('timenewroman', 30, 'bold'), bg='grey',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40)
        # ====================================================================================================
        self.LoginFrame1 = LabelFrame(self.frame, width=1000, height=600
                                      , font=('arial', 20), relief='ridge', bg='grey', bd=20)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1000, height=600
                                      , font=('arial', 20), relief='ridge', bg='grey', bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        # ==============================Label And Entry=======================================================
        self.lblUsername = Label(self.LoginFrame1, text='Nom', font=('arial', 10), bd=22,
                                 bg='grey')
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.LoginFrame1, font=('arial', 20, 'bold'), textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.LoginFrame1, text='Mot_de_passe', font=('arial', 10, 'bold'), bd=22,
                                 bg='grey')
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.LoginFrame1, font=('arial', 20, 'bold'), show='*', textvariable=self.Password)
        self.txtPassword.grid(row=1, column=1)

        # ==============================Buttons===============================================================

        self.btnLogin = Button(self.LoginFrame2, text='Entrer', width=17, font=('arial', 20, 'bold'),
                               command=self.Login_System)
        self.btnLogin.grid(row=3, column=0)

        # ==============================Buttons===========================================================

    def Login_System(self):
        if (self.Username.get() == "nesrine" and self.Password.get() == "SINT"):
            self.Login_System = tkinter.messagebox.askyesno("Login correct")
            self.newWindow = Toplevel(self.master)
            self.app = Windows2(self.newWindow)
            if self.Login_System > 0:
                self.master.destroy()
                command = self.new_window

            else:
                command = ""
                return



        else:
            tkinter.messagebox.askyesno("Login incorrect ")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()



    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Windows2(self.newWindow)


################==============================================class Window2==================================##############################

class Windows2():
    def __init__(self, master):
        self.master = Tk()
        self.master.title("My Application")
        self.master.geometry('1350x750+0+0')
        self.master.minsize(480, 360)
        # self.window.iconbitmap("logo.ico")
        self.master.config(background='black')

        # initialization des composants
        self.frame = Frame(self.master, bg='grey')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()

        self.create__button()
        self.create__button1()

    def create_title(self):
        label_title = Label(self.frame, text="Bienvenue sur l'application", font=("Courrier", 40), bg='white',
                            fg='grey')
        label_title.pack()


    def create__button(self):
        yt_button = Button(self.frame, text="Scrapping commentaire de site youtube ", font=("Courrier", 25), bg='white',
                           fg='grey',
                           command=self.open)
        yt_button.pack(pady=25, fill=X)

    def create__button1(self):
        yt1_button = Button(self.frame, text="programme en PYTHON", font=("Courrier", 25), bg='white', fg='grey',
                            command=self.open1)
        yt1_button.pack(pady=25, fill=X)

    def open(self):
        self.newWindow = Toplevel(self.master)
        self.app = MyApp(self.newWindow)
        self.master.destroy()

    def open1(self):
        self.newWindow = Toplevel(self.master)
        self.app = Windows3(self.newWindow)
        self.master.destroy()

        #####################========================================class MyApp================################################


class MyApp:

    def __init__(self, master):

        self.master = Tk()
        self.master.title("Projet fouille des données ")
        self.master.geometry('1350x750+0+0')
        self.master.minsize(480, 360)
        # self.window.iconbitmap("logo.ico")
        self.master.config(background='white')

        # initialization des composants
        self.frame = Frame(self.master, bg='grey')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()

        self.create__button()
        self.create__button2()

    def create_title(self):
        label_title = Label(self.frame, text="Entrer page youtube ", font=("Courrier", 40), bg='black',
                            fg='white')
        label_title.pack()


    def create__button(self):
        yt_button = Button(self.frame, text="projet fouille des données ", font=("Courrier", 25), bg='white',
                           fg='grey',
                           command=self.open_expose)
        yt_button.pack(pady=25, fill=X)

    def create__button2(self):
        yt1_button = Button(self.frame, text="Quitter", font=("Courrier", 25), bg='white', fg='grey',
                            command=self.quitter)
        yt1_button.pack(pady=25, fill=X)

    def open_expose(self):
        # webbrowser.open_new("https://docs.google.com/presentation/d/1sKhLgRPE2R7AnFQ7AWdhGTlUM28YLQAONPHb_2xN5V0/edit")
        data = []

        with Chrome(executable_path=r'D:\master\fouille\chromedriver_win32\chromedriver') as driver:
            wait = WebDriverWait(driver, 15)
            driver.get("https://www.youtube.com/watch?v=2Q78XXkhx0o&t=51s")
            for item in range(50):
                wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
                time.sleep(15)
            for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
                data.append(comment.text)
        df = pd.DataFrame(data, columns=['comment'])
        df.head()
        df.to_csv(r'C:\Users\DELL\Desktop\commentaires.csv', index=False, header=True)
        print(df)

    def quitter(self):
        self.newWindow = Toplevel(self.master)
        self.app = Windows2(self.newWindow)
        self.master.destroy()


# ======================================================================class windows3====================================#
class Windows3:

    def __init__(self, master):
        self.master = Tk()
        self.master.title("Programme en python")
        self.master.geometry('1350x750+0+0')
        self.master.minsize(480, 360)
        self.master.config(background='grey')

        # initialization des composants
        self.frame = Frame(self.master, bg='grey')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()

        self.create__button()
        self.create__button1()

    def create_title(self):
        label_title = Label(self.frame, text="Programme en PYTHON", font=("Courrier", 40), bg='black',
                            fg='white')
        label_title.pack()



    def create__button(self):
        yt2_button = Button(self.frame, text="Programme en PYTHON", font=("Courrier", 25), bg='white', fg='grey',
                            command=self.open_prog)
        yt2_button.pack(pady=25, fill=X)

    def create__button1(self):
        yt2_button = Button(self.frame, text="Quitter", font=("Courrier", 25), bg='white', fg='grey',
                            command=self.quitter)
        yt2_button.pack(pady=25, fill=X)

    def open_prog(self):
        webbrowser.open_new("http://localhost:8888/notebooks/scrape%20comment%20youtube%20.ipynb")

    def quitter(self):
        self.newWindow = Toplevel(self.master)
        self.app = Windows2(self.newWindow)
        self.master.destroy()


# =========================================================  main ============================================#
if __name__ == '__main__':
    root = Tk()
    app = Window1(root)
    root.mainloop()
