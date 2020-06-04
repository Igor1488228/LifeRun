from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry("300x500")
root.title("Войти в систему")

def registration():
    text = Label(text="Для входа в систему - зарегистрируйтесь !")
    text_fn = Label(text="Ваше имя")
    registr_fn = Entry()
    text_ln = Label(text="Ваша фамилия")
    registr_ln = Entry()
    text_role = Label(text="Роль")
    registr_role = Entry()
    text_email = Label(text="Почта")
    registr_email = Entry()
    text_log = Label(text="Введите Ваш логин")
    registr_lodin = Entry()
    text_password1 = Label(text="Введите Ваш пароль")
    registr_password1 = Entry()
    text_password2 = Label(text="Ещё раз пароль")
    registr_password2 = Entry(show="*")
    button_registr = Button(text="Зарегистрироваться", command=lambda: save())
    text.pack()
    text_fn.pack()
    registr_fn.pack()
    text_ln.pack()
    registr_ln.pack()
    text_role.pack()
    registr_role.pack()
    text_email.pack()
    registr_email.pack()
    text_log.pack()
    registr_lodin.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()

    def save():
        login_pass_save = {}
        login_pass_save[registr_lodin.get()]=registr_password1.get()
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()


def login():
    text_log = Label(text="Поздравляем! Теперь Вы можете войти в систему !")
    text_enter_login = Label(text="Введите Ваш логин:")
    enter_login = Entry()
    text_enter_pass = Label(text="Введите Ваш пароль:")
    enter_password = Entry(show="*")
    button_enter = Button(text="Войти", command=lambda: log_pass())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_password.pack()
    button_enter.pack()

    def log_pass():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() == a[enter_login.get()]:
                messagebox.showinfo("Вход выполнен", "Привет !")
            else:
                messagebox.showerror("Ошибка", "Вы ввели неверный логи или пароль")
        else:
            messagebox.showerror("Ошибка!", "Неверный логин!")

registration()

root.mainloop()
