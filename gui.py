import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self, pages):
        super().__init__()

        self.title("My Application")
        self.geometry("400x300")

        # Create a container frame for all pages
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        # Create a dictionary to hold all pages
        self.pages = {}

        for page_class in pages:
            # Create an instance of each page class
            page = page_class(self.container, self)
            self.pages[page.__class__.__name__] = page

            # Pack the page in the container frame
            page.pack(side="top", fill="both", expand=True)

        # Show the first page
        self.show_page(pages[0].__class__.__name__)

    def show_page(self, page_name):
        # Show the page with the given name
        page = self.pages[page_name]
        page.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = tk.Label(self, text="Welcome to the start page!")
        label.pack(padx=10, pady=10)

        button = tk.Button(self, text="Go to settings page",
                           command=lambda: controller.show_page("SettingsPage"))
        button.pack(padx=10, pady=10)

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = tk.Label(self, text="Welcome to the settings page!")
        label.pack(padx=10, pady=10)

        button = tk.Button(self, text="Go to start page",
                           command=lambda: controller.show_page("StartPage"))
        button.pack(padx=10, pady=10)

if __name__ == "__main__":
    pages = [StartPage, SettingsPage]
    app = MyApp(pages)
    app.mainloop()
