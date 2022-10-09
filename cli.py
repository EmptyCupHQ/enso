import typer
import utils
from rich import print as display, markup

enso = typer.Typer()

@enso.command()
def mail(addrp:str, contentp:str):
    addrs = utils.readlines(addrp)
    content = utils.read(contentp)

    for addr in addrs:
        _send_mail(addr, content)



def _send_mail(addr, content):
    display("To: [purple]%s[/purple]" % addr)
    display("")
    display("[white]%s[/white]" % content)
    display("------------")


if __name__ == '__main__':
    enso()