# Simulation Readme

The python code of interest is VirtualDeviceSimulator.py

## Installation

Install [Android Studio](https://developer.android.com/studio/?gclid=CjwKCAjwk6-LBhBZEiwAOUUDp8AQJFwBrEfgM57QCiYjmgVHyzGqMRj5eVwY39VveDIKxpPGnM5TohoCr4MQAvD_BwE&gclsrc=aw.ds), python, and pip3 on your local PC.

Next, you need to perform 

```bash
pip3 install pyautogui threading subprocess opencv-python
```
All other libraries are pre-built in python

### Locate Directories

We need to locate a couple folders and hardcode them into the file. The reason is when we perform multi-threading the directory is relative so we need absolute paths which you will need to adjust in the following lines.

```python
SdkToolsBin = "cd C:/Users/Michael/AppData/Local/Android/Sdk/tools/bin/"
pyFileDirectory = "C:/Users/Michael/Documents/FreeFood/"
avdConfigDirectory = "C:/Users/Michael/.android/avd/"
platformToolsDirectory = "cd C:/Users/Michael/AppData/Local/Android/Sdk/platform-tools"
emulatorDirectory = "cd C:/Users/Michael/AppData/Local/Android/Sdk/emulator"
```

Change these directory paths to the ones located on your pc. You have all of these folders.


