.PHONY: typehint
typehint:
	mypy part_2/iterable_object.py
	# mypy --ignore-missing-imports serc/

.PHONY: test
test:
	pytest tests/

.PHONY: lint
lint:
	pylint part_2/iterable_object.py

.PHONY: black
black:
	black --diff part_2/iterable_object.py
	# black -l 79 *.py

.PHONY: checklist
checklist: typehint lint black



.PHONY: clean
clean:
	find . -type f -name "*.pyc" | xargs rm -fr
	find . -type d -name __pycache__ | xargs rm -fr