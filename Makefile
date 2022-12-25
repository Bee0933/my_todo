install:
	# install dependencies
	pip install --upgrade pip &&\
		pip install -r requirements.txt 
format:
	# format python code with black
	black *.py 
lint:
	# check code syntaxes
	pylint --disable=R,C *.py 
test:
	# unit tests
	
build:
	# build docker container
	
run:
	# run docker
	
deploy:
	# deploy application
	
all: install format lint test deploy 