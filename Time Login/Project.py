import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Utilisateur:
    def __init__(self, login, mot_de_pass):
        self.__login = login
        self.__mot_de_pass = mot_de_pass

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, nvlogin):
        self.__login = nvlogin

    @property
    def mot_de_pass(self):
        return self.__mot_de_pass
    
    @mot_de_pass.setter
    def mot_de_pass(self, nvmot_de_pass):
        self.__mot_de_pass = nvmot_de_pass

    def verifier(self, login, mot_de_pass):
        return self.login == login and self.mot_de_pass == mot_de_pass


class AuthentificationSystem:
    def __init__(self):
        self.__liste_utilisateurs = []

    def ajouter_utilisateur(self, utilisateur):
        self.__liste_utilisateurs.append(utilisateur)

    def verifier_utilisateur(self, login, mot_de_pass):
        for utilisateur in self.__liste_utilisateurs:
            if utilisateur.verifier(login, mot_de_pass):
                return utilisateur
        return None

    def log_utilisateur(self, utilisateur, fichier):
        with open(fichier, 'a') as file:
            Time_Login = datetime.now().strftime("%H:%M:%S")
            Account = f"User : {utilisateur.login}, Mot de pass : {utilisateur.mot_de_pass} , Time Login:, {Time_Login} \n"
            file.write(Account)
        print(f"Logged to '{fichier}'")



root = tk.Tk()
root.title("Time Login")
root.geometry("400x200")

label_login = tk.Label(root, text="User:")
label_login.pack()
Test_login = tk.Entry(root)
Test_login.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()
Test_password = tk.Entry(root, show="*")
Test_password.pack()


u1 = Utilisateur('zakaria', 'password@123')
u2 = Utilisateur('anass', 'pasd901')
auth_sys = AuthentificationSystem()
auth_sys.ajouter_utilisateur(u1)
auth_sys.ajouter_utilisateur(u2)

def verify_and_save():
    login = Test_login.get()
    password = Test_password.get()
    utilisateur = auth_sys.verifier_utilisateur(login, password)
    if utilisateur:
        auth_sys.log_utilisateur(utilisateur, 'Project Time Login/Logs.csv')
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid login or password")

btn = tk.Button(root, text="Login", command=verify_and_save)
btn.pack()

root.mainloop()