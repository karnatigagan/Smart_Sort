import sys
import os

# Add the 'src' directory (parent of this file) to the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from backend.os_detection import detect_os
from backend.file_monitor import start_monitoring

if __name__ == "__main__":
    os_type = detect_os()
    print(f"Operating System Detected: {os_type}")

    # Specify the folder you want to monitor (Downloads folder)
    folder_to_monitor = "/Users/gagankarnati/Downloads"  # Adjust for your OS
    
    print(f"Monitoring folder: {folder_to_monitor}")
    start_monitoring(folder_to_monitor)

# from backend.os_detection import detect_os
# from backend.file_monitor import start_monitoring

# if __name__ == "__main__":
#     os_type = detect_os()
#     print(f"Operating System Detected: {os_type}")

#     # Specify the folder you want to monitor (Downloads folder)
#     folder_to_monitor = folder_to_monitor = "/Users/gagankarnati/Downloads" #"/path/to/your/downloads"  # Update this path according to your OS
    
#     print(f"Monitoring folder: {folder_to_monitor}")
#     start_monitoring(folder_to_monitor)


# import sys
# import os

# # Add the src directory to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from backend.os_detection import detect_os
# from backend.file_monitor import start_monitoring

# if __name__ == "__main__":
#     os_type = detect_os()
#     print(f"Operating System Detected: {os_type}")

#     # Specify the folder you want to monitor (Downloads folder)
#     folder_to_monitor = "/Users/gagankarnati/Downloads"  # Update this path according to your OS
    
#     print(f"Monitoring folder: {folder_to_monitor}")
#     start_monitoring(folder_to_monitor)