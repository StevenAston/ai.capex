"""Build the self-contained reading page and downloadable research files."""
from pathlib import Path
import runpy, shutil
root=Path(__file__).resolve().parent
source=root/"sites/shadow-capital-narrative"
runpy.run_path(str(source/"build.py"),run_name="__main__")
for path in (source/"dist").iterdir():
    if path.is_file():shutil.copy2(path,root/path.name)
