demo:
	python main.py -i test.in -s 2
CSlog-1:
	python main.py -i data/CSlog.data -o output/CSlog-1.out -s 5969
CSlog-2:
	python main.py -i data/CSlog.data -o output/CSlog-2.out -s 596
CSlog-3:
	python main.py -i data/CSlog.data -o output/CSlog-3.out -s 59
D10-1:
	python main.py -i data/D10.data -o output/D10-1.out -s 10000
D10-2:
	python main.py -i data/D10.data -o output/D10-2.out -s 1000
D10-3:
	python main.py -i data/D10.data -o output/D10-3.out -s 100
F5-1:
	python main.py -i data/F5.data -o output/F5-1.out -s 10000
F5-2:
	python main.py -i data/F5.data -o output/F5-2.out -s 1000
F5-3:
	python main.py -i data/F5.data -o output/F5-3.out -s 100
T1M-1:
	python main.py -i data/T1M.data -o output/T1M-1.out -s 100000
T1M-2:
	python main.py -i data/T1M.data -o output/T1M-2.out -s 10000
T1M-3:
	python main.py -i data/T1M.data -o output/T1M-3.out -s 1000
clean:
	find . -name '*.pyc' -print0 | xargs -0 rm -rf
	rm -rf test.out
