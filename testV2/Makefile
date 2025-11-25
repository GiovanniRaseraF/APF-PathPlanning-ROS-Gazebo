env:
	python3 -m venv .
	./bin/pip3 install numpy matplotlib PyQt5 opencv-python snakeviz

prof:
	python3 -m venv .
	./bin/python3 prof.py field_calculate.prof 100
	snakeviz 100_field_calculate.prof