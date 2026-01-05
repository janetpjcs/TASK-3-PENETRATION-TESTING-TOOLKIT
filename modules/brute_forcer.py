import time

def brute_force_simulator(usernames, passwords, output_callback):
    correct_user = "admin"
    correct_pass = "admin123"

    for user in usernames:
        for pwd in passwords:
            output_callback(f"[BRUTE] Trying {user}:{pwd}")
            time.sleep(0.4)

            if user == correct_user and pwd == correct_pass:
                output_callback(f"[SUCCESS] Valid credentials found -> {user} : {pwd}")
                return

    output_callback("[FAILED] No valid credentials found")
