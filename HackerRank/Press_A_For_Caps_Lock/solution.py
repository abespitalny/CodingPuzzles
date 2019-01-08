def pressAForCapsLock(message):
    s = ""
    # Caps Lock is initially off
    caps_lock = False
    for c in message:
        # Shift key is pressed if character is uppercase
        shift = c.isupper()
        if c == 'A' or c == 'a':
            # toggle Caps Lock when 'a' is pressed
            caps_lock = not caps_lock
        else:
            # Caps Lock is on
            if caps_lock:
                # if Shift key is pressed then character should be lowercase
                if shift:
                    s += c.lower()
                else:
                    s += c.upper()
            else:
                s += c

    return s
