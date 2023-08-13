import psutil
import win32gui
import time

def is_application_background(pid):
    try:
        # Get process handle
        handle = win32gui.OpenProcess(1, False, pid)
        # Get process window title
        window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        # Check if the window is empty or non-existent
        if not window_title or window_title == "":
            return True
        # Check if the process is running but not in focus
        if win32gui.GetForegroundWindow() != handle:
            return True
    except:
        pass
    return False

def detect_background_applications():
    # Get list of all running processes
    processes = psutil.process_iter()
    for process in processes:
        pid = process.pid
        if is_application_background(pid):
            print("Background Application Detected: PID", pid, "Name:", process.name())

if __name__ == "__main__":
    while True:
        detect_background_applications()
        time.sleep(3)  # Check every 5 seconds
