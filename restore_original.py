#!python3
"""
Created on Aug 12, 2013

@author: wT
@version: 1.1
"""

import sys
sys.dont_write_bytecode = True # It's just clutter for this small scripts
import os
import traceback

from unpack import check_for_correct_python, get_wad_path, get_wix_path


if __name__ == '__main__':
	try:
		check_for_correct_python()
		yesno = input(r"Overwrite both (potentially modified) .wad and .wix files with originals? [y/n]: ").lower()
		if yesno == "y" or yesno == "yes":
			os.replace(get_wad_path() + ".orig", get_wad_path())
			os.replace(get_wix_path() + ".orig", get_wix_path())
			print("Done")
		else:
			print("Not restoring")
	except SystemExit as e:
		print(e)
	except:
		traceback.print_exc()
