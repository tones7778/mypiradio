import subprocess

host = '0.0.0.0'
port = 5000
txtFile = 'stations.txt'
templateFile = 'interface.html'


def isInteger(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def mpcCommand(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    return p.stdout.read()
