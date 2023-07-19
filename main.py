import yaml
import random
import tkinter as tk

result_window = None  # Global variable for the evaluation window

def next_question():
    result_window.destroy()
    question_window.destroy()

def on_button_click(answers):
    global result_window  # Using the global variable result_window

    selected_items = [answer["text"] for answer in answers if answer["selected"].get()]
    print("Selected items:", selected_items)

    # Evaluation logic goes here
    corrected_answers = []
    for answer_item in answers:
        if answer_item["selected"].get():
            # Answer was selected, is it correct?
            if answer_item["truth"]:
                corrected_answers.append("(OK) (correct): " + answer_item["text"])
            else:
                corrected_answers.append("(!!!) (false): " + answer_item["text"])
        else:
            # Answer was not selected, was it correct?
            if answer_item["truth"]:
                corrected_answers.append("(!!!) (correct): " + answer_item["text"])
            else:
                corrected_answers.append("(OK) (false): " + answer_item["text"])
    print(corrected_answers)
    
    # Create new Tkinter window
    result_window = tk.Toplevel()
    result_window.title("Evaluation")

    # Create labels for each line in corrected_answers
    for index, answer in enumerate(corrected_answers):
        label = tk.Label(result_window, text=answer)
        label.pack()
    
    # Add OK button to close the window
    ok_button = tk.Button(result_window, text="OK", command=next_question)
    ok_button.pack()

def on_exit_click():
    print("Exiting the program as per user request")
    exit()

# Path to the YAML file
print("Loading questions...")
file_path = "questions.yaml"

with open(file_path, 'r') as file:
    myQuestions = yaml.safe_load(file)

print("Processing questions...")
random.shuffle(myQuestions)

print("Loaded successfully")

for question in myQuestions:
    this_answers = []
    answer_iterator = 0
    for answer_item in question["answers"]:
        if "istrue" in answer_item:
            this_answers += [{"text": answer_item["istrue"], "truth": True}]
        else:
            this_answers += [{"text": answer_item["isfalse"], "truth": False}]

    random.shuffle(this_answers)

    print(question["text"])
    for answer_item2 in this_answers:
        print("    " + answer_item2["text"])

    # Tkinter question_window creation
    question_window = tk.Tk()

    # Variable for the selected option
    selected = tk.StringVar()

    # Label to display the question
    label = tk.Label(question_window, text=question["text"])
    label.pack()

    # Loop through the list to create radio buttons
    for answer_item2 in this_answers:
        text = answer_item2["text"]
        answer_item2["selected"] = tk.BooleanVar()
        checkbox = tk.Checkbutton(question_window, text=text, variable=answer_item2["selected"])
        checkbox.pack(anchor=tk.W)

    # Create a confirmation button
    button = tk.Button(question_window, text="Select", command=lambda: on_button_click(this_answers))
    button.pack()

    # Create a button to allow the user to exit the quiz
    button = tk.Button(question_window, text="Exit Quiz", command=on_exit_click)
    button.pack()

    # Start the question_window
    question_window.mainloop()
