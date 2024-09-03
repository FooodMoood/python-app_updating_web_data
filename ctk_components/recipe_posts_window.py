import customtkinter as ctk
import webbrowser
import traceback

import ctk_components.get_config as get_config
from ctk_components.info_before_posting_window import PostConfirmation
from ctk_components.website_handler import WebsiteHandler

# Set theme
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill="both", expand=True)

class RecipeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Data Creator")

        # Configure the root window grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        #Main scroll frame
        self.scrollable_frame = ScrollableFrame(self.root, width=800, height=600)

        # GitHub icon
        self.github_icon = ctk.CTkButton(self.scrollable_frame, text="GitHub", command=self.open_github, width=80, height=30, corner_radius=10, fg_color="black", hover_color="#08210C")
        self.github_icon.pack(pady=(20, 5), padx=20, anchor="ne")
        
        # Components for main recipe ID
        self.input_label = ctk.CTkLabel(self.scrollable_frame, text="Input Recipe ID", anchor="w")
        self.input_label.pack(pady=(20, 5), padx=20, fill="x")

        self.recipe_id_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="")
        self.recipe_id_entry.pack(pady=5, padx=20, fill="x")

        # Socials buttons
        self.top_nav_frame = ctk.CTkFrame(self.scrollable_frame)
        self.top_nav_frame.pack(pady=10, padx=20, fill='x')

        self.top_nav_buttons_frame = ctk.CTkFrame(self.top_nav_frame)
        self.top_nav_buttons_frame.pack(pady=10, expand=True)

        self.youtube_button = self.create_nav_button("YouTube", self.yt_combined_command, self.top_nav_buttons_frame)
        self.instagram_button = self.create_nav_button("Instagram", self.instagram_combined_command, self.top_nav_buttons_frame)
        self.pinterest_button = self.create_nav_button("Pinterest", self.pinterest_combined_command, self.top_nav_buttons_frame)

        self.bottom_nav_frame = ctk.CTkFrame(self.scrollable_frame)
        self.bottom_nav_frame.pack(pady=10, padx=20, fill='x')

        self.bottom_nav_buttons_frame = ctk.CTkFrame(self.bottom_nav_frame)
        self.bottom_nav_buttons_frame.pack(pady=10, expand=True)

        self.wordpress_button = self.create_nav_button("Generate Wordpress code", self.wp_combined_command, self.bottom_nav_buttons_frame)
        self.post_button = self.create_nav_button("Publish post on Wordpress", self.post_confirmation, self.bottom_nav_buttons_frame)

        # Componetns for output data
        self.output_data_label = ctk.CTkLabel(self.scrollable_frame, text="Output Data", anchor="w")
        self.output_data_label.pack(pady=(20, 5), padx=20, fill="x")

        self.output_data_textbox = ctk.CTkTextbox(self.scrollable_frame, height=200, corner_radius=10)
        self.output_data_textbox.pack(pady=5, padx=20, fill="both", expand=True)

        # Action buttons
        self.button_frame = ctk.CTkFrame(self.scrollable_frame, height=50, width=800, corner_radius=10)
        self.button_frame.pack(pady=10)

        self.copy_button = self.create_action_button("COPY", self.copy_text, "#4CAF50")
        self.clear_button = self.create_action_button("CLEAR", self.clear_text, "#F44336")
   
    def open_github(self):
        webbrowser.open_new(get_config.path_github_repo)

    def combobox_callback(self, choice):
        print("Combobox option selected:", choice)

    def create_nav_button(self, text, command, frame):
        button = ctk.CTkButton(frame, text=text, command=command, width=150, height=30, corner_radius=10)
        button.pack(side="left", padx=5, pady=5)
        return button

    def create_action_button(self, text, command, color):
        button = ctk.CTkButton(self.button_frame, text=text, width=100, height=40, corner_radius=10, fg_color=color, command=command)
        button.pack(side="left", padx=5, pady=5)
        return button
    
    def copy_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.output_data_textbox.get("1.0", "end"))

    def post_confirmation(self):
        recipe_id = self.recipe_id_entry.get()
        PostConfirmation(self.root, recipe_id)

    def clear_text(self):
        self.output_data_textbox.delete("1.0", "end")

    def handle_wordpress(self):
        self.handle_website(get_config.PLATFORM_WORDPRESS)

    def handle_youtube(self):
        self.handle_website(get_config.PLATFORM_YOUTUBE)

    def handle_instagram(self):
        self.handle_website(get_config.PLATFORM_INSTAGRAM)

    def handle_pinterest(self):
        self.handle_website(get_config.PLATFORM_PINTEREST)

    def handle_website(self, website_type):
        recipe_id = self.recipe_id_entry.get()
        try:
            if recipe_id:
                website_handler = WebsiteHandler(recipe_id, website_type)
                output_data = website_handler.perform_action()
                self.output_data_textbox.delete("1.0", "end")
                self.output_data_textbox.insert("1.0", output_data)
            else:
                self.output_data_textbox.configure(state="normal`")
        except Exception as e:
            error_trace = traceback.format_exc()
            error_message = f"An error occurred while processing the request. Error details: {str(e)}\n{error_trace}"

    def wp_combined_command(self):
        self.clear_text()
        self.handle_wordpress()

    def yt_combined_command(self):
        self.clear_text()
        self.handle_youtube()

    def instagram_combined_command(self):
        self.clear_text()
        self.handle_instagram()

    def pinterest_combined_command(self):
        self.clear_text()
        self.handle_pinterest()
