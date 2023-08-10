import tkinter as tk
import customtkinter as ctK
from tkinter import messagebox
from PIL import Image
import os

ctK.set_appearance_mode("dark")


class Login (ctK.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("App Music Diversion")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctK.CTkImage(Image.open(current_path + "/images/bg_gradient.jpg"), size=(self.width, self.height))
        self.bg_image_label = ctK.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = ctK.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        
        self.login_label = ctK.CTkLabel(self.login_frame, text="Bienvenidos\nA la Diversion",
        font=ctK.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        # crea botones traslucidos
        self.username_entry = ctK.CTkEntry(self.login_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        
        self.password_entry = ctK.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        """ aca inicia el llamado a otra pantalla ___resgistro o verificacion de usuario"""
        # desde aca inicia la verificacion de usuario
        self.login_button = ctK.CTkButton(self.login_frame, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        #
        # aca tengo que importar registro
        # desde aca inicia el registro de usuario
        self.login_button = ctK.CTkButton(self.login_frame, text="Registrate", command=self.registro_event, width=200)
        self.login_button.grid(row=4, column=0, padx=30, pady=(15, 15))

        # create main frame 2 pantalla
        self.main_frame = ctK.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_label = ctK.CTkLabel(self.main_frame, text="Bienvenido al Mundo\nde la Maxima Musica",font=ctK.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        self.back_button = ctK.CTkButton(self.main_frame, text="Back", command=self.back_event, width=200)
        self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))
     # solicita datos de acceso   
    def login_event(self):
        print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())
        self.login_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame
    # inicia registro de usuario
    def registro_event(self):
        self.main_frame.grid_forget()  # remove main frame
        print (" deberia empezar el registro")
        self.login_frame = ctK.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        
        self.login_label = ctK.CTkLabel(self.login_frame, text="Inicia tu Aventura\n El camino es nuestro",
        font=ctK.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        
        self.firstname_entry = ctK.CTkEntry(self.login_frame, width=200, placeholder_text="¿Cual es tu nombre?")
        self.firstname_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        
        self.lastname_entry = ctK.CTkEntry(self.login_frame, width=200, placeholder_text="Dinos tu Apellido !!")
        self.lastname_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        
        self.password_entry = ctK.CTkEntry(self.login_frame, width=200,show="*", placeholder_text="Tu palabra clave")
        self.password_entry.grid(row=3, column=0, padx=30, pady=(15, 15))

        self.repassword_entry = ctK.CTkEntry(self.login_frame, width=200,show="*", placeholder_text="repitela")
        self.repassword_entry.grid(row=4, column=0, padx=30, pady=(15, 15))
        
        #self.login_button = ctK.CTkButton(self.login_frame, text="re Login", command=self.login_password, width=200)
        #self.login_button.grid(row=6, column=0, padx=30, pady=(15, 15))
        
        self.login_button = ctK.CTkButton(self.login_frame, text="Bienvenido", command=self.login_event, width=200)
        self.login_button.grid(row=5, column=0, padx=30, pady=(15, 15))
        
    
     
     # cierra la ventana y abre otra
    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame
  

if __name__ == "__main__":
    app = Login()
    app.mainloop()
