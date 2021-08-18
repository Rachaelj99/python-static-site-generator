from pathlib import Path

class Site:

    #constructor that accepts 3 arugments
    #instance attributes = prefixed with self
    def __init__(self, source, dest, parsers=None):
        #convert source to a Path object
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = parsers or []

    def create_dir(self, path):
        #contains the full path to the destination folder
        directory = self.dest / path.relative_to(self.source)
        #want 'directory' to be replaced if it exists
        directory.mkdir(parents=True, exist_ok=True)

    def load_parser(self, extension):
        for parser in self.parsers:
            if parser.valid_extension(extension):
                return parsers

    def run_parser(self, path):
        parser = self.load_parser(path.suffix)
        if parser is not None:
            parser.parse(path, self.source, self.dest)
        else:
            print("Not Implemented")

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        #iterate through the paths of self.source.rglob("*")
        for path in self.source.rglob("*"):
            #if current path is  a directory
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                self.run_parser(path)
