#!/usr/bin/python

import subprocess

display_users_cmd = "git log --pretty=format:\" %an \""

def run_command(command):    
  popen = subprocess.Popen(command, stdout=subprocess.PIPE)
  lines_iterator = iter(popen.stdout.readline, b"")
  return lines_iterator;

commiters_list = []
commiters_iterator = run_command(display_users_cmd)

for line in commiters_iterator:
	commiters_list.append(line.strip().decode('utf-8'))

commiters = set(commiters_list)
lines_added_by_commiter = {}
lines_deleted_by_commiter = {}

for commiter in commiters:
	commit_lines = run_command("git log --author=\""+commiter+"\" --pretty=tformat: --numstat")
	lines_added = 0
	lines_deleted = 0 
	for commit_line in commit_lines:
		line_result = commit_line.split()
		if line_result:
			if "-" not in line_result[0]:
				lines_added += int(line_result[0])
			if "-" not in line_result[1]:
				lines_deleted += int(line_result[1])

	lines_added_by_commiter[commiter] = lines_added
	lines_deleted_by_commiter[commiter] = lines_deleted

commiters = sorted(commiters)

for commiter in commiters:
	print(commiter)
	print("Lines added: " + str(lines_added_by_commiter[commiter]))
	print("Lines deleted: " + str(lines_deleted_by_commiter[commiter]))
	subtraction = lines_added_by_commiter[commiter] - lines_deleted_by_commiter[commiter]
	print("Added-Deleted: " + str(subtraction))
	print("\n")

