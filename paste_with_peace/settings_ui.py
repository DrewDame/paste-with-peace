import customtkinter as ctk
import json
import os
import sys
from CTkMessagebox import CTkMessagebox

CONFIG_PATH = 'config.json'
ctk.set_appearance_mode("System")
ctk.set_default_color_theme('blue')

def load_config():
    """Loads and returns config file. Returns empty json if config file not found"""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    print(f"Could not find config file at {CONFIG_PATH}", file=sys.stderr)
    return {}

class SettingsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Paste with Peace")
        self.geometry("1000x700")  # Fixed typo
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

        if name == "Settings":
            self.build_settings_page()
        if name == "Apps":
            self.build_apps_page()
        else:
            ctk.CTkLabel(self.main_frame, text=f"{name} Page", font=ctk.CTkFont(size=18)).pack(pady=30)
    
    def build_settings_page(self):
        config = load_config()

        content = ctk.CTkFrame(self.main_frame)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        content.grid_columnconfigure(1, weight=1)

        font_title = ctk.CTkFont(size=14, weight='bold')
        font_desc = ctk.CTkFont(size=11)

        row = 0

        def section_header(text):
            nonlocal row
            ctk.CTkLabel(content, text=text, font=ctk.CTkFont(size=16, weight="bold")).grid(
                row=row, column=0, columnspan=2, sticky="w", pady=(15, 5)
            )
            row += 1

        def setting(label, desc, widget):
            nonlocal row
            ctk.CTkLabel(content, text=label, font=font_title).grid(row=row, column=0, sticky="w", padx=(0, 10))
            widget.grid(row=row, column=1, sticky="ew")
            row += 1
            ctk.CTkLabel(content, text=desc, font=font_desc, text_color="gray").grid(
                row=row, column=0, columnspan=2, sticky="w", padx=(0, 10), pady=(0, 5)
            )
            row += 1

         # --- System Tray ---
        section_header("System Tray")
        self.allow_user_quit_var = ctk.StringVar(value="Enabled" if config.get("allow_user_quit", True) else "Disabled")
        allow_quit_menu = ctk.CTkOptionMenu(content, variable=self.allow_user_quit_var, values=["Enabled", "Disabled"])
        setting("Allow Quit from Tray", "Controls whether users can exit the app via the tray icon.", allow_quit_menu)

        # --- Popups ---
        section_header("Popups")
        self.popup_timeout_var = ctk.StringVar(value=str(config.get("popup_timeout", 5) * 1000))
        popup_entry = ctk.CTkEntry(content, textvariable=self.popup_timeout_var, placeholder_text="5000")
        setting("Popup Timeout", "How long popups stay on screen (in milliseconds, 0 to 50,000).", popup_entry)

        # --- App Behavior ---
        section_header("App Behavior")
        self.clear_after_paste_var = ctk.StringVar(value="Enabled" if config.get("clear_after_paste", True) else "Disabled")
        clear_paste_menu = ctk.CTkOptionMenu(content, variable=self.clear_after_paste_var, values=["Enabled", "Disabled"])
        setting("Clear After Paste", "Deletes pasted secrets in Slack with backspace automation.", clear_paste_menu)

        # --- Logging ---
        section_header("Logging")
        self.logging_enabled_var = ctk.StringVar(value="Enabled" if config.get("logging_enabled", True) else "Disabled")
        logging_menu = ctk.CTkOptionMenu(content, variable=self.logging_enabled_var, values=["Enabled", "Disabled"])
        setting("Enable Logging", "Save detection events to a local log file.", logging_menu)

        self.redact_mode_var = ctk.StringVar(value=config.get("redact_mode", "Masked").capitalize())
        redact_menu = ctk.CTkOptionMenu(content, variable=self.redact_mode_var, values=["Masked", "Hash", "Unchanged", "Redacted"])
        setting("Redact Mode", "How secrets appear in logs: Masked, Hashed, Plain, or Redacted.", redact_menu)

        self.log_file_path_var = ctk.StringVar(value=config.get("log_file_path", "logs/detection_log.txt"))
        log_path_entry = ctk.CTkEntry(content, textvariable=self.log_file_path_var, placeholder_text="logs/detection_log.txt")
        setting("Log File Path", "Where to save logs if logging is enabled.", log_path_entry)

        ctk.CTkButton(
            self.main_frame,
            text="Save Settings",
            command=self.save_settings
        ).pack(pady=15)

        ctk.CTkButton(
            self.main_frame,
            text="Restart App",
            fg_color="gray30",
            command=self.restart_app
        ).pack(pady=(0,5))

    def build_apps_page(self):
        config = load_config()
        enabled_apps = config.get("enabled_apps", {})
        slack_enabled = enabled_apps.get("slack", True)

        content = ctk.CTkFrame(self.main_frame)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        content.grid_columnconfigure(1, weight=1)

        font_title = ctk.CTkFont(size=14, weight="bold")
        font_desc = ctk.CTkFont(size=11)

        row = 0
        def setting(label, desc, widget):
            nonlocal row
            ctk.CTkLabel(content, text=label, font=font_title).grid(row=row, column=0, sticky="w", padx=(0, 10))
            widget.grid(row=row, column=1, sticky="ew")
            row += 1
            ctk.CTkLabel(content, text=desc, font=font_desc, text_color="gray").grid(
                row=row, column=0, columnspan=2, sticky="w", padx=(0, 10), pady=(0, 5)
            )
            row += 1

        # Slack toggle
        self.slack_enabled_var = ctk.StringVar(value="Enabled" if slack_enabled else "Disabled")
        slack_menu = ctk.CTkOptionMenu(content, variable=self.slack_enabled_var, values=["Enabled", "Disabled"])
        setting("Slack", "Enable or disable clipboard detection and blocking in Slack Desktop.", slack_menu)

        # Save button
        def save_apps():
            config["enabled_apps"] = {
                "slack": self.slack_enabled_var.get() == "Enabled"
            }
            with open(CONFIG_PATH, "w") as f:
                json.dump(config, f, indent=4)
            CTkMessagebox(
                title="Saved",
                message="Settings saved successfully.\nRestart the app to apply all changes.",
                icon="check"
            )

        ctk.CTkButton(content, text="Save App Settings", command=save_apps).grid(row=row, column=0, columnspan=2, pady=15)

        ctk.CTkButton(
            self.main_frame,
            text="Restart App",
            fg_color="gray30",
            command=self.restart_app
        ).pack(pady=(0,5))

    def save_settings(self):
        """Adds save button functionality so that the settings page will actually change config.json"""
        try:
            timeout_ms = int(self.popup_timeout_var.get())
            if not (0 <= timeout_ms <= 50000):
                raise ValueError("Popup timeout must be between 0 and 50000.")
            timeout_sec = timeout_ms // 1000
        except ValueError:
            CTkMessagebox(title="Error", message="Invalid popup timeout value. Must be between 0 and 50,000 milliseconds", icon="cancel")
            return
            
        updated_config = {
            "allow_user_quit": self.allow_user_quit_var.get() == "Enabled",
            "popup_timeout": timeout_sec,
            "clear_after_paste": self.clear_after_paste_var.get() == "Enabled",
            "logging_enabled": self.logging_enabled_var.get() == "Enabled",
            "redact_mode": self.redact_mode_var.get(),
            "log_file_path": self.log_file_path_var.get()
        }

        with open(CONFIG_PATH, "w") as f:
            json.dump(updated_config, f, indent=4)

        CTkMessagebox(
            title="Saved",
            message="Settings saved successfully.\nRestart the app to apply all changes.",
            icon="check"
        )

    def restart_app(self):
        import sys, subprocess, os
        subprocess.Popen([sys.executable, os.path.join(os.path.dirname(__file__), "main.py")])
        self.destroy()        

def launch_settings_ui():
    app = SettingsApp()
    app.mainloop()

if __name__ == "__main__":
    launch_settings_ui()