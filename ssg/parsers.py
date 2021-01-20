from typing import List
from pathlib import Path
import shutil

class Parser:

    def __init__(self):
        self.extensions:List[str] = []


    def valid_extension(self, extension):
        return (extension in self.extentions)


    def parse(self, path:Path, source:Path, dest:Path):
        raise NotImplementedError(f"This function Not Implemented")


    def read(self, path):
        with path.open() as f:
            return f.read()


    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name

        with full_path.open('w') as f:
            f.write(content)


    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):

    extensions:List[str] = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path:Path, source:Path, dest:Path):
        self.copy(path, source, dest)
