env:
	python3 -m venv .
	./bin/pip3 install numpy matplotlib PyQt5 opencv-python snakeviz open3d

run:
	./bin/python3 main.py

prof:
	./bin/python3 prof.py field_calculate.prof 1000
	./bin/snakeviz 1000_field_calculate.prof

clear:
	rm -rf ./bin
	rm -rf ./etc
	rm -rf ./include
	rm -rf ./lib
	rm -rf ./lib64
	rm -rf ./share
	rm -rf ./__pycache__
	rm -rf ./pyvenv.cfg