import tkinter as tk
from tkinter import scrolledtext
from core import run_scan


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
    
def handle_scan_result(result):
    append_output(f'Scan complete: {result}')
    start_btn.config(state=tk.NORMAL)

def start_scan():
    clear()
    target = target_box.get()
    append_output("Scan Started......\nPlease Wait for Results\n") 
    start_btn.config(state=tk.DISABLED)
    run_scan(target,selected.get(), handle_scan_result)
    
    



root = tk.Tk()
root.title("NMAP")
root.geometry("700x600")

top_frame=tk.Frame(root)
top_frame.pack(pady=10)
target_label=tk.Label(top_frame,text="Target:")
target_label.pack(side=tk.LEFT)
target_box=tk.Entry(top_frame,width=30)
target_box.pack(side=tk.LEFT,padx=10)

modes=["-sS","-sT","-O"]
selected=tk.StringVar(value="-sS")
options_menu=tk.OptionMenu(top_frame,selected,*modes)
options_menu.pack(side=tk.LEFT,padx=10)
start_btn=tk.Button(top_frame,text="Start",command=start_scan)
start_btn.pack(side=tk.LEFT, padx=10)
output=scrolledtext.ScrolledText(root,wrap=tk.WORD)
output.config(state='disabled')
output.pack(pady=20)
root.mainloop()