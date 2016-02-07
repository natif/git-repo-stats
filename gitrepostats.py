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
    users.append(line.strip())

users_set = set(users)
print(users_set)