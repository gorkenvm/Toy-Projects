import pyautogui
import time

x, y = 933, 594

sayac = 10

while True:
    for i in range(0, sayac):
        pyautogui.click(x, y)
        time.sleep(0.3)

    cevap = pyautogui.confirm(
        text="Devam Etmek istiyormusun", title="mekatronik.com", buttons=["Hayır", "Evet"])

    if cevap == "Hayır":
        break
    else:
        while True:
            try:
                sayac = int(pyautogui.prompt(
                    "Daha Kaç Kişi Like İstiyorsun", title="mekatronik.com", default=""))
                break
            except ValueError:
                pyautogui.alert(text="Lütfen Tam Sayı gir",
                                title="mekatronik.com", button="Tamam")
