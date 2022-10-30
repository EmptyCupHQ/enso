from setuptools import setup

setup(
    name="enso",
    version=0.1,
    py_modules=["utils", "cli"],
    install_requires=[
        "Click",
    ],
    entry_points="""
    [console_scripts]
    enso=cli:ensocli
    """,
)
