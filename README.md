GRAN
====

Gran, a security analyser for Grsecurity RBAC policies

### Requirements

* Python 2.7 or greater (Python 3.X supported)
* [PLY][] module, available in most Linux distributions. It can also be
  installed manually by executing `easy_install ply`

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
	  -e ENTRYPOINTS, --entrypoints ENTRYPOINTS
				specify the entrypoints file
	  -t TARGETS, --targets TARGETS
				specify a file with sensitive targets
	  -l LEARNCONFIG, --learnconfig LEARNCONFIG
				specify the learn_config file to get sensitive targets
	  -d, --debug           enable debugging mode
	  -v, --version         show program's version number and exit

Targets file consists of sensitive path, one entry per line. In case of no
targets specified, gran computes all the states and transitions and quits.


Each line of the entry-points file has the following syntax:

	<stateA> [<stateB> <target>]

where `stateA` and `stateB` are triples of the form
`<role_name>:<type>:<subject>` and `target` is a sensitive path that should not
be leaked from stateA to stateB by an indirect flow.

If no entry-points file is provided, gran assumes all the roles in the policy
file paired with the default subject '/' as entry points.

Examples of targets and entry-points files can be found under `misc/`.

### Limitations

At the moment, the following Grsecurity RBAC features are supported:

* role modes: `u`, `g`, `s`, `A`
* role attributes: `role_transitions`
* subject modes: `o`
* subject attributes: `user_transition_allow`, `user_transition_deny`,
                      `group_transition_allow`, `group_transition_deny`
* object modes: `r`, `w`, `a`, `c`, `x`, `d`, `h`, `none`
* capabilities: `CAP_ALL`, `CAP_SETUID`, `CAP_SETGID`
* domains
* include, define and replace rules

The tool provides a limited support for wild-carded objects. Nested subjects
are not supported, since the learning system of Grsecurity does not account for
them.

[PLY]:   http://www.dabeaz.com/ply/
