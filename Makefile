include */Makefile

MAKEFLAGS += --silent
MAKECONFS += $(wildcard */Makefile)
MAKEREPOS += $(subst /,, $(dir ${MAKECONFS}))

.DEFAULT_GOAL := check

.venv:
	python -m venv .venv --clear --symlinks

init:
	@for dir in ${MAKEREPOS} ; do make init-$$dir ; done

clean:
	@for dir in ${MAKEREPOS} ; do make clean-$$dir ; done

check:
	@for dir in ${MAKEREPOS} ; do make check-$$dir ; done

commit:
	@for dir in ${MAKEREPOS} ; do make commit-$$dir ; done
