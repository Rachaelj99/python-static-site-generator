from pathlib import path

class Site:

    #constructor that accepts 3 arugments
    #instance attributes = prefixed with self
    def __init__(self, source, dest):
        #convert source to a Path object
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        #contains the full path to the destination folder
        directory = self.dest / path.relative_to(self.source)
        #want 'directory' to be replaced if it exists
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        #iterate through the paths of self.source.rglob("*")
        for path in self.source.rglob("*"):
            #if current path is  a directory
            if path.is_dir():
                self.create_dir(path)
