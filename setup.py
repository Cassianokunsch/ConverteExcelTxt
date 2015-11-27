import sys
from cx_Freeze import setup, Executable

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Leds Conversor",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]LedsConversor.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {'data': msi_data}
build_exe_options = {"packages": ["os", "pandas", "threading", "sys"], "include_files": ["View\\", "Controle\\", "icone.ico"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "ConversorLeds",
        version = "0.1",
        description = "Conversor de Xlsx para txt.",
        options = {"build_exe": build_exe_options,"bdist_msi": bdist_msi_options},
        executables = [Executable("LedsConversor.py", base=base)])


