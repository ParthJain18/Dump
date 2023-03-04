import pyautogui
import time
import keyboard
# import math
# import threading

# def listener():
#     if keyboard.wait("q"):
#         threading.main_thread.stop()


time.sleep(3)


def main():
    pyautogui.moveTo(800,100)
    pyautogui.mouseDown(button= "primary")

    line_length = 250
    direction_x = 1
    direction_y = 1

    while True:

        factor= 0.95


        pyautogui.moveRel(line_length * direction_x, line_length * direction_y, 1)

        if direction_x == 1 and direction_y == 1:
            direction_x = -1
            direction_y = 1

        elif direction_y == 1 and direction_x == -1:   
            direction_x = -1
            direction_y = -1

        elif direction_x == -1 and direction_y == -1:
            direction_x = 1
            direction_y = -1

        else:
            direction_x = 1
            direction_y = 1

        # if direction_x == 1:
        #     direction_x = 0
        #     direction_y = 1

        # elif direction_y == 1:
        #     direction_x = -1
        #     direction_y =0

        # elif direction_x == -1:
        #     direction_x = 0
        #     direction_y = -1

        # elif direction_y == -1:
        #     direction_x = 1
        #     direction_y = 0


        line_length *= factor

        if keyboard.is_pressed('q'):
            pyautogui.mouseUp()
            break
main()
# t1 = threading.Thread(target=main)
# t1.start()
# keyboard.wait('q')
# t1.join()
