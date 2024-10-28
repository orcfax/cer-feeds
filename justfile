# CLI Helpers

# Help
help:
	just -l

# Run all pre-commit checks
all-checks:
	pre-commit run --all-files

# Run pre-commit spelling check
spell:
	pre-commit run codespell --all-files

# Run pre-commit makdown-lint
markdown:
	pre-commit run markdownlint --all-files
