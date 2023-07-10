from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas(height=500, width=800)
card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 260, image=card_front)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 260, text="word", font=("Ariel", 40, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# button
wrong_btn = PhotoImage(file="./images/wrong.png")
right_btn = PhotoImage(file="./images/right.png")

wrong_button = Button(image=wrong_btn, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_btn, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()
