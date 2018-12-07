init-tests: .venv
	.venv/bin/pip install '.[tests]'
	ln -fs 'tests/pytest.ini' 'pytest.ini'

clean-tests:
	find . -name '.hypothesis' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +

check-tests: .venv
	.venv/bin/pytest --quiet --tb=line | grep ".py" || true

commit-tests: test;

test: .venv
	.venv/bin/pytest
