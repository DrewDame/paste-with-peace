import customtkinter as ctk
import json
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme('blue')

class SettingsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Paste with Peace")
        self.geometry("700x400")  # Fixed typo
        self.resizable(True, True)  # Fixed typo

        # Layout: Sidebar left, content right

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_main_area()

    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=160)
        self.sidebar.grid(row=0, column=0, sticky='ns')
        self.sidebar.grid_propagate(False)

        ctk.CTkLabel(self.sidebar, text="Paste with Peace", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(20, 10))

        self.nav_buttons = {
            "Settings": ctk.CTkButton(self.sidebar, text="Settings", command=lambda: self.show_page("Settings")),
            "Apps": ctk.CTkButton(self.sidebar, text="Apps", command=lambda: self.show_page("Apps")),
            "About": ctk.CTkButton(self.sidebar, text="About", command=lambda: self.show_page("About")),
        }

        for btn in self.nav_buttons.values():
            btn.pack(fill="x", padx=10, pady=5)

    def create_main_area(self):
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        self.current_page = None
        self.show_page("Settings")

    def show_page(self, name):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.main_frame, text=f"{name} Page", font=ctk.CTkFont(size=18)).pack(pady=30)

def launch_settings_ui():
    app = SettingsApp()
    app.mainloop()

if __name__ == "__main__":
    launch_settings_ui()