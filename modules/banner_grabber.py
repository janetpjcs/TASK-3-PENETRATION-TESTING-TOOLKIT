import socket

def grab_banner(target, port, output_callback):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((target, port))
        banner = s.recv(1024).decode(errors="ignore").strip()
        s.close()

        if banner:
            output_callback(f"[BANNER] Port {port}: {banner}")
        else:
            output_callback(f"[BANNER] Port {port}: No banner received")

    except Exception as e:
        output_callback(f"[BANNER] Port {port}: Failed to grab banner")
