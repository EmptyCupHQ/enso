
def read(fp):
    with open(fp, 'r') as rf:
        return rf.read()

def readlines(fp):
    with open(fp, 'r') as rf:
        return [l.strip() for l in rf.readlines()]

red = lambda s: '[red]%s[/red]' % s
blue = lambda s: '[blue]%s[/blue]' % s
magenta = lambda s: '[magenta]%s[/magenta]' % s
cyan = lambda s: '[cyan]%s[/cyan]' % s
yellow = lambda s: '[yellow]%s[/yellow]' % s
