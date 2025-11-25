env:
	python3 -m venv .
	./bin/pip3 install numpy matplotlib PyQt5 opencv-python snakeviz

run:
	python3 -m venv .
	./bin/python3 main.py

prof:
	python3 -m venv .
	./bin/python3 prof.py field_calculate.prof 100
	snakeviz 100_field_calculate.prof