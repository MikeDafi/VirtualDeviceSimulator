import pyautogui
import os
import time
import subprocess
import win32clipboard
import threading
nameOfEmulator = "emu2"
nameOfEmulatorRaw = "emu2"
SdkToolsBin = "cd C:/Users/Michael/AppData/Local/Android/Sdk/tools/bin/"
pyFileDirectory = "C:/Users/Michael/Documents/FreeFood/"
avdConfigDirectory = "C:/Users/Michael/.android/avd/"
platformToolsDirectory = "cd C:/Users/Michael/AppData/Local/Android/Sdk/platform-tools"
emulatorDirectory = "cd C:/Users/Michael/AppData/Local/Android/Sdk/emulator"

# We will be changing these devices
#you can find the devices your computer supports by going to SdkToolsBin and avdmanager list device
device = {0 : "pixel",1:"Nexus 5",2:"Nexus 4",3:"Nexus 5X",4:"pixel_c",5:"Nexus S",6:"pixel_xl",7:"Nexus One",8:"wear_round",9:"tv_1080p"} #wear_round is the Android Wear Round and tv_1080p is the Google TV
done = False

def checkIfEmulatorExists(emulator):
    resultOutput = os.popen(SdkToolsBin + " && avdmanager list avd").read()
    return emulator in resultOutput

def getOS():
    f = open(pyFileDirectory + "OsNumber.txt", "r")
    osNumber = int(f.readline()) or 0
    f.close()
    f = open(pyFileDirectory + "OsNumber.txt", 'w')
    f.write(str((osNumber + 1) % 2))
    f.close()
    print(osNumber)

    return str(29 + osNumber)


def deleteAndCreateEmulator():
    print("deleteAndCreateEmulator")
    if(checkIfEmulatorExists(nameOfEmulator)):
        os.popen(SdkToolsBin + " && avdmanager delete avd -n " + nameOfEmulator)
    while(checkIfEmulatorExists(nameOfEmulator)):
        print("still deleting")
        time.sleep(1)
    osNumber = getOS()
    os.popen(SdkToolsBin +" && avdmanager create avd -n " + nameOfEmulator + " -k \"system-images;android-"+osNumber + ";google_apis_playstore;x86\" -g \"google_apis_playstore\" --device \"pixel\" --force")
    time.sleep(20)
    config = open(avdConfigDirectory + nameOfEmulatorRaw + ".avd/config.ini", "a")  # append mode
    config.write("hw.keyboard=yes \n")
    time.sleep(5)


def errorFunction(count,timeToTrigger,finalErrorMessage,temporaryErrorMessage):
    if(count == timeToTrigger):
        raise Exception(message)
    time.sleep(1)
    count += 1
    print(temporaryErrorMessage)
    return count

def openEmulator():
    print("open emulator")
    os.popen(emulatorDirectory + " && emulator @"+nameOfEmulator)
    count = 0
    while(not pyautogui.locateCenterOnScreen(pyFileDirectory + 'Android/EmulatorExists.PNG',confidence=0.9) and not pyautogui.locateCenterOnScreen(pyFileDirectory + 'Android/EmulatorExists2.PNG',confidence=0.9)):
        count = errorFunction(count,300,"No Emulator In View","Haven't Found Emulator on Desktop " + str(count) + " secs")

appMapping = {
    1 : "Wetzel",
    2 : "Auntie",
    3 : "Peets",
    4 : "Rais"
}

def checkIfEmulatorOnline(count):
    if count == 240: # 1 minute countdown
        raise Exception("No Emulator")
    output = os.popen(platformToolsDirectory + " && adb devices").read()
    if "emulator-" in output:
        return True
    return False

def installAppOfInterest(number):
    print("installing app" + appMapping[number])
    count = 0
    while(not checkIfEmulatorOnline(count)):
        errorFunction(count,240,"Couldn't Install App","Still Installing "+ appMapping[number])

    os.system(platformToolsDirectory + " && adb install "+ appMapping[number] + ".apk")


def openChromeAndCreateEmail():
    print("creating email")
    url = "https://10minutemail.com/"
    os.system('start chrome')
    time.sleep(2)
    # Maximize Window
    start = pyautogui.locateCenterOnScreen(pyFileDirectory + 'Chrome/MaximizeWindow.PNG',confidence=0.9) or pyautogui.locateCenterOnScreen(pyFileDirectory + 'Chrome/MaximizeWindow2.PNG',confidence=0.9)
    print(start)
    pyautogui.click(start)

    # Find Search Bar
    time.sleep(2)
    start = pyautogui.locateCenterOnScreen(pyFileDirectory + 'Chrome/SearchBar.PNG',confidence=0.9)
    pyautogui.click(start)
    pyautogui.write(url,interval=0.05)
    pyautogui.press('enter')
    while(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Chrome/BrowserLoaded.PNG',confidence=0.9) is None):
        time.sleep(0.25)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('c')

    # Minimize Window
    start = pyautogui.locateCenterOnScreen(pyFileDirectory + 'Chrome/MinimizeWindow.PNG',confidence=0.9) or pyautogui.locateCenterOnScreen(pyFileDirectory + 'Chrome/MinimizeWindow2.PNG',confidence=0.9)
    pyautogui.click(start)

def openAppFolder():
    print("open app")
    time.sleep(3)
    count = 0
    while(not pyautogui.locateCenterOnScreen(pyFileDirectory + 'Android/SearchBar.PNG',confidence=0.9)):
        count = errorFunction(count,300,"No HomeScreen Search Bar In View","Haven't Found HomeScreen Search Bar " + str(count) + " secs")
    start = pyautogui.locateCenterOnScreen(pyFileDirectory + 'Android/SearchBar.PNG',confidence=0.9)
    pyautogui.moveTo(start)
    pyautogui.drag(0,-400,1,button='left')

def infiniteLoopCheckForWait():
    while not done:
        print("infinite")
        if(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Android/Wait.PNG',confidence=0.9)):
            print("error Message to CLICK!!")
            pyautogui.click(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Android/Wait.PNG',confidence=0.9))

        if(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Android/Wait2.PNG',confidence=0.9)):
            print("error Message to CLICK!!")
            pyautogui.click(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Android/Wait2.PNG',confidence=0.9))

        if(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/LocationServices.PNG',confidence=0.9)):
            print("error Message to CLICK!!")
            pyautogui.click(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/LocationServices.PNG',confidence=0.9))

        if(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/LocationServices2.PNG',confidence=0.9)):
            print("error Message to CLICK!!")
            pyautogui.click(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/LocationServices2.PNG',confidence=0.9))
            
        if(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/LocationServices3.PNG',confidence=0.9)):
            print("error Message to CLICK!!")
            pyautogui.click(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/LocationServices3.PNG',confidence=0.9))

def openAnApp(number):
    count = 0
    while(not pyautogui.locateCenterOnScreen(pyFileDirectory + 'Android/' + appMapping[number] + '.PNG',confidence=0.9)):
        count = errorFunction(count,60,"No "+ appMapping[number] + "App Found","no " + appMapping[number] + " app found for " + str(count) + " secs")
    
    start = pyautogui.locateCenterOnScreen(pyFileDirectory + 'Android/' + appMapping[number] + '.PNG',confidence=0.9)
    print(pyFileDirectory + 'Android/' + appMapping[number] + '.PNG')
    pyautogui.click(start)

def createAWetzelsAccount():
    print("creating a wetzel's account")
    count = 0
    while(not pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/MoreTab.PNG',confidence=0.9)):
        count = errorFunction(count,60,"Wetzel's won't open","Wetzel's hasn't opened yet, waited " + str(count) + " secs")
    pyautogui.click(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/MoreTab.PNG',confidence=0.9))
    while(not pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/BeforeLogin.PNG',confidence=0.95)):
        time.sleep(1)
        print("Finding BeforeLogin Space")
    pyautogui.click(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/BeforeLogin.PNG',confidence=0.95))
    while(not pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/Login.PNG',confidence=0.95)):
        time.sleep(2)
        pyautogui.press('tab')
        print("Finding Login Button")
    pyautogui.click(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/Login.PNG',confidence=0.95))
    while(not pyautogui.locateCenterOnScreen(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/SignUpButton.PNG',confidence=0.95))):
        time.sleep(1)
        print("Finding SignUp Button")
    pyautogui.click(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/SignUpButton.PNG',confidence=0.95))
    time.sleep(15)
    pyautogui.write("Mic",interval=0.05)
    pyautogui.press('tab')
    time.sleep(5)
    pyautogui.write("James",interval=0.05)
    pyautogui.press('tab')
    time.sleep(5)
    pyautogui.write(getClipboardData(),interval=0.05)
    pyautogui.press('tab')
    # print(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/PasswordField.PNG',confidence=0.9))
    # pyautogui.click(pyautogui.locateCenterOnScreen(pyFileDirectory + 'Wetzel/PasswordField.PNG',confidence=0.9))
    time.sleep(4)
    pyautogui.write("Random1234",interval=0.05)
    pyautogui.press('tab')
    time.sleep(4)
    pyautogui.write("Random1234",interval=0.05)
    pyautogui.press('tab')
    time.sleep(4)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    for i in range(6):
        pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')

def getClipboardData():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

def begin():
    # openChromeAndCreateEmail()
    # deleteAndCreateEmulator()
    openEmulator()
    # installAppOfInterest(1)
    # openAppFolder()
    # openAnApp(1)
    # createAWetzelsAccount()
    # done = True

t1 = threading.Thread(target=infiniteLoopCheckForWait)
t1.daemon = True
t1.start()
begin()

