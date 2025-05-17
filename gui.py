import tkinter as tk
from core import run

#This function0 temporarly allows the output area to be writen to and then disables it after to prevent user tampering
def append_output(text):
    output.config(state='normal')
    output.insert(tk.END, f'{text}')
    output.config(state='disabled')
    output.see(tk.END)

def clear():
    output.config(state='normal')
    output.delete('1.0', tk.END)
    output.config(state='disabled')
    
def start():
    clear()
    append_output(run(target_box.get()))



root = tk.Tk()
root.title("NMAP")
root.geometry("700x600")

top_frame=tk.Frame(root)
top_frame.pack(pady=10)
target_label=tk.Label(top_frame,text="Target:")
target_label.pack(side=tk.LEFT)
target_box=tk.Entry(top_frame,width=30)
target_box.pack(side=tk.LEFT,padx=10)
start_btn=tk.Button(top_frame,text="Start",command=start)
start_btn.pack(side=tk.LEFT, padx=10)
output=tk.scrolledtext.ScrolledText(root,wrap=tk.WORD)
output.config(state='disabled')
output.pack(pady=20)
root.mainloop()