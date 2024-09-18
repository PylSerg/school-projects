import keyboard

print(f"\n Key  ==>  Code \n")

def on_key_event(event):
    print(f"{event.name}  ==>  {event.scan_code} \n")

keyboard.hook(on_key_event)
keyboard.wait()
