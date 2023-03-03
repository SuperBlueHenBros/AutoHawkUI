import tkinter as tk
import tkinter.messagebox
import customtkinter as ct
from PIL import Image    #Pillow
from GUIStats import * 

import GUIStats

#System settings
ct.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"




#Class for the app
class Home(ct.CTk):
    #Class building the actual window and functions for AutoHawk
    
    def __init__(self,count):
        super().__init__()
        self.count = 1
        self.clicked = 0


        #Making the GUI

        # configure window
        self.title("AutoHawk")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.build_text()

        #Side Bar for options
        self.sidebar_frame = ct.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = ct.CTkLabel(self.sidebar_frame, text="Tabs", font=ct.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.sidebar_button_1 = ct.CTkButton(self.sidebar_frame, text = "About Us", command=self.sidebar_button_home)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ct.CTkButton(self.sidebar_frame, text = "Games", command=self.sidebar_button_game)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)



    #Building fucntions
    def build_text(self):
        #Function that builds the main entry front page

        self.textbox = ct.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        #Input for Text box
        intro = open("Intro.txt", 'r')
        self.textbox.insert("0.0",intro.read())
        self.textbox.configure(state = tk.DISABLED)

    def build_games(self):
        #Function that builds the games display with buttons

        self.game_frame =  ct.CTkFrame(self, width = 250, corner_radius=0)
        self.game_frame.grid(row = 0, column = 1, rowspan = 4, sticky = "nsew")

        self.game_btn1 = self.button(GUIStats.excitebike)
        self.game_btn1.grid(row = 1, column = 1, padx = 20, pady = 10)
        


        self.game_btn2 = self.button(GUIStats.metro)
        self.game_btn2.grid(row = 1, column = 2, padx = 20, pady = 10)
        



    #Button functions
    def sidebar_button_home(self):
        #Function to build the side bar for each game

        if (self.count == 0):
            #Add a delete for the games here
            self.delete_games()
            if(self.clicked == 1):
                self.delete_game_bar()
                self.clicked = 0
            self.build_text()
            self.count = 1
            

    def sidebar_button_game(self):
        #Function that builds the text box for the sidebar

        if( self.count == 1):
            self.textbox.configure(state = tk.NORMAL)
            #self.textbox.delete("1.0",tk.END)
            self.textbox.destroy()
            self.build_games()
            self.count = 0
    

    #Making the button
    def button(self,stats):
        #Function that builds the button need to change to a class
           
        self.game = stats[0]
        self.path = stats[1]
        self.img = stats[2]
        self.stats = stats[3]
        

        self.size = 150


        #Need to change button to class and change in the app with .configure
        img =ct.CTkImage(light_image = Image.open(self.img),size=(self.size,self.size))
        return ct.CTkButton(master=self.game_frame, text = "", image = img, command=self.game_button)

    #Button Helpers
    def get_imgpath(self): return self.img
    def get_game(self): return self.game 
    def get_path(self): return self.path
    def get_attempt(self): 
        print(self.stats)
        return  self.stats


    #Button Functions
    def game_button(self):
        #Opens the side bar for each button
        if(self.clicked == 1):
            self.delete_game_bar()
        self.clicked = 1
        self.game_bar_frame = ct.CTkFrame(self, width = 400)
        self.game_bar_frame.grid(row=0, column=4, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.label_gamebar_group = ct.CTkLabel(master=self.game_bar_frame, text="Game Stats:")
        self.label_gamebar_group.grid(row=0, column=4, columnspan=1, padx=10, pady=10, sticky="")
        
        self.gametext = ct.CTkEntry(master=self.game_bar_frame)
        self.gametext.grid(row = 1, column = 4, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.gametext.insert('1',self.get_attempt())
        self.gametext.configure(state = tk.DISABLED)


        self.label_gamebar_group = ct.CTkLabel(master=self.game_bar_frame, text="Attempts:")
        self.label_gamebar_group.grid(row=2, column=4, columnspan=1, padx=10, pady=10, sticky="")

        self.attempt_text = ct.CTkEntry(master=self.game_bar_frame)
        self.attempt_text.grid(row = 3, column = 4, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.attempt_text.insert('1',self.get_attempt())
        self.attempt_text.configure(state = tk.DISABLED)


    #Deletes
    def delete_game_bar(self):
        #Deletes the game side bar
        self.gametext.configure(state = tk.NORMAL)
        self.game_bar_frame.destroy()
    
    def delete_games(self):
        #Deletes the game buttons themself
        self.game_btn1.destroy()
        self.game_btn2.destroy()

        

            

        



if __name__ == "__main__":
    app = Home(1)
    app.mainloop()