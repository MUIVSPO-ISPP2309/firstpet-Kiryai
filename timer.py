import tkinter as tk

class Timer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.running = False
        self.seconds = 0
        self.laps = []
        self.display_seconds = "00:00:00"
        self.create_widgets()
        self.update_timer()

    def create_widgets(self):
        self.time_label = tk.Label(self, text=self.display_seconds, font=("Helvetica", 24))
        self.time_label.pack()

        self.start_button = tk.Button(self, text="Старт", command=self.start)
        self.start_button.pack(side="left")

        self.stop_button = tk.Button(self, text="Остановка", command=self.stop, state="disabled")
        self.stop_button.pack(side="left")

        self.reset_button = tk.Button(self, text="Сброс", command=self.reset)
        self.reset_button.pack(side="left")

        self.lap_button = tk.Button(self, text="Круг", command=self.lap)
        self.lap_button.pack(side="left")

        self.laps_label = tk.Label(self, text="Круги:")
        self.laps_label.pack()

        self.laps_text = tk.Text(self, height=10, width=20)
        self.laps_text.pack()

    def start(self):
        self.running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

    def stop(self):
        self.running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def reset(self):
        self.running = False
        self.seconds = 0
        self.laps = []
        self.display_seconds = "00:00:00"
        self.time_label.config(text=self.display_seconds)
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.laps_text.delete('1.0', tk.END)

    def lap(self):
        self.laps.append(self.display_seconds)
        self.laps_text.insert(tk.END, f"{len(self.laps)}. {self.display_seconds}\n")

    def update_timer(self):
        if self.running:
            self.seconds += 1
            hours, remainder = divmod(self.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.display_seconds = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
            self.time_label.config(text=self.display_seconds)
        self.master.after(1000, self.update_timer)

root = tk.Tk()
app = Timer(master=root)
app.mainloop()
