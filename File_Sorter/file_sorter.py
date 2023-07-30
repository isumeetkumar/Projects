import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the download directory path and the destination folders for different file types
DOWNLOAD_DIR = "C:\\Users\\trail\\Downloads"  # Replace with your actual download directory path
DESTINATION_FOLDERS = {
    ".jpg": "C:\\Users\\trail\\Downloads\\IMAGE",  # Replace with the appropriate folder paths
    ".mkv": "C:\\Users\\trail\\Downloads\\VIDEO",
    ".zip": "C:\\Users\\trail\\Downloads\\DOCUMENT",
    ".pdf": "C:\\Users\\trail\\Downloads\\PDF",
    ".exe": "C:\\Users\\trail\\Downloads\\Software",
}

# Delay time after the file is created before moving it (in seconds)
DELAY_AFTER_CREATED = 10

class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            time.sleep(DELAY_AFTER_CREATED)  # Add a delay after the file is created
            self.sort_file(event.src_path)

    def sort_file(self, file_path):
        file_name, file_extension = os.path.splitext(file_path)
        destination_folder = DESTINATION_FOLDERS.get(file_extension.lower())

        if destination_folder:
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Add error handling to check if the file still exists
            if os.path.exists(file_path):
                new_file_path = os.path.join(destination_folder, os.path.basename(file_path))
                try:
                    shutil.move(file_path, new_file_path)
                    print(f"Moved '{file_path}' to '{new_file_path}'")
                except FileNotFoundError:
                    print(f"Error: File '{file_path}' no longer exists. Skipped sorting.")
            else:
                print(f"Error: File '{file_path}' no longer exists. Skipped sorting.")

if __name__ == "__main__":
    event_handler = DownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path=DOWNLOAD_DIR, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
