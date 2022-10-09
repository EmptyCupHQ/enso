from setuptools import setup

setup(
    name="ensocli",
    version=0.1,
    py_modules=["utils", "cli"],
    install_requires=[
        "Typer",
    ],
    entry_points="""
    [console_scripts]
    enso=cli:enso
    """,
)
