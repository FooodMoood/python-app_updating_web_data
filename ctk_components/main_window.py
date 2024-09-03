# import customtkinter as ctk
# from ctk_components.recipe_posts_window import RecipeApp

# class MainWindow:
#     def __init__(self, root):
#         self.master = root

#         # Configure the main window grid
#         self.master.grid_rowconfigure(0, weight=1)
#         self.master.grid_columnconfigure(0, weight=0)
#         self.master.grid_columnconfigure(1, weight=1)

#         # Left frame
#         self.frame_left = ctk.CTkFrame(root, width=200, corner_radius=0)
#         self.frame_left.grid(row=0, column=0, sticky="nswe")
#         self.frame_left.grid_rowconfigure(0, weight=1)
#         self.frame_left.grid_columnconfigure(0, weight=1)

#         # Left frame content
#         self.label_info = ctk.CTkLabel(self.frame_left, text="Short description", font=ctk.CTkFont("Roboto", 20, "bold"))
#         self.label_info.grid(row=0, column=0, pady=10, padx=10, sticky="nswe")

#         # Right frame
#         self.frame_right = ctk.CTkFrame(root)
#         self.frame_right.grid(row=0, column=1, sticky="nswe")
#         self.frame_right.grid_rowconfigure(0, weight=1)
#         self.frame_right.grid_rowconfigure(1, weight=1)
#         self.frame_right.grid_columnconfigure(0, weight=1)
#         self.frame_right.grid_columnconfigure(1, weight=1)
#         self.frame_right.grid_columnconfigure(2, weight=1)

#         # Buttons for right frame properly distributed
#         self.button_prompt_generator = ctk.CTkButton(self.frame_right, text="Prompt generator for \nYoutube, Instagram, Pinterest", command=self.open_recipe_post_window)
#         self.button_prompt_generator.grid(row=0, column=0, columnspan=2, pady=1, padx=1, sticky="we")

#         self.button_wordpress_generator = ctk.CTkButton(self.frame_right, text="Code generator for \nWordpress recipes")
#         self.button_wordpress_generator.grid(row=0, column=2, pady=1, padx=1)

#         # API buttons in one line
#         self.button_youtube_api = ctk.CTkButton(self.frame_right, text="API for YouTube")
#         self.button_youtube_api.grid(row=1, column=0, pady=1, padx=1)

#         self.button_instagram_api = ctk.CTkButton(self.frame_right, text="API for Instagram")
#         self.button_instagram_api.grid(row=1, column=1, pady=1, padx=1)

#         self.button_pinterest_api = ctk.CTkButton(self.frame_right, text="API for Pinterest")
#         self.button_pinterest_api.grid(row=1, column=2, pady=1, padx=1)

#     def open_recipe_post_window(self):
#         instance = RecipeApp(self.master)

# # if __name__ == "__main__":
# #     app = MainWindow(root)
# #     root.mainloop()
