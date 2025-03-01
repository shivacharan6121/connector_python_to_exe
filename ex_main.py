import customtkinter as ctk
import pymysql
from tkinter import ttk

# Configure theme
ctk.set_appearance_mode("Dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue", "green", "dark-blue"

# Styled MessageBox
class CustomMessageBox(ctk.CTkToplevel):
    def __init__(self, title, message, color, action=None):
        super().__init__()
        self.title(title)
        self.geometry("300x150")
        self.configure(bg=color)
        self.action = action
        
        # Label for displaying message
        label = ctk.CTkLabel(self, text=message, font=("Arial", 14), text_color="white")
        label.pack(pady=10)
        
        # Frame to hold buttons
        button_frame = ctk.CTkFrame(self, bg_color=color)
        button_frame.pack(pady=10)
        
        # OK button
        ok_button = ctk.CTkButton(button_frame, text="OK", command=self.on_ok, fg_color="black", hover_color="gray")
        ok_button.grid(row=0, column=0, padx=10)
        
        # Cancel button
        cancel_button = ctk.CTkButton(button_frame, text="Cancel", command=self.on_cancel, fg_color="red", hover_color="dark red")
        cancel_button.grid(row=0, column=1, padx=10)
    
    def on_ok(self):
        if self.action:
            self.action()
        self.destroy()
    
    def on_cancel(self):
        self.destroy()

# Database Connection Functions
def execute_query(query, params):
    try:
        conn = pymysql.connect(
            host="localhost", user="root", password="", database="connectors.db"
        )
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()
        display_data() #refresh the database items
    except mysql.connector.Error as err:
        CustomMessageBox("Error", f"Database Error: {err}", "#8B0000")

# Function to insert data into the database
def insert_data():
    part_no = part_entry.get()
    connectors_required = connectors_entry.get()
    if part_no and connectors_required:
        try:
            conn = pymysql.connect(
                host="localhost", user="root", password="", database="connectors.db"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT quantity FROM parts WHERE part_no = %s", (part_no,))
            result = cursor.fetchone()
            conn.close()
            
            if result:
                existing_quantity = result[0]
                added_quantity = int(connectors_required)
                new_quantity = existing_quantity + added_quantity
                action = lambda: execute_query("UPDATE parts SET quantity = %s WHERE part_no = %s", (new_quantity, part_no))
                CustomMessageBox("Update Confirmation", f"Part No: {part_no}\nAdded Connectors: {added_quantity}\nAvailable Connectors: {existing_quantity}\nTotal Connectors: {new_quantity}", "#228B22", action)
            else:
                action = lambda: execute_query("INSERT INTO parts (part_no, quantity) VALUES (%s, %s)", (part_no, connectors_required))
                CustomMessageBox("New Entry Confirmation", f"New Part No added: {part_no}\n:Added Connectors:{connectors_required}", "#006400", action)
        except mysql.connector.Error as err:
            CustomMessageBox("Error", f"Database Error: {err}", "#8B0000")
    else:
        CustomMessageBox("Warning", "Please enter valid data!", "#FFD700")

# Function to remove data from the database
def remove_data():
    part_no = part_entry.get()
    quantity_to_remove = connectors_entry.get()
    if part_no and quantity_to_remove:
        try:
            conn = pymysql.connect(
                host="localhost", user="root", password="", database="connectors.db"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT quantity FROM parts WHERE part_no = %s", (part_no,))
            result = cursor.fetchone()
            conn.close()
            
            if result:
                current_quantity = result[0]
                removed_quantity = int(quantity_to_remove)
                if current_quantity >= removed_quantity:
                    new_quantity = current_quantity - removed_quantity
                    action = lambda: execute_query("UPDATE parts SET quantity = %s WHERE part_no = %s", (new_quantity, part_no))
                    CustomMessageBox("Removal Confirmation", f"Part No: {part_no}\nRequired Connectors: {removed_quantity}\nRemaining Connectors: {new_quantity}", "#FF4500", action)
                else:
                    CustomMessageBox("Warning", f"Insufficient Connectors\n Available Connectors:{current_quantity}\nRequired Connectors:{removed_quantity}", "#FFD700")
            else:
                CustomMessageBox("Error", f"Invalid Part No:{part_no}", "#8B0000")
        except mysql.connector.Error as err:
            CustomMessageBox("Error", f"Database Error: {err}", "#8B0000")
    else:
        CustomMessageBox("Warning", "Please enter valid data!", "#FFD700")

# Function to display data in the table
def display_data():
    for i in table.get_children():
        table.delete(i)
    try:
        conn = pymysql.connect(
            host="localhost", user="root", password="", database="connectors.db"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM parts")
        rows = cursor.fetchall()
        for idx, row in enumerate(rows, start=1):
            table.insert("", "end", values=(idx, row[0], row[1]), tags=("even" if idx % 2 == 0 else "odd"))
        conn.close()
    except mysql.connector.Error as err:
        CustomMessageBox("Error", f"Database Error: {err}", "#8B0000")

# GUI Setup
app = ctk.CTk()
app.title("Connector Management System")
#window = tk.Tk()
width= app.winfo_screenwidth() 
height= app.winfo_screenheight()
#setting tkinter window size
app.geometry("%dx%d" % (width, height))

# Title
title_label = ctk.CTkLabel(app, text="Connector Management System", font=("Arial", 24, "bold"))
title_label.pack(pady=10)

# Input Frame
input_frame = ctk.CTkFrame(app)
input_frame.pack(pady=10, padx=20, fill="x")

# Part Number Input
part_label = ctk.CTkLabel(input_frame, text="Part No:")
part_label.grid(row=0, column=0, padx=5, pady=5)
part_entry = ctk.CTkEntry(input_frame, width=200)
part_entry.grid(row=0, column=1, padx=5, pady=5)

# Number of Connectors Input
connectors_label = ctk.CTkLabel(input_frame, text="No. of Connectors:")
connectors_label.grid(row=1, column=0, padx=5, pady=5)
connectors_entry = ctk.CTkEntry(input_frame, width=200)
connectors_entry.grid(row=1, column=1, padx=5, pady=5)

# Buttons
enter_button = ctk.CTkButton(input_frame, text="Add", command=insert_data, fg_color="green", hover_color="dark green")
enter_button.grid(row=2, column=0, pady=10)

remove_button = ctk.CTkButton(input_frame, text="Enter", command=remove_data, fg_color="red", hover_color="dark red")
remove_button.grid(row=2, column=1, pady=10)

# Table Frame
table_frame = ctk.CTkFrame(app)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

columns = ("Serial No", "Part No", "Quantity")
table = ttk.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    table.heading(col, text=col)
    table.column(col, anchor="center", width=150)

table.pack(fill="both", expand=True)

display_data()
app.mainloop()
