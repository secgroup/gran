GRAN
====

Gran, a security analyser for Grsecurity RBAC policies

### Requirements

* Python 2.7 or grater (but not 3.X) 
* [PLY][] module, available in most Linux distrubutions or by executing `easy_install ply`

### Usage

	usage: gran [-h] [-a] [-b] [-p PROCESSEDPOLICY] [-e ENTRYPOINTS] [-t TARGETS]
		    [-l LEARNCONFIG] [-d] [-v]
		    policy

	a security analyser for Grsecurity RBAC policies.

	positional arguments:
	  policy                policy file to be analyzed

	optional arguments:
	  -h, --help            show this help message and exit
	  -a, --admin           include administrative special roles in the analysis
	  -b, --bestcase        assume there are not setuid/setgid files in the system
	  -p PROCESSEDPOLICY, --processedpolicy PROCESSEDPOLICY
				write preprocessed policy to file, useful for
				debugging
	  -e ENTRYPOINTS, --entrypoints ENTRYPOINTS
				specify the entrypoints file
	  -t TARGETS, --targets TARGETS
				specify a file with sensitive targets
	  -l LEARNCONFIG, --learnconfig LEARNCONFIG
				specify the learn_config file to get sensitive targets
	  -d, --debug           enable debugging mode
	  -v, --version         show program's version number and exit

If no entrypoints file is provided, gran assumes all the roles in the policy
file paired with the default subject '/' as entry points. In case of no targets
specified, gran computes all the states and transitions and quits.

### Limitations

At the moment, the following RBAC features are supported:

* role modes: `u`, `g`, `s`, `A`
* role attributes: `role_transitions`
* subject modes: `o`
* subject attributes: `user_transition_allow`, `user_transition_deny`,
                      `group_transition_allow`, `group_transition_deny`
* object modes: `r`, `w`, `a`, `c`, `x`, `d`, `h`, `none`
* capabilities: `CAP_ALL`, `CAP_SETUID`, `CAP_SETGID`

The tool provides a limited support for wild-carded objects. Nested subjects
are not supported, since the learning system of Grsecurity does not account for
them.


[PLY]:   http://www.dabeaz.com/ply/
