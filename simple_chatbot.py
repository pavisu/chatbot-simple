from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import tkinter as tk
from tkinter import scrolledtext

# Create a chatbot instance
chatbot = ChatBot('SimpleBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Function to handle user input and display response
def get_response():
    user_input = user_input_entry.get()
    
    # Exit the application if the user enters 'exit'
    if user_input.lower() == 'exit':
        response_text.config(state=tk.NORMAL)
        response_text.insert(tk.END, "SimpleBot: Goodbye!\n")
        response_text.config(state=tk.DISABLED)
        user_input_entry.config(state=tk.DISABLED)
        send_button.config(state=tk.DISABLED)
    else:
        # Get the chatbot's response
        response = chatbot.get_response(user_input)
        
        # Display user input and chatbot response
        response_text.config(state=tk.NORMAL)
        response_text.insert(tk.END, f"You: {user_input}\n")
        response_text.insert(tk.END, f"SimpleBot: {response}\n")
        response_text.config(state=tk.DISABLED)
        user_input_entry.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("Simple Chatbot")

# Create and configure UI components
user_input_entry = tk.Entry(app, width=50)
send_button = tk.Button(app, text="Send", command=get_response)
response_text = scrolledtext.ScrolledText(app, width=60, height=15, state=tk.DISABLED)

# Place UI components in the window
user_input_entry.pack(pady=10)
send_button.pack()
response_text.pack(padx=10, pady=10)

# Start the application
app.mainloop()
