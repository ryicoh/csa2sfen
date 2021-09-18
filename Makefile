clean:
	rm -rf csa2sfen.egg-info dist

distribute-test:
	python setup.py sdist
	python setup.py bdist_wheel
	twine upload --repository testpypi dist/*
	open https://test.pypi.org/project/csa2sfen

distribute:
	python setup.py sdist
	python setup.py bdist_wheel
	twine upload --repository pypi dist/*
	open https://pypi.org/project/csa2sfen
