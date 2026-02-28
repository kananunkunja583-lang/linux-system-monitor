import psutil
import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def monitor():
    while True:
        clear()

        print("===== LINUX SYSTEM MONITOR =====\n")

        # CPU
        cpu = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu}%")

        # Memory
        memory = psutil.virtual_memory()
        print(f"Memory Usage: {memory.percent}%")

        # Disk
        disk = psutil.disk_usage('/')
        print(f"Disk Usage: {disk.percent}%")

        # Processes
        print("\nTop Processes:")
        processes = sorted(psutil.process_iter(['pid','name','cpu_percent']),
                           key=lambda p: p.info['cpu_percent'],
                           reverse=True)

        for p in processes[:5]:
            print(f"PID: {p.info['pid']} | {p.info['name']}")

        time.sleep(2)

if __name__ == "__main__":
    monitor()