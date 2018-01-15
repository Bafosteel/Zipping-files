import zipfile as ziph
from os import path
from tkinter import *
from tkinter import filedialog
from os import listdir, path
class Gui(Toplevel):
    def __init__(self, parent, title="Обработка файлов"):
        Toplevel.__init__(self, parent)
        parent.geometry("250x250+100+150")
        if title:
            self.title(title)
        parent.withdraw()
        self.parent = parent
        self.result = None
        dialog = Frame(self)
        self.initial_focus = self.dialog(dialog)
        self.protocol("WM_DELETE_WINDOW", self.on_exit)
        dialog.pack()

    def on_exit(self):
        self.quit()

    def text_3_on(self):
        if self.var_1.get():
            self.text_3["state"] = "normal"
            self.text_3.delete(0, END)
            self.text_3.insert(END, "address.jpg")
        else:
            self.text_3["state"] = "disabled"

    def text_5_on(self):
        if self.var_2.get():
            self.text_5["state"] = "normal"
            self.text_5.delete(0, END)
            self.text_5.insert(END, "Name_{{initial_image_name}}")
        else:
            self.text_5["state"] = "disabled"

    def search_folder_for_files(self):
        path_to = filedialog.askdirectory()
        print(path_to)
        self.text_1.delete(0, END)
        self.text_1.insert(END, path_to)

    def search_folder_for_images(self):
        path_to = filedialog.askdirectory()
        print(path_to)
        self.text_2.delete(0, END)
        self.text_2.insert(END, path_to)

    def search_folder_for_zip(self):
        path_to = filedialog.askdirectory()
        print(path_to)
        self.text_4.delete(0, END)
        self.text_4.insert(END, path_to)

    def start(self):
        print()
        print(listdir(self.text_1.get()))
        print(listdir(self.text_2.get()))
        print(listdir(self.text_4.get()))

    # Создадим массив имен архивов
        name = []
        for i in range(0, len(listdir(self.text_2.get()))):
            name.append(str(self.text_5.get())+"_"+str(i+1))


        for i in range(0,len(listdir(self.text_2.get()))):
            # Создает архив
            newzip = ziph.ZipFile(str(self.text_4.get().replace('/', '\\')) + '\\' + str(name[i]) + '.zip', 'w',
                                  ziph.ZIP_LZMA)
            # Берет все элементы
            for item in listdir(self.text_1.get()):
                newzip.write(str(self.text_1.get().replace('/', '\\')) + '\\' + str(item), str(item))

            # Берет по одному элементу
            if self.var_1.get():
                if ".jpg" in listdir(self.text_2.get())[i]:
                    newzip.write(str(self.text_2.get()).replace('/', '\\') + "\\" + str(listdir(self.text_2.get())[i]),
                                 str(self.text_3.get()))
                else:
                    newzip.write(str(self.text_2.get().replace('/', '\\')) + '\\' + str(listdir(self.text_2.get())[i]),
                                 str(listdir(self.text_2.get())[i]))
            else:
                newzip.write(str(self.text_2.get().replace('/', '\\'))+'\\'+str(listdir(self.text_2.get())[i]),
                         str(listdir(self.text_2.get())[i]))

        newzip.close()

        import ctypes
        message = 'Готово!'
        ctypes.windll.user32.MessageBoxW(0, message, 'Обработка файлов', 0)
        print('ok')


    def dialog(self, parent):
        self.parent = parent

        # Created main elements
        self.label_1 = Label(parent, text="Укажите папку, в которой лежат основные файлы")
        self.text_1 = Entry(parent, width=50)
        self.but_1 = Button(parent, text="Указать", command=self.search_folder_for_files)

        self.label_2 = Label(parent, text="Укажите папку, где лежат изображения, которые нужно разложить")
        self.text_2 = Entry(parent, width=50)
        self.but_2 = Button(parent, text="Указать", command=self.search_folder_for_images)

        self.var_1 = IntVar()
        self.var_2 = IntVar()
        self.text_3 = Entry(parent, width=50, state=DISABLED, disabledforeground=parent.cget('bg'))
        self.chk_1 = Checkbutton(parent, text="Переименовать изображения при копировании в:", variable=self.var_1, command=self.text_3_on)


        self.label_3 = Label(parent, text="Укажие папку, куда сложить финальные файлы zip")
        self.text_4 = Entry(parent, width=50)
        self.but_3 = Button(parent, text="Указать", command=self.search_folder_for_zip)

        self.chk_2 = Checkbutton(parent, text="Переименовать zip архивы по маске", variable=self.var_2, command=self.text_5_on)
        self.text_5 = Entry(parent, width=50, state=DISABLED, disabledforeground=parent.cget('bg'))

        self.label_1.pack()
        self.text_1.pack()
        self.but_1.pack()

        self.label_2.pack()
        self.text_2.pack()
        self.but_2.pack()

        self.chk_1.pack()
        self.text_3.pack()

        self.label_3.pack()
        self.text_4.pack()
        self.but_3.pack()

        self.chk_2.pack()
        self.text_5.pack()

        # start button
        self.but_start = Button(parent, text="Выполнить",command=self.start)
        self.but_start.pack()


if __name__ == "__main__":
    root = Tk()
    root.minsize(width=500, height=400)
    gui = Gui(root)
    root.mainloop()