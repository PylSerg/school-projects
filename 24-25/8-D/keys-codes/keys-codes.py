import keyboard
import time

last_time = 0

print(f"\n Key  ==>  Code \n")

def on_key_event(event):
    global last_time

    current_time = time.time()

    if current_time - last_time >= 1:
        print(f"{event.name}  ==>  {event.scan_code} \n")

        last_time = current_time
    #if
#def


keyboard.hook(on_key_event)
keyboard.wait()
