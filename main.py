from tkinter import *

class Task:
    tasks = []
    def __init__(self):
        self.id = 0
        self.title = ''
        self.stats = 0
        #background color
        #gray
        self.a = '#2b303e'
        #blue
        self.c = '#181731'
        #green
        self.d = '#0C280F'
        #images
        self.task_bg = PhotoImage(file='./components/task_bg.png')
        self.task_bg2 = PhotoImage(file='./components/task_bg2.png')
        self.btn_delete = PhotoImage(file='./components/btn_delete.png')
        self.btn_uncheck = PhotoImage(file='./components/btn_update.png')
        self.btn_check = PhotoImage(file='./components/btn_check.png')

    def create_task(self, title, w, stats, color):
        if self.stats == 0:           
            #background
            self.task_frame = Label(w, image=stats, bg='#2B303E')
            self.task_frame.pack(pady=10)
            #delete button
            self.button_delete_frame = Button(self.task_frame, image=self.btn_delete, bg=color, bd=0, activebackground=color, command=self.destroy)
            self.button_delete_frame.place(x=610,y=25)
            #uncheck stats
            self.button_uncheck_frame = Button(self.task_frame, image=self.btn_uncheck, bg=color, bd=0, activebackground=color, command=self.uncheck)
            self.button_uncheck_frame.place(x=570,y=25)
            #check stats
            self.button_check_frame = Button(self.task_frame, image=self.btn_check, bg=color, bd=0, activebackground=color, command=self.check)
            self.button_check_frame.place(x=530,y=25)
            #task title
            self.title_label = Label(self.task_frame, text=title, fg='white', bg=color, font='17')
            self.title_label.place(x=200, y=27)

    def destroy(self):
        self.task_frame.destroy()
        print(self.id, self.title, self.stats)
        self.delete(self.id)

    def setDatas(self, id, title, stats):
        self.id = id
        self.title = title
        self.stats = stats

    def uncheck(self):
        if self.stats == 1:
            from sql import update_task_stats
            self.stats = 0
            self.task_frame.config(image=self.task_bg)
            self.button_delete_frame.config(bg='#181731', activebackground='#181731')
            self.button_uncheck_frame.config(bg='#181731', activebackground='#181731')
            self.button_check_frame.config(bg='#181731', activebackground='#181731')
            self.title_label.config(bg='#181731')
            print(self.stats)
            update_task_stats(self.id, 0)
    
    def check(self):
        if self.stats == 0:
            from sql import update_task_stats
            self.stats = 1
            self.task_frame.config(image=self.task_bg2)
            self.button_delete_frame.config(bg='#0C280F', activebackground='#0C280F')
            self.button_uncheck_frame.config(bg='#0C280F', activebackground='#0C280F')
            self.button_check_frame.config(bg='#0C280F', activebackground='#0C280F')
            self.title_label.config(bg='#0C280F')
            print(self.stats)
            update_task_stats(self.id, 1)
            
    def insert(self, title):
        from sql import insert_task
        insert_task(title, self.stats)

    def delete(self, task_id):
        from sql import delete_task
        delete_task(task_id)

    def get_all(self):
        from sql import get_all_tasks
        return get_all_tasks()

    def update_all_task(self):
        for i in self.get_all():
            self.data = Task.tasks
            self.data.append((i[0],i[1],i[2]))
        
    def get_list(self):
        print(Task.tasks)
        
class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("Task Manager")
        self.window.geometry("750x750")
        #self.window.resizable(0,0)
        self.window.configure(bg="#2B303E")
        self.window.minsize(width=750, height=750)
        #Default color
        self.cd = '#181731'
        self.c = '#2B303E'
        self.d = '#0C280F'
        self.create_header_content()
        self.create_content()
        self.t = Task()
        self.t.update_all_task()
        self.add()
        print(self.t.tasks)

    #1
    def create_header_content(self):
        self.header_content = Frame(self.window, height=6, bg=self.c)
        self.header_content.pack(fill=X)

        self.box_components = Label(self.header_content, width=50, height=5, bg=self.c)
        self.box_components.pack()

        self.box_label_left = Label(self.box_components, text='Task', fg='white', bg=self.c)
        self.box_label_left.place(x=0, y=35)

        self.box_bottom_center_img = PhotoImage(file='./components/center_button.png')
        self.box_bottom_center = Button(self.box_components, image=self.box_bottom_center_img, border=0, background=self.c, activebackground=self.c, cursor='hand2', command=self.create_input_content)
        self.box_bottom_center.place(x=150, y=20)

        self.box_label_right = Label(self.box_components, text='Manager', fg='white', bg=self.c)
        self.box_label_right.place(x=299, y=35)

    def create_input_content(self):
        self.box_bottom_center.config(state=DISABLED)

        self.input_label_image = PhotoImage(file='./components/input_bg.png')
        self.input_label = Label(self.window, bg=self.c, image=self.input_label_image)
        self.input_label.pack()

        self.input_entry = Entry(self.input_label, bg='white', font='Arial 12', bd=0)
        self.input_entry.place(x=54, y=87, width=560, height=40)

        self.input_button_confirm_image = PhotoImage(file='./components/input_confirm.png')
        self.input_button_confirm = Button(self.input_label, image=self.input_button_confirm_image, activebackground='#181731', bd=0, bg='#181731', command=self.confirm_input)
        self.input_button_confirm.place(x=200, y=155)

        self.input_button_cancel_image = PhotoImage(file='./components/input_cancel.png')
        self.input_button_cancel = Button(self.input_label, image=self.input_button_cancel_image, activebackground='#181731', bd=0, bg='#181731', command=self.hidde_input)
        self.input_button_cancel.place(x=350, y=155)

    def hidde_input(self):
        self.input_label.pack_forget()
        self.box_bottom_center.config(state=NORMAL)

    def confirm_input(self):
        self.task = Task()
        self.task.insert(self.input_entry.get())
        self.task.create_task(self.input_entry.get(), self.main_frame, self.task_bg, self.cd)
        self.input_label.pack_forget()
        self.box_bottom_center.config(state=NORMAL)
        
    def create_content(self):
        self.main_content = Frame(self.window, bg=self.c)
        self.main_content.pack(fill=Y, expand=1)

        self.canvas = Canvas(self.main_content, bg=self.c, highlightbackground=self.c, width=700)
        self.canvas.pack(side=LEFT, fill=Y, expand=1)

        self.scrollbar = Scrollbar(self.main_content, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))

        self.main_frame = Frame(self.canvas, bg=self.c)
        self.canvas.create_window((0,0), window=self.main_frame, anchor="nw")

    def add(self):
        self.task_bg2 = PhotoImage(file='./components/task_bg2.png')
        self.task_bg = PhotoImage(file='./components/task_bg.png')
        for i in Task.tasks:
            self.task = Task()
            if i[2] == 1:
                self.task.create_task(i[1], self.main_frame, self.task_bg2, self.d)
            else:
                self.task.create_task(i[1], self.main_frame, self.task_bg, self.cd)
            self.task.setDatas(i[0], i[1], i[2])
    
if __name__ == "__main__":
    app = App()
    app.window.mainloop()