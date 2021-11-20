.PHONY: test ship scrape

scrape:
	pipenv run nwsaurora images --pole=north > data/images-north.json
	pipenv run nwsaurora images --pole=south > data/images-south.json
	pipenv run nwsaurora images --pole=north --latest > data/latest-image-north.txt
	pipenv run nwsaurora images --pole=south --latest > data/latest-image-north.txt
	pipenv run nwsaurora grid > data/grid.json
	pipenv run nwsaurora forecast > data/forecast.json

test:
	pipenv run flake8 ./
	pipenv run coverage run test.py
	pipenv run coverage report -m


ship:
	rm -rf build/
	rm -rf dist/
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload dist/* --skip-existing
