#!/usr/bin/env python

import sys
import os
import timeit
import subprocess

policy_base = """
role default
subject /
		/			h
		-CAP_ALL"""

policy_objs = """
		/				h
		/bin				x
		/dev				h
		/dev/null			w
		/dev/tty			rw
		/etc				r
		/etc/grsec			h
		/etc/shadow			h
		/etc/ssh			h
		/home				
		/lib				rx
		/lib/modules			h
		/proc/meminfo			r
		/usr				h
		/usr/bin			
		/usr/lib			rx
		/usr/share			h
		/usr/share/terminfo		r
		-CAP_ALL"""

fnull = None

def run_gran():
	#subprocess.call(["../gran", "policy"], stdout=fnull, stderr=fnull)
    subprocess.call(["../gran", "policy"])
		
def create_policy(rolen):
	policy = policy_base
	for role in range(rolen):
		policy += "\nrole tmpuser{} u\nsubject /\n{}\n".format(role, policy_objs)
	policy_file_h = open('policy', 'w')
	policy_file_h.write(policy)
	policy_file_h.close()

def main():
	global fnull

	fnull = open(os.devnull, 'w')
	for roles in range(0, int(sys.argv[1]), 10):
		create_policy(roles)
		time = timeit.Timer(stmt='run_gran()', setup='from __main__ import run_gran')
		print("{} {}".format(roles + 1, time.timeit(number=1)))
	fnull.close()
	os.remove('policy')

if __name__ == '__main__':
	main()
