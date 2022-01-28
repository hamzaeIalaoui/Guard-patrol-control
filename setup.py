import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"
 
executables = [Executable("main.py", base=base, target_name="ATGASCR.exe")]

setup (
    name="ATGASCR",
    version="1.0",
    description="Application de Traitement et Gestion des Alertes pour un système de contrôle de rondes",
    options=options,
    executables=executables,
)
