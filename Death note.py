import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime, timedelta
import threading
import time

class DeathNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💀 Death Note")
        self.entries = []

        # Name
        tk.Label(root, text="👤 Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=0, column=1)

        # Cause of death
        tk.Label(root, text="☠️ Cause of Death:").grid(row=1, column=0, sticky="w")
        self.cause_entry = tk.Entry(root, width=30)
        self.cause_entry.insert(0, "heart attack")
        self.cause_entry.grid(row=1, column=1)

        # Delay (in seconds)
        tk.Label(root, text="⏳ Delay (seconds):").grid(row=2, column=0, sticky="w")
        self.delay_entry = tk.Entry(root, width=30)
        self.delay_entry.insert(0, "0")
        self.delay_entry.grid(row=2, column=1)

        # Buttons
        tk.Button(root, text="✍️ Write Name", command=self.write_name).grid(row=3, column=0, pady=10)
        tk.Button(root, text="📜 Show Entries", command=self.show_entries).grid(row=3, column=1)
        tk.Button(root, text="💥 Simulate Deaths", command=self.start_simulation).grid(row=4, column=0, columnspan=2)

        # Log window
        self.log = scrolledtext.ScrolledText(root, width=50, height=15)
        self.log.grid(row=5, column=0, columnspan=2, pady=10)
        self.log.insert(tk.END, "📓 Welcome to the Death Note\n")

    def write_name(self):
        name = self.name_entry.get().strip()
        cause = self.cause_entry.get().strip()
        try:
            delay = int(self.delay_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Delay must be a number!")
            return

        if not name:
            messagebox.showerror("Error", "Name cannot be empty.")
            return

        death_time = datetime.now() + timedelta(seconds=delay)
        self.entries.append({'name': name, 'cause': cause, 'death_time': death_time})
        self.log.insert(tk.END, f"🖊️ Wrote '{name}' - Cause: {cause}, Delay: {delay} sec\n")
        self.name_entry.delete(0, tk.END)

    def show_entries(self):
        self.log.insert(tk.END, "\n📜 All Entries:\n")
        for e in self.entries:
            self.log.insert(tk.END, f"👤 {e['name']} - ☠️ {e['cause']} - 🕒 {e['death_time']}\n")
        self.log.insert(tk.END, "\n")

    def simulate_deaths(self):
        self.log.insert(tk.END, "\n🔮 Starting Simulation...\n")
        for e in self.entries:
            now = datetime.now()
            delay = (e['death_time'] - now).total_seconds()
            if delay > 0:
                self.log.insert(tk.END, f"⏳ Waiting for {e['name']} to die in {int(delay)} seconds...\n")
                self.log.see(tk.END)
                time.sleep(delay)
            self.log.insert(tk.END, f"💀 {e['name']} has died due to {e['cause']} at {datetime.now()}.\n")
            self.log.see(tk.END)

    def start_simulation(self):
        t = threading.Thread(target=self.simulate_deaths)
        t.start()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DeathNoteApp(root)
    root.mainloop()
