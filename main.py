import tkinter as tk
from tkinter import messagebox
from modules.port_scanner import start_port_scan
from modules.banner_grabber import grab_banner
from modules.brute_forcer import brute_force_simulator
import threading
import socket
import os


# ================= BANNER TEST SERVER =================
def start_banner_test_server():
    try:
        HOST = "127.0.0.1"
        PORT = 9090

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(1)

        while True:
            client, addr = server.accept()
            client.sendall(b"Pentesting-Toolkit-Test-Server v1.0\r\n")
            client.close()
    except:
        pass


threading.Thread(target=start_banner_test_server, daemon=True).start()


# ================= OUTPUT FUNCTIONS =================
def log_output(message):
    output_text.insert(tk.END, message + "\n")
    output_text.see(tk.END)


def clear_output():
    output_text.delete("1.0", tk.END)


# ================= MODULE RUNNERS =================
def run_port_scan():
    clear_output()
    target = target_entry.get()

    if not target:
        messagebox.showerror("Error", "Enter target IP / Host")
        return

    threading.Thread(
        target=start_port_scan,
        args=(target, 1, 100, log_output),
        daemon=True
    ).start()


def run_banner_grab():
    clear_output()
    target = target_entry.get()

    if not target:
        messagebox.showerror("Error", "Enter target IP / Host")
        return

    threading.Thread(
        target=grab_banner,
        args=(target, 9090, log_output),
        daemon=True
    ).start()


def run_bruteforce():
    clear_output()

    log_output("[INFO] Starting Brute Force Attack Simulation...")
    log_output("[INFO] Monitoring authentication attempts...\n")

    usernames = ["admin", "user", "test"]
    passwords = ["1111", "2222", "wrongpass", "qwerty"]

    threading.Thread(
        target=brute_force_simulator,
        args=(usernames, passwords, log_output),
        daemon=True
    ).start()


def export_report():
    os.makedirs("reports", exist_ok=True)
    with open("reports/scan_report.txt", "w") as f:
        f.write(output_text.get("1.0", tk.END))
    messagebox.showinfo("Saved", "Report exported successfully")


# ================= GUI SETUP =================
root = tk.Tk()
root.title("Penetration Testing Toolkit")
root.geometry("780x560")

tk.Label(root, text="Target IP / Host").pack()
target_entry = tk.Entry(root, width=40)
target_entry.pack(pady=5)

tk.Button(root, text="Port Scan", command=run_port_scan).pack(pady=5)
tk.Button(root, text="Banner Grab", command=run_banner_grab).pack(pady=5)

tk.Button(
    root,
    text="Brute Force Attack Detection",
    command=run_bruteforce
).pack(pady=10)

tk.Button(root, text="Export Report", command=export_report).pack(pady=5)

output_text = tk.Text(root, height=16, width=95)
output_text.pack(pady=10)

root.mainloop()
