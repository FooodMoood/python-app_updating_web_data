import customtkinter as ctk
from ctk_components.recipe_posts_window import *
# from ctk_components.main_window import RecipeApp

# Basic settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    app = ctk.CTk()
    # app.title("Foood Moood Tool")
    # app.geometry("800x600")

    main_window = RecipeApp(app)
    app.mainloop()