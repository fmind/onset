init-formats: .venv
	.venv/bin/pip install '.[formats]'
	ln -fs 'formats/black.ini' 'black.ini'

clean-formats: ;

check-formats: ;

commit-formats: format;

format: .venv
	.venv/bin/black --config='black.ini' .
