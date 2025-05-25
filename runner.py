import pyautogui
import pydirectinput
import time
import asyncio

time.sleep(2)

def restart():
   pyautogui.moveTo(1859, 1307)
   pyautogui.mouseDown()
   pyautogui.mouseUp()

async def PrestigeTime():
    while True:
        try:
            xp = pyautogui.locateOnScreen("C:/Users/cclen/Desktop/Python/ObeliskMiner/Pics/84.png", confidence=0.9)
        except Exception as e:
            print("Not yet level 100! Trying again shortly")
            xp = None
        if xp is None:
            await asyncio.sleep(30)
            continue

        if xp:
            print("Time for a reset")
            pyautogui.moveTo(1714, 862) #Move to sell button
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.moveTo(1978, 1238) #Move to actual sell button inside menu, and double click to sell all
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            await asyncio.sleep(1) #Quick wait to not overload game too quickly
            pyautogui.moveTo(1859, 1303) #Move to the X button for menu reset
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            await asyncio.sleep(1) #Quick wait to not overload game too quickly
            pyautogui.moveTo(1423, 283) #Move to the prestige menu button
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            await asyncio.sleep(.2) 
            pyautogui.moveTo(1767, 559) #move to the Prestige button within the menu
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.moveTo(1859, 1307) #Move to the X for a menu reset
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            await asyncio.sleep(.5)
            pyautogui.moveTo(1567, 863) #Move to Upgrades tab
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            await asyncio.sleep(1)
            pyautogui.moveTo(2028, 1244) #Move to upgrade pickaxe menu option
            pydirectinput.mouseDown()
            pydirectinput.mouseUp()
            pydirectinput.mouseDown()
            pydirectinput.mouseUp()
            pydirectinput.moveRel(0, 1)
            pydirectinput.mouseDown()
            pydirectinput.mouseUp()
            pydirectinput.mouseDown()
            pydirectinput.mouseUp()
            pydirectinput.moveRel(0, 1)
            pydirectinput.moveRel(0, 1)
            await asyncio.sleep(.5)
            pydirectinput.doubleClick()  #Purchase all complete
            pyautogui.moveTo(1859, 1306) #Menu Reset
            pyautogui.mouseDown()
            pyautogui.mouseUp()
        else:
            print("Nah, no chance")

        await asyncio.sleep(25)

async def Store_Collect():
    while True:
        store_pixel = pyautogui.pixel(2163, 1292)

        if store_pixel == (16, 178, 66):
            print("Store ready.. collecting...")
            pyautogui.moveTo(2150, 1312)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.moveTo(2026, 678)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            await asyncio.sleep(0.2)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            await asyncio.sleep(0.2)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.moveTo(1859, 1307)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
        else:
            print("Store not ready.. Looping around.")

        await asyncio.sleep(20)  # Wait 20 minutes before rechecking
       
async def main():
   await asyncio.gather(
      Store_Collect(),
      PrestigeTime()
   )

print("Starting in 2 seconds...")
time.sleep(2)
looptimes = 10000

if looptimes >= 0:
    asyncio.run(main())
    looptimes -= 1
