import os, sys
arg = sys.argv[1] # primer argumento

os.system("python " + 
    os.path.join(
        f"C:{os.path.sep}",
        "Users","Ramón","AppData",
        "Local","Programs","Python",
        "Python37-32","Lib","site-packages",
        "PyQt4","uic", "pyuic.py"
        ) + f" {arg}")