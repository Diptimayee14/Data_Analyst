import tkinter as tk
from tkinter import messagebox

quiz_data = [
    {
        "question": "Q1. Which is the biggest continent in the world?",
        "options": ["1. North America", "2. Asia", "3. Africa", "4. Australia"],
        "correct_answer": "Asia",
    },
    
    {
        "question" : "Q2. Which is the longest river in the world?",
        "options" : ["1. Great Ganga", "2. Nile", "3. Amazon", "4. Niger"],
        "correct_answer" : "Nile",    
    },
    
    {
        "question" : "Q3. Which is the largest ocean in the world?",
        "options" : ["1. Indian Ocean", "2. Pacific Ocean", "3. Arctic Ocean", "4. Atlantic Ocean"],
        "correct_answer" : "Pacific Ocean",    
    },
    
    {
        "question" : "Q4. Which is India's first super computer?",
        "options" : ["1. Param8000", "2. param80000", "3. param800", "4. param8"],
        "correct_answer" : "Param8000",    
    },
    
    {
        "question" : "Q5. Which bank is called bankers Bank of India?",
        "options" : ["1. Reserve Bank of India", "2. Punjab National Bank", "3. State Bank of India", "4. ICICI Bank"],
        "correct_answer" : "Reserve Bank of India",  
    },
    
    {
        "question" : "Q6. Which is the largest flower in the world?",
        "options" : ["1. Rafflesia", "2. Jasmine", "3. Balloon Flower", "4. Camellia"],
        "correct_answer" : "Rafflesia",  
    },
    
    {
        "question" : "Q7. Tsunami is a word in which language?",
        "options" : ["1. Hindi", "2. Urdu", "3. Japanese", "4. French"],
        "correct_answer" : "Japanese",  
    },
    
    {
        "question" : "Q8. On which river the Uri dam is constructed?",
        "options" : ["1. Beas", "2. Jhelum", "3. Sutlej", "4. Ganga"],
        "correct_answer" : "Jhelum",  
    },
    
    {
        "question" : "Q9. Which is hottest continent on Earth?",
        "options" : ["1. Africa", "2. South Asia", "3. North America", "4. Australia"],
        "correct_answer" : "Africa",  
    },
    
    {
        "question" : "Q10. Which animal is Fastest land animal in the world?",
        "options" : ["1. Cheetah", "2. Springbok", "3. Lion", "4. House Centipede"],
        "correct_answer" : "Cheetah",  
    },
]

# Create the main window
class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.current_qs = 0
        
        self.title("QUIZ GAME")
        self.geometry("600x500")
        
        self.label_qs = tk.Label(self, text="", wraplength=300, font=('Segoe UI', 20, 'bold'))
        self.label_qs.pack(pady=10)
        
        self.radio_var = tk.IntVar()
        self.radio_var.set(-1)
        
        self.radio_buttons = []
        for i in range(4):
            radio = tk.Radiobutton(self, text="", variable=self.radio_var, value=i)
            self.radio_buttons.append(radio)
            radio.pack()
    
        self.button_next = tk.Button(self, text="Next", command=self.next_question)
        self.button_next.pack(pady=10)
        self.load_question(0)
        
    # Create and pack widgets
    def load_question(self, qs_index):
        if qs_index < len(quiz_data):
            self.label_qs.config(text=quiz_data[qs_index]["question"])
            for i in range(4):
                self.radio_buttons[i].config(text=quiz_data[qs_index]["options"][i], font=('Segoe UI', 15, 'bold'))
        else:
            self.show_result()
    
    def next_question(self):
        selected_option = self.radio_var.get()
        
        if selected_option == -1:
            messagebox.showwarning("Warning", "Please select an option", font=('Segoe UI', 10, 'bold'))
        else:
            correct_answer = quiz_data[self.current_qs]["correct_answer"]
            if quiz_data[self.current_qs]["options"][selected_option].split(".")[1].strip() == correct_answer:
                self.score += 1
                
            self.current_qs += 1
            self.radio_var.set(-1)
            
            if self.current_qs < len(quiz_data):
                self.load_question(self.current_qs)
            else:
                self.show_result()
                
    def show_result(self):
        messagebox.showinfo("Result", f"You Scored {self.score}/{len(quiz_data)}")
        self.quit()
        
# Run the Tkinter event loop
if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
