import os
import psutil
import platform
import shutil

try:
    import termuxapi
    IS_ANDROID = True
except importError:
    IS_ANDROID = False
    

def create_folder(folder_name):
    os.makedirs(folder_name, exist-ok = True)
    print(f"FOlder '{folder_name}' created.")

def create_file(filename, content = ""):
    with open(file_nae, "w")as f:
        f.write(content)
    print(f"File '{file_name}' created.")

def read_file(file_name):
    try:
        with open(file_name, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found!")

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted.")
    except FileNotFoundError:
        print("File not found!")

def delete_folder(folder_name):
    try:
        shutil.rmtree(folder_name)
        print(f"FOlder '{folder_name}' deleted.")
    except FIleNotFoundError:
        print("FOlder not found!")

def system_info():
    print("\n--- System Information ---")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    print(f"Architecture: {platform.architecture()[0]}")

def memory_info():
    ram = psutil.virtual_memory()
    storage = shutil.disk_usage("/")
    print("\n--- Memory Status ---")
    print(f"Total RAM: {ram.total / (1024**3):.2f} GB")
    print(f"Available RAM: {ram.available / (1024**3):.2f} GB")
    print(f"Total Storage: {storage.total / (1024**3):.2f} GB")
    print(f"Used Storage: {storage.used / (1024**3):.2f} GB")
    print(f"Free Storage: {storage.free / (1024**3):.2f} GB")

def battery_status():
    if IS_ANDROID:
        battery = termux_api.battery_status()
        print(f"\nBattery: {battery['percentage']}%")
    elif hasattr(psutil, "sensors_battery"):
        battery = psutil.sensors_battery()
        if battery:
            print(f"\nBattery: {battery.percent}%")
        else:
            print("\nBattery info not available.")
    else:
        print("\nBattery info not available.")
        
def installed_packages():
    print("\n--- Installed Packages ---")
    os.system("pip list")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Create Folder")
        print("2. Create File")
        print("3. Read File")
        print("4. Delete File")
        print("5. Delete Folder")
        print("6. System Info")
        print("7. Memory Info")
        print("8. Battery Status")
        print("9. Installed Packages")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            folder = input("Enter folder name: ")
            create_folder(folder)
        elif choice == "2":
            file = input("Enter file name: ")
            content = input("Enter content (optional): ")
            create_file(file, content)
        elif choice == "3":
            file = input("Enter file name: ")
            read_file(file)
        elif choice == "4":
            file = input("Enter file name: ")
            delete_file(file)
        elif choice == "5":
            folder = input("Enter folder name: ")
            delete_folder(folder)
        elif choice == "6":
            system_info()
        elif choice == "7":
            memory_info()
        elif choice == "8":
            battery_status()
        elif choice == "9":
            installed_packages()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
