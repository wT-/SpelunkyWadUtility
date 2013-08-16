#!python3
"""
Created on Aug 12, 2013

@author: wT
@version: 1.0
"""

import sys
sys.dont_write_bytecode = True # It's just clutter for this small scripts
import shutil
import traceback

from unpack import check_for_correct_python, get_wad_path, get_wix_path


if __name__ == '__main__':
	try:
		check_for_correct_python()
		yesno = input(r"Overwrite both (potentially modified) .wad and .wix files with originals? [y/n]: ").lower()
		if yesno == "y" or yesno == "yes":
			shutil.copy2(get_wad_path() + ".orig", get_wad_path())
			shutil.copy2(get_wix_path() + ".orig", get_wix_path())
			print("Done")
		else:
			print("Not restoring")
	except SystemExit as e:
		print(e)
	except:
		traceback.print_exc()
