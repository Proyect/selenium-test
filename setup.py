from cx_Freeze import setup, Executable

setup(
    name = "mi_programa",
    version = "1.0",
    description = "Mi aplicación con Selenium",
    executables = [Executable("taking_of_absences.py")]
)
# python setup.py build