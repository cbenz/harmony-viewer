.PHONY: clean flake8 jshint tests

all: clean flake8 jshint tests

clean:
	find -name "*.pyc" | xargs rm -f
	rm -rf cache/*

flake8:
	flake8 --max-line-length=120 --ignore=E123,E128 harmony_viewer

jshint:
	jshint harmony_viewer/static/*.js

tests:
	nosetests
