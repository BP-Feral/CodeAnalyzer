import tkinter as tk
from tkinter import filedialog
from code_analyzer import find_unused_variables, remove_css_duplicates, extract_comments

# Function to handle text change event
def on_text_change(event):
    update_text()

def update_text():
    # print("Text has changed!")
    code = text1.get(1.0, tk.END).strip()
    # Call your custom function here
    if selected_option.get() == "unused_var":
        data = find_unused_variables(code)
    if selected_option.get() == "process_css":
        data = remove_css_duplicates(code)
    if selected_option.get() == "extract_comments":
        data = extract_comments(code)
    
    text2.delete(1.0, tk.END)
    text2.insert(tk.END, data)
    
    text1.edit_modified(False)

def load_file_to_text():
    file_path = filedialog.askopenfilename(title="Select a file")
    
    if file_path:
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                text1.delete(1.0, tk.END)  # Clear the text widget before inserting new content
                text1.insert(tk.END, file_content)  # Insert file content into the text widget
        except Exception as e:
            print(f"Error reading file: {e}")


# Interface Window
root = tk.Tk()
root.title("Syntax Helper")

window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

root.geometry(f"{window_width // 2}x{window_height // 2}")

root.config(bg="#292b3d")
# Setup a frame
frame = tk.Frame(root, bg="#26242f")
frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Text boxes
text1 = tk.Text(frame, height=1, width=1, bg="#26242f", fg="#FFFFFF")
text1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
text1.bind('<<Modified>>', on_text_change)

text2 = tk.Text(frame, height=1, width=1, bg="#26242f", fg="#FFFFFF")
text2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Button to load from file
button_frame = tk.Frame(root, bg="#292b3d")
button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

button = tk.Button(button_frame, text="Load File", command=load_file_to_text)
button.pack()


# Radio Buttons
selected_option = tk.StringVar(value="unused_var")

radio1 = tk.Radiobutton(button_frame, text="Unused Var", variable=selected_option, value="unused_var", command=update_text, 
bg='#292b3d', fg='#FFFFFF', activeforeground='#FFFFFF', activebackground='#292b3d')
radio1.pack(side=tk.LEFT, padx=10)

radio2 = tk.Radiobutton(button_frame, text="Process CSS", variable=selected_option, value="process_css", command=update_text, 
bg='#292b3d', fg='#FFFFFF', activeforeground='#FFFFFF', activebackground='#292b3d')
radio2.pack(side=tk.LEFT, padx=10)

radio3 = tk.Radiobutton(button_frame, text="Extract Comments", variable=selected_option, value="extract_comments", command=update_text, 
bg='#292b3d', fg='#FFFFFF', activeforeground='#FFFFFF', activebackground='#292b3d')
radio3.pack(side=tk.LEFT, padx=10)


root.mainloop()
