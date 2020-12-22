import six.moves.urllib as urllib
from pathlib import Path

f = open("categories2.txt", "r")
categories=[]
strr=""
for i in f:
    strr=strr+i
categories=strr.split("\n")
print(categories)


def download(url, filename, path):
    if not Path(path).exists():
        Path(path).mkdir()
    fpath = Path(path) / filename
    opener = urllib.request.URLopener()
    opener.retrieve(url, str(fpath))
    return fpath

def download_recurse(url, path, categories):
    path = Path(path)
    for cat in categories:
        site = url + cat.replace(' ', '%20') + '.bin'
        fpath = download(site, cat + '.bin', path)
        print('downloaded: {} from {}'.format(fpath, site))



path="/home/shaashwatlobnikki/Desktop/caartonize_reality2/dataset"
url="https://storage.googleapis.com/quickdraw_dataset/full/binary/"
download_recurse(url, path, categories)