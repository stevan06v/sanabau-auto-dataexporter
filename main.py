import pyautogui
IMAGE_PATH = "image"

def main():
    print(pyautogui.size()) 
    print(pyautogui.position()) 
    pyautogui.moveTo(519, 1060, duration = 1)
    pyautogui.press("win")
    pyautogui.write('Hello world!')  
    pyautogui.press('enter')
    pyautogui.sleep(1)

    
if __name__ == '__main__':
    main()