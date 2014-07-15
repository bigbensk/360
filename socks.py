import os
import re
import sys

def ifconfig_reg():
    dic = {}
    content = os.popen('ifconfig')
    for line in content:
        if line[0] != ' ' and line[0] != '\n':
            nc = line.split()[0]
            line = content.next()
            if line:
                se = re.search(r'inet addr:((\d*\.){3}\d*)', line)
                ip = se.group(1)
                dic[nc] = ip
    print dic
        
if __name__ == '__main__':
    ifconfig_reg()