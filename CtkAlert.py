import customtkinter as ctk
import winsound

def CtkMessage(parent, name, desc):
    alert = ctk.CTkToplevel(parent) 
    alert.title(name)
    alert.geometry("250x160")
    alert.resizable(False, False)
    alert.attributes("-topmost", True)
    ctk.CTkLabel(alert, text=str(desc)).pack(pady=20)
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    alert.wait_window()

def CtkQuestion(parent, name, desc, opt1, opt2):
    question = ctk.CTkToplevel(parent) 
    question.title(name)
    question.geometry("250x160")
    question.resizable(False, False)
    question.attributes("-topmost", True)
    question.choice = None

    def select_option(res):
        question.choice = res
        question.destroy()

    ctk.CTkLabel(question, text=str(desc)).pack(pady=20)
    ctk.CTkButton(question, text=str(opt1), width=90, 
                  command=lambda: select_option(opt1)).place(x=25, y=110)
    ctk.CTkButton(question, text=str(opt2), width=90, 
                  command=lambda: select_option(opt2)).place(x=135, y=110)
    
    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
    question.wait_window()
    return question.choice