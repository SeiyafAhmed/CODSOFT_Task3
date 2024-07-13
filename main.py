import random
import ttkbootstrap.toast
from ttkbootstrap import *

root = Window("Password Generator", themename="passwordgenerator", size=(350, 600), resizable=(False, False))

root.iconbitmap("./logo.ico")

logo = PhotoImage(file="./logo.png")

Label(root, image=logo).pack()

Label(root, text="PASSWORD GENERATOR", font=("Arial black", 16), style="warning").pack()

lows = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upps = [i.upper() for i in lows]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
syms = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|", ";", ":", "\'", "\"", ",", "<", ".", ">", "/", "?"]

upp = BooleanVar()
num = BooleanVar()
sym = BooleanVar()
lvl = StringVar()
lnt = IntVar(value=8)
pwd = StringVar()

includes = [
    ["Uppercase", upp],
    ["Numbers", num],
    ["Symbols", sym]
]
levels = ["Low", "Normal", "High"]

len_frame = Frame(root)
len_frame.pack(pady=10)
Label(len_frame, text="Length of the password", font=("dubai medium", 14), style="secondary").pack(side=LEFT, padx=10)
Spinbox(len_frame, textvariable=lnt, from_=8, to=40, width=3, style="warning" ).pack(side=RIGHT, padx=10)

include_frame = LabelFrame(root, text="Include", style="secondary")
include_frame.pack(pady=10)

level_frame = LabelFrame(root, text="Complexity Level", style="secondary")
level_frame.pack(pady=10)




def password_generator():
    upp_len = 0
    num_len = 0
    sym_len = 0

    if upp.get():
        upp_len = lnt.get()//8

    if num.get():
        num_len = lnt.get()//8

    if sym.get():
        sym_len = lnt.get()//8

    if lvl.get() == "Normal":
        upp_len *= 2
        num_len *= 2
        sym_len *= 2

    if lvl.get() == "High":
        upp_len *= 3
        num_len *= 3
        sym_len *= 3
        pass

    temp = ""
    while (sym_len or num_len or upp_len) and len(temp) < lnt.get() :
        if upp_len:
            temp += random.choice(upps)
            upp_len -= 1
        if num_len:
            temp += random.choice(nums)
            num_len -= 1
        if sym_len:
            temp += random.choice(syms)
            sym_len -= 1

    while len(temp) < lnt.get():
        temp += random.choice(lows)

    temp = list(temp)
    n_lst = list(range(len(temp)))

    for i in temp.copy():
        n = random.choice(n_lst)
        temp[n] = i
        n_lst.remove(n)

    pwd.set("".join(temp))
    copy_btn.config(state="normal", text="Copy to Clipboard")

for txt, var in includes:
    Checkbutton(include_frame, text=txt, variable=var, style="warning", width=15).pack(pady=10, padx=15)

for level in levels:
    Radiobutton(level_frame, text=level, width=10, style="warning", variable=lvl, value=level).pack(side=LEFT, padx=10, pady=15)

generate_btn = Button(root, text="Generate Password", style="warning", command=password_generator)
generate_btn.pack(pady=10, padx=10)

def copy_to_clipboard():
    pwd_label.clipboard_clear()
    pwd_label.clipboard_append(pwd.get())
    ttkbootstrap.toast.ToastNotification("Password copied!", f"Password: {pwd.get()}", duration=2500, alert=True).show_toast()
    copy_btn.config(text="Copied!")

pwd_label = Entry(root, textvariable=pwd, width=50, style="secondary", justify="center", state="disabled")
pwd_label.pack(pady=5)

copy_btn = Button(root, text="Copy to Clipboard", style="warning", command=copy_to_clipboard, state="disabled")
copy_btn.pack(pady=5)

footer = Frame(root, width=550, style="dark",)
footer.pack(side=BOTTOM)
Label(footer, text="©2024 Seiyaf Ahmed ", style="inverse-dark", justify="right",).pack(padx=116)

root.mainloop()
