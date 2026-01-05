import socket
import threading

open_ports = []

def scan_port(target, port, output_callback):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((target, port)) == 0:
            open_ports.append(port)
            output_callback(f"[OPEN] Port {port}")
        s.close()
    except:
        pass

def start_port_scan(target, start_port, end_port, output_callback):
    open_ports.clear()
    output_callback(f"Starting port scan on {target}...\n")

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(
            target=scan_port,
            args=(target, port, output_callback)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    risk = "LOW"
    if len(open_ports) > 10:
        risk = "HIGH"
    elif len(open_ports) > 5:
        risk = "MEDIUM"

    output_callback(f"\nScan completed.")
    output_callback(f"Open ports: {open_ports}")
    output_callback(f"Risk Level: {risk}")

    return open_ports, risk
