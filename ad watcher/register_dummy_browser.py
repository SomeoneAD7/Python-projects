import winreg

# IMPORTANT: Change this to the exact path where you saved your .exe
# Keep the 'r' before the string to handle backslashes correctly.

exe_path = r"C:\Users\HP\Desktop\programming\backend\Python\Mini projects\ad watcher\dist\dummy_browser.exe"

def create_key(path): 
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, path).Close()

def set_val(path, name, value): 
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_WRITE) as key: 
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)

# 1. Define how Windows should launch the app
create_key(r"Software\Classes\DummyBrowserHTM\shell\open\command") 
set_val(r"Software\Classes\DummyBrowserHTM", "", "Dummy Browser Handler") 
set_val(r"Software\Classes\DummyBrowserHTM", "URL Protocol", "") 
set_val(r"Software\Classes\DummyBrowserHTM\shell\open\command", "", f'"{exe_path}" "%1"')

# 2. Tell Windows this app is capable of handling web links
create_key(r"Software\Clients\StartMenuInternet\DummyBrowser\Capabilities\URLAssociations") 
set_val(r"Software\Clients\StartMenuInternet\DummyBrowser\Capabilities", "ApplicationName", "Dummy Browser") 
set_val(r"Software\Clients\StartMenuInternet\DummyBrowser\Capabilities\URLAssociations", "http", "DummyBrowserHTM") 
set_val(r"Software\Clients\StartMenuInternet\DummyBrowser\Capabilities\URLAssociations", "https", "DummyBrowserHTM")

# 3. Register the app in the Windows Default Apps list
with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\RegisteredApplications", 0, winreg.KEY_WRITE) as key: 
    winreg.SetValueEx(key, "DummyBrowser", 0, winreg.REG_SZ, r"Software\Clients\StartMenuInternet\DummyBrowser\Capabilities") 

print("Successfully registered as a web browser!")