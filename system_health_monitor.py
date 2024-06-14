import psutil
import logging

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
    return cpu_usage

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {memory_usage}%')
    return memory_usage

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'High disk usage detected: {disk_usage}%')
    return disk_usage

def check_running_processes():
    processes = [proc.info for proc in psutil.process_iter(['pid', 'name'])]
    return processes

def main():
    cpu_usage = check_cpu_usage()
    memory_usage = check_memory_usage()
    disk_usage = check_disk_usage()
    processes = check_running_processes()

    logging.info(f'CPU usage: {cpu_usage}%')
    logging.info(f'Memory usage: {memory_usage}%')
    logging.info(f'Disk usage: {disk_usage}%')
    logging.info(f'Running processes: {len(processes)}')

    # Print to console
    print(f'CPU usage: {cpu_usage}%')
    print(f'Memory usage: {memory_usage}%')
    print(f'Disk usage: {disk_usage}%')
    print(f'Running processes: {len(processes)}')

if __name__ == '__main__':
    main()
