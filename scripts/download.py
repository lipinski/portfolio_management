import os
import argparse
import wget
import zipfile


if __name__ == "__main__":
    gpw = 'https://info.bossa.pl/pub/ciagle/mstock/mstcgl.zip'
    target = gpw.split('/')[-1]
    wget.download(gpw, target)
    data_dir = 'data/gpw'

    if os.path.exists(data_dir):
        os.removedirs(data_dir)

    with zipfile.ZipFile(target) as zip_ref:
        zip_ref.extractall(data_dir)

    os.remove(target)

