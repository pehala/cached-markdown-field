default: dist

clean:
	rm -rf build django_composite_field.egg-info dist .tox

sdist:
	python setup.py sdist

bdist:
	python setup.py bdist

dist: clean sdist bdist

upload: dist
	python setup.py sdist bdist upload
