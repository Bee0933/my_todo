install:
	# install dependencies
	pip install --upgrade pip &&\
		pip install -r requirements.txt 
format:
	# format python code with black
	black *.py db/*.py endpoints/*.py endpoints/security/*.py schemas/*.py
lint:
	# check code syntaxes
	pylint --disable=R,C *.py db/*.py endpoints/*.py endpoints/security/*.py schemas/*.py
test:
	# unit tests
	
build:
	# build docker container
	
run:
	# run docker
	
deploy:
	# deploy application
	
all: install format lint test deploy 