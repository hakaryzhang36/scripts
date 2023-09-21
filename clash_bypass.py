import os
import io
from hak_log import log

FILE_NAME = "Sockboom.yaml"

PATH = "/Users/zhanghaijia/.config/clash/"

PY_PASS_HEADER = "\nbypass:\n"

HOST_LIST = [
    "119.28.13.121",
    "\"www.notion.so\"",
    "119.28.13.121",
    "\"msgstore.www.notion.so\"",
    "119.28.13.121", 
    "\"api.pgncs.notion.so\"",
    "119.28.13.121",
    "\"exp.notion.so\""
]

def writeBypass(file_path):
    input = open(file_path, "r")
    
    text = input.read()
    if text.find('bypass:') != -1:
        input.close()
        log.error('"bypass" config existed')
        return

    output = open(file_path, "+a")
    s = PY_PASS_HEADER

    for host in HOST_LIST:
        s = s + " - " + host + "\n"
    
    output.write(s)
    log.info('yeah! success!')


if __name__ == "__main__":
    print(PATH + FILE_NAME)
    if os.path.isfile(PATH + FILE_NAME):
        writeBypass(PATH + FILE_NAME)
    else:
        log.error('file not existed')