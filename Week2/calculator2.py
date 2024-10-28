import tkinter as tk

root = tk.Tk()
root.title("Calculator")

entry=tk.Entry(root,width=16)
entry.grid(row=0,column=0, columnspan=4)

buttons = [1,2,3,4,5,6,7,8,9,0,"C","D","=","+","-","/","*"];

def btnClick(btn):
    if btn == "=":
        ans = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
    elif btn == "C":
        entry.delete(0,tk.END)
    elif btn == "D":
        text=entry.get()[:-1];
    
        entry.delete(0,tk.END)
        entry.insert(tk.END,text)
    else:
        entry.insert(tk.END,btn)
        

row=1
col=0
for button in buttons:
    tk.Button(root,text=button,command=lambda b=button: btnClick(b)).grid(row=row,column=col)
    col+=1
    if col == 4:
        col=0;
        row+=1


root.mainloop()