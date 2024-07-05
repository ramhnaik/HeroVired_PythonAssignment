"""
Python program to monitor the health of the CPU
"""

import psutil


def monitor_cpu_health(threshold):
    """
    To monitor CPU usage continuously until keyboard interrupt sent by user

     Parameters:
        threshold : int
                  Password entered by user.
     Return : Nil

    """

    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=2)  # Monitor CPU utilization for 2 seconds
            print("CPU Usage: ", cpu_usage)
            if cpu_usage > threshold:
                print(f"Alert..! CPU usage exceeds threshold of {cpu_usage}%")
            print("Hit ctrl+c to stop monitoring process.")
    except KeyboardInterrupt:
        print("CPU usage monitoring stopped by user.")
    except Exception as error:
        print(f"ERROR: {error}")


if __name__ == "__main__":
    THRESHOLD_CPU_USAGE = 80
    monitor_cpu_health(THRESHOLD_CPU_USAGE)
