import re
import time
import pyperclip
from pynput import mouse
from pynput.keyboard import Controller, Key

keyboard = Controller()

def clean_clipboard():
    text = pyperclip.paste()
    # هر چیزی غیر از رقم را حذف کن (+ - ( ) فاصله و حروف)
    digits_only = re.sub(r"\D", "", text)
    pyperclip.copy(digits_only)
    print(f"تمیز شد \u2192 {digits_only!r}")

def paste_clipboard():
    # شبیه‌سازی Ctrl+V
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    print("پیست شد")

def on_click(x, y, button, pressed):
    if not pressed:
        return
    if button == mouse.Button.x2:      # کلید فوروارد \u2192 تمیز کردن کلیپ‌بورد
        clean_clipboard()
    elif button == mouse.Button.x1:    # کلید بک \u2192 پیست کردن
        # کمی تأخیر تا کلیک ماوس تمام شود
        time.sleep(0.05)
        paste_clipboard()

print("برنامه فعال است:")
print("\u2022 کلید فوروارد ماوس \u2192 کلیپ‌بورد را تمیز می‌کند")
print("\u2022 کلید بک ماوس \u2192 پیست می‌کند (Ctrl+V)")
print("برای خروج: Ctrl+C")

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
