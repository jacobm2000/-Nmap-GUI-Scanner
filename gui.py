import tkinter as tk
from tkinter import scrolledtext
import time
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
    global end_time
    end_time=time.time()
    total_time=round(end_time-start_time,2)
    append_output(f'\nTotal time elapsed: {total_time} seconds \n')
    append_output(f'Scan complete: {result}')
    start_btn.config(state=tk.NORMAL)
   
    

def start_scan():
    clear()
    global start_time
    start_time=time.time()
    target = target_box.get()
    append_output("Scan Started......\nPlease Wait for Results\n") 
    start_btn.config(state=tk.DISABLED)
    run_scan(target,selected_mode.get(),port_start.get(),port_end.get(),selected_speed.get(), handle_scan_result)
    
    


start_time=0.0
end_time=0.0
root = tk.Tk()
root.title("NMAP")
root.geometry("750x600")

top_frame=tk.Frame(root)
top_frame.pack(pady=10)
target_label=tk.Label(top_frame,text="Target:")
target_label.pack(side=tk.LEFT)
target_box=tk.Entry(top_frame,width=30)
target_box.pack(side=tk.LEFT,padx=10)
port_start_label=tk.Label(top_frame,text="Port range start")
port_start_label.pack(side=tk.LEFT)
port_start=tk.Entry(top_frame,width=5)
port_start.pack(side=tk.LEFT,padx=10)
port_end_label=tk.Label(top_frame,text="Port range end")
port_end_label.pack(side=tk.LEFT)
port_end=tk.Entry(top_frame,width=5)
port_end.pack(side=tk.LEFT,padx=10)

modes=["-sS","-sT","-O","-A"]
selected_mode=tk.StringVar(value="-sS")
type_menu=tk.OptionMenu(top_frame,selected_mode,*modes)
type_menu.pack(side=tk.LEFT,padx=10)

speeds=["-T5","-T4","-T3","-T2","-T1","-T0"]
selected_speed=tk.StringVar(value="-T4")
speed_menu=tk.OptionMenu(top_frame,selected_speed,*speeds)
speed_menu.pack(side=tk.LEFT,padx=10)

start_btn=tk.Button(top_frame,text="Start",command=start_scan)
start_btn.pack(side=tk.LEFT, padx=10)
output=scrolledtext.ScrolledText(root,wrap=tk.WORD)
output.config(state='disabled')
output.pack(pady=20)
root.mainloop()