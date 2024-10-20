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












# import sys
# import os
# from backend.os_detection import detect_os
# from backend.file_monitor import start_monitoring
# from ai.classifier_ai import classify_and_categorize_file

# # Ensure the correct directory is added to the Python path
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# if __name__ == "__main__":
#     os_type = detect_os()
#     print(f"Operating System Detected: {os_type}")

#     folder_to_monitor = "/Users/gagankarnati/Downloads"
#     print(f"Monitoring folder: {folder_to_monitor}")

#     start_monitoring(folder_to_monitor, classify_and_categorize_file)









# # Path: src/backend/file_monitor.py

# import os
# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler




# from ai.classifier_ai import classify_and_categorize_file  # AI-based classification
# from backend.file_manager import move_file  # Use existing backend file manager

# class FileHandler(FileSystemEventHandler):
#     def __init__(self, classifier):
#         self.classifier = classifier  # AI-based classifier

#     def on_created(self, event):
#         if not event.is_directory:
#             print(f"New file detected: {event.src_path}")
#             time.sleep(3)  # Increase delay to 3 seconds to ensure the file is fully written
#             try:
#                 category = self.classifier(event.src_path)  # Call the AI classifier
#                 dest_folder = f"/Users/gagankarnati/{category}"  # Update the path based on your system
#                 move_file(event.src_path, dest_folder)  # Move file based on AI category
#             except Exception as e:
#                 print(f"Error processing file: {e}")

# def start_monitoring(folder_to_monitor, classifier):
#     event_handler = FileHandler(classifier)
#     observer = Observer()
#     observer.schedule(event_handler, folder_to_monitor, recursive=False)
#     observer.start()
#     try:
#         while True:
#             pass
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()













# import sys
# import os
# from backend.os_detection import detect_os
# from backend.file_monitor import start_monitoring
# from ai.classifier_ai import classify_and_categorize_file  # AI-based classification

# # Add the 'src' directory (parent of this file) to the Python path
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# if __name__ == "__main__":
#     os_type = detect_os()
#     print(f"Operating System Detected: {os_type}")

#     # Specify the folder you want to monitor (Downloads folder)
#     folder_to_monitor = "/Users/gagankarnati/Downloads"  # Adjust for your OS
    
#     print(f"Monitoring folder: {folder_to_monitor}")
#     start_monitoring(folder_to_monitor, classify_and_categorize_file)  # Pass the AI classifier function







# import sys
# import os

# # Add the 'src' directory (parent of this file) to the Python path
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# from backend.os_detection import detect_os
# from backend.file_monitor import start_monitoring  # Keep using backend monitoring
# from ai.classifier_ai import classify_and_categorize_file  # Import AI classification

# if __name__ == "__main__":
#     os_type = detect_os()
#     print(f"Operating System Detected: {os_type}")

#     # Specify the folder you want to monitor (Downloads folder)
#     folder_to_monitor = "/Users/gagankarnati/Downloads"  # Adjust for your OS
    
#     print(f"Monitoring folder: {folder_to_monitor}")
    
#     # Start monitoring with AI-based classification
#     start_monitoring(folder_to_monitor, classify_and_categorize_file)






##working simple backend code. 
# import sys
# import os

# # Add the 'src' directory (parent of this file) to the Python path
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# from backend.os_detection import detect_os
# from backend.file_monitor import start_monitoring

# if __name__ == "__main__":
#     os_type = detect_os()
#     print(f"Operating System Detected: {os_type}")

#     # Specify the folder you want to monitor (Downloads folder)
#     folder_to_monitor = "/Users/gagankarnati/Downloads"  # Adjust for your OS
    
#     print(f"Monitoring folder: {folder_to_monitor}")
#     start_monitoring(folder_to_monitor)













#Previously used code NOT CURRENTLY IN USE.
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