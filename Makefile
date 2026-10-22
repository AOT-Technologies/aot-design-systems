LINTER := @google/design.md@0.4.0
SYSTEM ?=
SYSTEM_ARG := $(if $(SYSTEM),--system $(SYSTEM),)

.PHONY: build verify

# Regenerate generated systems, then refresh plugin copies (all, or SYSTEM=<name>).
build:
	python3 scripts/build_design_md.py $(SYSTEM_ARG)
	python3 scripts/build_plugins.py $(SYSTEM_ARG)

# Run every system's checks (all, or SYSTEM=<name>).
verify:
	python3 scripts/verify.py $(SYSTEM_ARG) --linter $(LINTER)
