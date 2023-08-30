class File:
    def __init__(self, name):
        self.name = name
        self.content = ""

class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = []
        self.files = []

class FileSystemSimulator:
    def __init__(self):
        self.root = Directory("root")
        self.current_directory = self.root

    def ls(self):
        items = [item.name for item in self.current_directory.subdirectories + self.current_directory.files]
        return "\n".join(items)

    def mkdir(self, directory_name):
        new_directory = Directory(directory_name)
        self.current_directory.subdirectories.append(new_directory)

    def cd(self, directory_name):
        if directory_name == "..":
            if self.current_directory != self.root:
                self.current_directory = self.root
            return

        for directory in self.current_directory.subdirectories:
            if directory.name == directory_name:
                self.current_directory = directory
                return

        print(f"Directory '{directory_name}' not found.")

    def touch(self, file_name):
        new_file = File(file_name)
        self.current_directory.files.append(new_file)


if __name__ == "__main__":
    fs = FileSystemSimulator()

    while True:
        command = input(f"{fs.current_directory.name}> ")
        parts = command.split()

        if parts[0] == "ls":
            print(fs.ls())
        elif parts[0] == "mkdir":
            fs.mkdir(parts[1])
        elif parts[0] == "cd":
            fs.cd(parts[1])
        elif parts[0] == "touch":
            fs.touch(parts[1])
        elif parts[0] == "exit":
            break
        else:
            print("Invalid command.")

