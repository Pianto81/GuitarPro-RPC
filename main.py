import pypresence
import time
import subprocess
from dotenv import dotenv_values
from pywinauto import Desktop
import threading

def runGP():
    subprocess.run(dotenv_values(".env")["EXECUTABLE"])


def main():
    time.sleep(2) # In order to sync with the runGP() function
    GP_VERSION = dotenv_values(".env")["VERSION"]
    def get_file_name():
        windows = Desktop(backend="uia").windows()
        for w in windows:
            if f"Guitar Pro {GP_VERSION}" in w.window_text(): # Gets the name of the window to return the name of the file
                return w.window_text()[15:]

    client_id = dotenv_values(".env")["CLIENT_ID"] # Returns the CLIENT_ID property of the .env file (put your client ID in the .env file)
    filename = get_file_name()
    timer = [0,0,0] # h,m,s
    refreshTime = 1 # in seconds

    rpc = pypresence.Presence(client_id=client_id)
    rpc.connect()

    while True:
        if filename == None or filename == "": # if GuitarPro is not running anymore
            break

        time.sleep(refreshTime)
        timer[0] += refreshTime

        if timer[0] == 60: # not optimised thing to make a hh/mm/ss format
            timer[0] = 0
            timer[1] += 1
            filename = get_file_name()
            if timer[1] == 60:
                timer[1] = 0
                timer[2] += 1

        rpc.update(state=f"Currently editing: {filename}",
                   details=f"{timer[2]}h {timer[1]}m {timer[0]}s elapsed",
                   large_image="guitarpro",
                   large_text=f"Guitar Pro {GP_VERSION}"
                   )


# Run the app discord rpc server at the same time

gpThread = threading.Thread(target=runGP)
mainThread = threading.Thread(target=main)


gpThread.start()
mainThread.start()
