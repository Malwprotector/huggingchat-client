print('botname HAS BEEN INITIALIZED\n--------------------')
print('loading libraries...')
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
from hugchat import hugchat
from hugchat.login import Login

# Function to send user input to the chatbot
def send_message():
    user_input = entry.get()
    entry.delete(0, tk.END)  # Clear the input field

    if user_input.lower() == 'exit':
        chatbot.delete_all_conversations()
        window.quit()
    else:
        response = chatbot.query(user_input)
        conversation_display.configure(state="normal")
        conversation_display.insert(tk.END, f"user: {user_input}\n", "user_message")
        conversation_display.insert(tk.END, f"botname: {response['text']}\n\n", "bot_message")
        conversation_display.configure(state="disabled")
        conversation_display.see(tk.END)  # Scroll to the bottom

# Load email and password from the credentials file
print('Reading credentials...')
with open('credentials', 'r') as file:
    email = file.readline().strip()
    password = file.readline().strip()

sign = Login(email, password)
cookies = sign.login()
print('Identification data has been recorded and registered.')

# Save cookies to the local directory
print('Saving login info...')
cookie_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)

# Create a ChatBot
print('Sending request to create instance...')
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

# Create and switch to the existing "wall-e" conversation
print('Loading instance...')
wl = chatbot.new_conversation()
chatbot.change_conversation(wl)

# Send initial message to the chatbot
print('Reading prompt and WALL-M 1.0 data...')
with open('prompt', 'r') as file:
    initial_user_message = file.readline().strip()
response = chatbot.query(initial_user_message)

# Create the themed GUI window
print('Graphic interface modeling...')
window = ThemedTk(theme="equilux")
window.title("windowstitle")

# Set a custom style for the ttk Entry widget
style = ttk.Style()
style.configure("TEntry", padding=5)

# Create a frame to hold the conversation display and scrollbar
frame = ttk.Frame(window, padding=(10, 10), style="TFrame")
frame.grid(row=0, column=0, sticky="nsew")
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Create a scrollbar and attach it to the conversation display
scrollbar = ttk.Scrollbar(frame, style="Vertical.TScrollbar")
scrollbar.grid(row=0, column=1, sticky="ns")

# Create a custom style for the conversation display
style.configure("user_message.TLabel", foreground="blue")
style.configure("bot_message.TLabel", foreground="green")

conversation_display = tk.Text(frame, wrap="word", state="disabled", font=("Arial", 12), yscrollcommand=scrollbar.set, bg="black", fg="white")
conversation_display.tag_configure("user_message", font=("Arial", 12, "bold"))
conversation_display.tag_configure("bot_message", font=("Arial", 12, "italic"))
print('Graphic interface initialized, no error reported')

# Insert initial user message and bot response
print('Sending prompt and WALL-M 1.0 data...')
conversation_display.configure(state="normal")
conversation_display.insert(tk.END, f"user: {response['text']}\n\n", "bot_message")
conversation_display.configure(state="disabled")
conversation_display.grid(row=0, column=0, sticky="nsew")
scrollbar.config(command=conversation_display.yview)

# Create an input field and a send button
entry = ttk.Entry(window, font=("Arial", 12), justify="left")
entry.grid(row=1, column=0, sticky="nsew", padx=(10, 0), pady=(0, 10))

send_button = ttk.Button(window, text="Send", command=send_message, cursor="hand2")
send_button.grid(row=1, column=1, sticky="nsew", padx=(0, 10), pady=(0, 10))

# Function to close the application
def close_app():
    if messagebox.askokcancel("Disconnect", "Disconnect and stop WALL-M?"):
        print('Destroying online data...')
        chatbot.delete_all_conversations()
        print('Done')
        print('Destroying Graphic Interface...')
        window.destroy()
        print('Done')
        print('See you soon!\n--------------------\nbotname HAS BEEN STOPPED')

# Create a close button
close_button = ttk.Button(window, text="Close", command=close_app, cursor="hand2")
close_button.grid(row=1, column=2, sticky="nsew", padx=(0, 10), pady=(0, 10))

# Set grid weights for resizing
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Start the GUI event loop
window.mainloop()
