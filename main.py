import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('YTSampyler')
        self.geometry("720x450")
        self.iconbitmap('images/icon.ico')
        self.resizable(width=False, height=False)

        # Grids
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # Widgets
        self.logo = customtkinter.CTkLabel(self, text='YTSampyler')
        self.logo.grid(row = 0, column = 0, sticky='ew')

        self.linkField = customtkinter.CTkEntry(self, placeholder_text='Insira o link')
        self.linkField.grid(row=0, column = 2, sticky='ew')

        self.submitButton = customtkinter.CTkButton(self, text='Submit', command=self.submit)
        self.submitButton.grid(row=0, column = 3)

        self.templateThumbnail = customtkinter.CTkImage(
                                   light_image=Image.open('images/template.png'), 
                                   dark_image=Image.open('images/template.png'),
                                   size=(170, 170))
        self.thumbnail = customtkinter.CTkLabel(self, text='', image=self.templateThumbnail)
        self.thumbnail.grid(row=1, column = 0, columnspan = 2)

    # Funções
    def submit(self):
        print('teste') # debug
        pass

app = App()
app.mainloop()