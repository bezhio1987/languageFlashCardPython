from tkinter import *
import pandas, random, time

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/french_words.csv")
data_dict = data.to_dict(orient="records")
current_card={}

def new_card():
    global current_card, flip_timer
    # we have to stop the timer when the button is pressed, otherwise if i click many times it will flip immediately
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    word = current_card["French"]
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=word, fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background, image=card_back_img)



# --------------------------------------------------UI---------------------------------------

window = Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# canvas
canvas = Canvas(height=500, width=800)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 260, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 260, text="word", font=("Ariel", 40, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# button
wrong_btn = PhotoImage(file="./images/wrong.png")
right_btn = PhotoImage(file="./images/right.png")

wrong_button = Button(image=wrong_btn, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_btn, highlightthickness=0, command=new_card)
right_button.grid(row=1, column=1)

new_card()
window.mainloop()
