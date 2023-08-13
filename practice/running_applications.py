import psutil

def get_running_applications():
    running_apps = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            print(proc)
            if proc.info['name']:
                running_apps.append(proc.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return running_apps

# Example usage
running_applications = get_running_applications()
for app in running_applications:
    print(app)
