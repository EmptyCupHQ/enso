from cli import ensocli

@ensocli.group('bootstrap', short_help='command to bootstrap common projects')
def bootstrap():
    pass

@bootstrap.command('docs', short_help='Bootstrap a docs site using mkdocs')
def init_mkdocs():
    print('Creating directory...')
    print('Setting up virtualenv...')
    print('Installing mkdocs...')
    print('Updating mkdocs.yml...')