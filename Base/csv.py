import os
import xml.dom.minidom

def data_dirs():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIRS = (
    os.path.join(BASE_DIR,'Data'),
    )
    d='/'.join(DATA_DIRS)
    return d


dom = xml.dom.minidom.parse(data_dirs()+"/system.xml")

root = dom.documentElement

cc = dom.getElementsByTagName('live')

live = cc[0]
print live.firstChild.data

