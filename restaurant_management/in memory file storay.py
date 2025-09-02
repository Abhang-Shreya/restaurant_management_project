# in_memory_file_storage.py

class InMemoryFileStorage:
    def __init__(self):
        # Dictionary to hold filename -> file content
        self.storage = {}

    def save_file(self, filename, content):
        """Save or overwrite a file in storage."""
        self.storage[filename] = content
        print(f"File '{filename}' saved successfully.")

    def get_file(self, filename):
        """Retrieve a file's content."""
        if filename in self.storage:
            return self.storage[filename]
        else:
            raise FileNotFoundError(f"File '{filename}' does not exist.")

    def delete_file(self, filename):
        """Delete a file from storage."""
        if filename in self.storage:
            del self.storage[filename]
            print(f"File '{filename}' deleted successfully.")
        else:
            raise FileNotFoundError(f"File '{filename}' does not exist.")

    def list_files(self):
        """List all stored files."""
        return list(self.storage.keys())


#Example Usage
if __name__ == "__main__":
    fs = InMemoryFileStorage()

    # Save files
    fs.save_file("profile_pic.png", b"binary_image_data")
    fs.save_file("report.txt", "This is a sample report.")

    # List files
    print("Files in storage:", fs.list_files())

    # Retrieve a file
    print("Report Content:", fs.get_file("report.txt"))

    # Delete a file
    fs.delete_file("profile_pic.png")
    print("Files after deletion:", fs.list_files())
