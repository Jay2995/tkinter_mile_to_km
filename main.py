import tkinter

window = tkinter.Tk();



window.title("Miles to Kilometers converter")
window.minsize(width=350, height=150);
window.config(padx=25, pady=25);







def button_clicked():
    print("I got clicked");
    input = float(text_input.get());
    converted = round(input * 1.60934, 2);
    result_label["text"] = converted;


text_input = tkinter.Entry(width=10);
text_input.grid(column=1, row=0);

button = tkinter.Button(text= "button", command=button_clicked);
button.grid(column=1,row=2)

my_label1 = tkinter.Label(text="Is equal to ", font=("Arial",15, "italic"));
my_label1.grid(column=0, row=1);

my_label2 = tkinter.Label(text="Miles", font=("Arial",15, "italic"));
my_label2.grid(column=2, row=0);

result_label = tkinter.Label(text="this", font=("Arial",15, "italic"));
result_label.grid(column=1, row=1);

my_label3 = tkinter.Label(text="Km", font=("Arial",15, "italic"));
my_label3.grid(column=2, row=1);




window.mainloop()