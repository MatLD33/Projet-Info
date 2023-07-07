from cx_Freeze import setup, Executable

base = None
executables = [Executable("main.py", base=base)]
packages = ["idna", "numpy", "matplotlib", "tkinter", "pandas", "datetime"]
options = {
    "build_exe": {
        "packages": packages,
    },
}

setup(
    name="ThermoGraph",
    options=options,
    version="1.0",
    description="Logiciel de visualisation de données thermiques",
    executables=executables,
)
