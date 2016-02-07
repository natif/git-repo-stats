#!/usr/bin/python

import subprocess

display_users_cmd = "git log --pretty=format:\" %an \""

def execute(command):    
  popen = subprocess.Popen(command, stdout=subprocess.PIPE)
  lines_iterator = iter(popen.stdout.readline, b"")
  return lines_iterator;

users = []

users_iterator = execute(display_users_cmd)

for line in users_iterator:
	users.append(line.strip().decode('utf-8'))

users_set = set(users)
users_dict_added = {}
users_dict_deleted = {}

for user in users_set:
	print("User: " + user)
	print("\n")
	file_lines = execute("git log --author=\""+user+"\" --pretty=tformat: --numstat")
	lines_added = 0
	lines_deleted = 0 
	for fline in file_lines:
		file_list = fline.split()
		if file_list:
			lines_added += int(file_list[0])
			lines_deleted += int(file_list[1])

	users_dict_added[user] = lines_added
	users_dict_deleted[user] = lines_deleted

print(users_set)
print(users_dict_added)
print(users_dict_deleted)