#!python3
"""
Created on Aug 10, 2013

@author: wT
"""

import sys
sys.dont_write_bytecode = True # It's just clutter for this small scripts
import os
from collections import OrderedDict

from unpack import get_wad_path, get_wix_path, backup_files


class File():
	"""
	Represents a file entry in the index file
	Only have one instance per filename
	This is probably an awful idea...
	"""
	_instances = {}

	def __new__(cls, *args, **kwargs):
		file_name = args[0]
		if not file_name in cls._instances.keys():
			cls._instances[file_name] = super().__new__(cls)
		elif len(args) == 4: # File exists but group is probably new, so add it
			cls._instances[file_name].add_group(args[3])
		return cls._instances[file_name]

	def __init__(self, filename, offset, size, group=None):
		self.filename = filename
		self.offset = int(offset)
		self.size = int(size)

		self.new_size = None
		self.new_offset = None
		self.should_repack = False
		if group:
			self.add_group(group)

	def add_group(self, group):
		if not hasattr(self, "groups"):
			self.groups = {group}
		else:
			self.groups.add(group)

def compare_file_size(orig_file_name, orig_size):
	""" Returns new_size - orig_size """
	for item in os.listdir("repack"):
		if item == orig_file_name:
			new_size = os.path.getsize(os.path.join("repack", item))
			if new_size != orig_size:
				return new_size - orig_size
	return 0

def scan_repack_dir(file_list):
	""" Check for stuff to repack, compare sizes and calculate new offsets """
	# TODO: Figure out elegant way to incorporate size comparison to this without any extra loops
	files_to_repack = [ item for item in os.listdir("repack") if os.path.isfile(os.path.join("repack", item)) ] # Aww yiss, list comprehensions
	for file in file_list:
		if file.filename in files_to_repack:
			file.should_repack = True
			size_difference = compare_file_size(file.filename, file.size)
			if size_difference:
				file.new_size = file.size + size_difference

def shift_offsets(file_list, item_index):
	changed_file = file_list[item_index] # The file that changed size
	print("{} size was {:,} bytes, new size {:,} bytes".format(changed_file.filename, changed_file.size, changed_file.new_size))
	size_difference = changed_file.size - changed_file.new_size #
	for file in file_list[item_index + 1:]: # Shift offsets off every file after it
		if file.new_offset:
			file.new_offset -= size_difference
		else:
			file.new_offset = file.offset - size_difference

def write_new_wad(processed_file_list, first_change):
	with open(get_wad_path(), mode='wb') as wad_file:
		with open(get_wad_path() + ".orig", mode="rb") as orig_wad_file:
			for file in processed_file_list:
				if file.should_repack:
					with open(os.path.join("repack", file.filename), mode='rb') as input_file:
						wad_file.write(input_file.read())
				else:
					orig_wad_file.seek(file.offset)
					wad_file.write(orig_wad_file.read(file.size))
	print("Wrote new .wad")


if __name__ == '__main__':
	backup_files()

	file_index = OrderedDict() # The original .wix file as dict
	processed_file_list = set() # I swear it'll be a list in a moment

	with open(get_wix_path() + ".orig", mode="r") as index_file:
		for line in index_file:
			if line.startswith("!group"):
				_, group_name = line.split()
				group = []
				file_index[group_name] = group
			else:
				file = File(*line.split())
				file.add_group(group_name)
				group.append(file)
				processed_file_list.add(file)

	processed_file_list = sorted(list(processed_file_list), key=lambda file: file.offset) # That's ugly

	scan_repack_dir(processed_file_list)

	first_change = None

	for index, file in enumerate(processed_file_list):
		if file.new_size:
			if not first_change:
				first_change = index
			shift_offsets(processed_file_list, index)
		elif file.should_repack: # In case the new file manages to be exactly the same size as before
			if not first_change:
				first_change = index

	# Write the updated .wad
	write_new_wad(processed_file_list, first_change)

	# Write the modified .wix
	with open(get_wix_path(), mode='w') as index_file:
		for group, items in file_index.items():
			index_file.write("!group {}\n".format(group))
			for item in items:
				index_file.write("{} {} {}\n".format(item.filename, item.new_offset or item.offset, item.new_size or item.size))

