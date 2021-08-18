import shutil
import sys

from typing import List
from pathlib import Path

from docutils.core import publish_parts
from markdown import markdown

from ssg.content import content

#help convert Markdown and ReStructuredText to HTML
class Parser:
    extensions: List[str] = []

    #check whether certain files have a parser
    #since part of the Parser methods, it dose not accpet 'self' as an argument
    def valid_extension(self, extension):
        return extension in self.extensions

    #implemented in any subclass
    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    #read the contents of a file
    def read(self, path):
        with open(path, "r") as file:
            return file.read()

    #needs to contain the full path to the file being written to
    def write(self, path, dest, content, ext='.html'):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, "w") as file:
            file.write(content)

    #copy resources to the correct location
    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))

#subclass of Parser
class ResourceParser(Parser):
    extensions = ['.jpg', '.png', '.gif', '.css', '.html']

    def parse(self, path, source, dest):
        self.copy(path, source, desr)

class MarkdownParser(Parser):
    extensions = [".md", ".markdown"]

    def parse(self, path, source, dest):
        content = Content.load(self.read(path))
        html = markdown(content.body)
        self.write(path, dest, html)
        sys.stdout.write("\x1b[1;32m{} converted to HTML. Metadata: {}\n".format(path.name, content))

class ReStructuredTextParser(Parser):
    extensions = [".rst"]

    def parse(self, path, source, dest):
        content = Content.load(self.read(path))
        html = publish_parts(content.body, writer_name="html5")
        self.write(path, dest, html["html_body"])
        sys.stdout.write("\x1b[1;32m{} converted to HTML. Metadata: {}\n".format(path.name, content))
