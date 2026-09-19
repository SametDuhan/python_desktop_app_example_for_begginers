
import customtkinter as ctk

# Apprearance and theme settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main application window
app = ctk.CTk()
app.geometry("450x350")
app.title("User Greeting Panel")

# 1.Title Label
title_label = ctk.CTkLabel(app, text="Welcome to the User Greeting Panel", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

# 2. Name Entry Field
name_entry = ctk.CTkEntry(app, placeholder_text="Write your name...", width=250, height=35)
name_entry.pack(pady=10)

# 3. Result Display Area
result_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
result_label.pack(pady=20)

# Function to be executed when the button is pressed
def greet():
    entered_name = name_entry.get().strip()  # Here is the string method you learned: strip() removes whitespace

    if entered_name:
        result_label.configure(text=f"Hello {entered_name.capitalize()}, nice to have you here!", text_color="#4CAF50")
    else:
        result_label.configure(text="Please enter a name first!", text_color="#F44336")

# 4. Tetikleyici Buton
buton = ctk.CTkButton(app, text="Say Hello", command=greet, width=150, height=35)
buton.pack(pady=10)

# Döngüyü başlat
app.mainloop()

print("HELLO THIS IS A TEST APPLICATION AND IT IS IMPROVONG DAY BY DAY IF YOU WANT TO HELP ME PLEASE CONTACT ME SO I CAN IMPROVE MYSELF AND MY APPLICATION THANK YOU FOR YOUR SUPPORT")

name=input("Please enter your name: ")
surname=input("Please enter your surname: ")
print(f"Hello, {name} {surname}! Welcome to the test application. We are glad to have you here.")

name=""
inputName = input("enter your namee")

def wiya(year):
    return 2026-year

numbers=[1,2,3,4,5,6]
numbers_sq=[]
for i in numbers:
    if i %2==0:
        numbers_sq.append()
        
    
