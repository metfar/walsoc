init:
	pip install --break-system-packages -r requirements.txt

test:
	nosetests --rednose tests
