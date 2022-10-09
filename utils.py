
def read(fp):
    with open(fp, 'r') as rf:
        return rf.read()

def readlines(fp):
    with open(fp, 'r') as rf:
        return [l.strip() for l in rf.readlines()]