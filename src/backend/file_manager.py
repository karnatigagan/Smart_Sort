import os
import shutil
def move_file(src_path, dest_folder):
    """
    Moves a file from src_path to dest_folder.
    Creates the destination folder if it doesn't exist.
    """
    try:
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        shutil.move(src_path, dest_folder)
        print(f"Moved file {src_path} to {dest_folder}")
    except Exception as e:
        print(f"Error moving file: {e}")
























# import os
# import shutil

# # Helper function to move file to the appropriate category folder
# def move_file(src_path, dest_folder):
#     if not os.path.exists(src_path):
#         print(f"Source file not found: {src_path}")
#         return

#     if not os.path.exists(dest_folder):
#         os.makedirs(dest_folder)

#     try:
#         filename = os.path.basename(src_path)
#         dest_path = os.path.join(dest_folder, filename)
#         if os.path.exists(dest_path):
#             base, ext = os.path.splitext(filename)
#             counter = 1
#             new_dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
#             while os.path.exists(new_dest_path):
#                 counter += 1
#                 new_dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
#             dest_path = new_dest_path

#         shutil.move(src_path, dest_path)
#         print(f"Moved file {src_path} to {dest_path}")
#     except Exception as e:
#         print(f"Error moving file: {e}")












# # Path: src/backend/file_manager.py

# import os
# import shutil

# # Helper function to move file to the appropriate category folder
# def move_file(src_path, dest_folder):
#     # Ensure the source file exists before trying to move it
#     if not os.path.exists(src_path):
#         print(f"Source file not found: {src_path}")
#         return

#     # Create the destination directory if it doesn't exist
#     if not os.path.exists(dest_folder):
#         os.makedirs(dest_folder)  # Create the directory if it doesn't exist

#     try:
#         filename = os.path.basename(src_path)
#         dest_path = os.path.join(dest_folder, filename)

#         # Check if file already exists in destination and append a number if so
#         if os.path.exists(dest_path):
#             base, ext = os.path.splitext(filename)
#             counter = 1
#             new_dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
#             while os.path.exists(new_dest_path):
#                 counter += 1
#                 new_dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
#             dest_path = new_dest_path

#         # Move the file
#         shutil.move(src_path, dest_path)
#         print(f"Moved file {src_path} to {dest_path}")
#     except Exception as e:
#         print(f"Error moving file: {e}")



















# import os
# import shutil

# # Move file to destination folder, handling file name conflicts
# def move_file(src_path, dest_folder):
#     # Ensure the destination folder exists
#     if not os.path.exists(dest_folder):
#         os.makedirs(dest_folder)

#     # Get the base name of the file (e.g., "file.txt")
#     file_name = os.path.basename(src_path)
#     dest_path = os.path.join(dest_folder, file_name)

#     # Check if the file already exists at the destination
#     if os.path.exists(dest_path):
#         # Create a new file name to avoid overwriting
#         base, ext = os.path.splitext(file_name)
#         count = 1
#         while os.path.exists(dest_path):
#             new_file_name = f"{base}_{count}{ext}"
#             dest_path = os.path.join(dest_folder, new_file_name)
#             count += 1

#     try:
#         # Move the file to the destination
#         shutil.move(src_path, dest_path)
#         print(f"Moved file {src_path} to {dest_path}")
#     except Exception as e:
#         print(f"Error moving file: {e}")





# import os
# import shutil

# def move_file(src_path, dest_folder):
#     """
#     Moves a file to the destination folder. If the destination folder doesn't exist, it will be created.
#     """
#     # Ensure the destination folder exists
#     if not os.path.exists(dest_folder):
#         print(f"Destination folder {dest_folder} doesn't exist. Creating it...")
#         os.makedirs(dest_folder)  # Create the folder if it doesn't exist
    
#     # Try to move the file to the destination folder
#     try:
#         shutil.move(src_path, dest_folder)
#         print(f"Moved file {src_path} to {dest_folder}")
#     except Exception as e:
#         print(f"Error moving file: {e}")











# import os
# import shutil

# def move_file(src_path, dest_folder):
#     """
#     Moves a file from src_path to dest_folder.
#     Creates the destination folder if it doesn't exist.
#     """
#     try:
#         if not os.path.exists(dest_folder):
#             os.makedirs(dest_folder)
#         shutil.move(src_path, dest_folder)
#         print(f"Moved file {src_path} to {dest_folder}")
#     except Exception as e:
#         print(f"Error moving file: {e}")


        