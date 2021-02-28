import os

from zipfile import ZipFile
from tempfile import mkdtemp
from shutil import rmtree

DEFAULT_TMPDIR = mkdtemp(prefix="aaaaa-")


def extract_zip(zip_file, member=None, path=DEFAULT_TMPDIR):
    with ZipFile(zip_file) as zf:
        path = path or mkdtemp(prefix="00000-")
        if member:
            zf.extract(member, path=path)
        else:
            for m in zf.namelist():
                if m.endswith((".csv", ".json", ".parquet")):
                    zf.extract(m, path=path)

    return path if not member else os.path.join(path, member)
