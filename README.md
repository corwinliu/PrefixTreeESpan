# PrefixTreeESpan

## Usage

### General

```
python main.py -i inputfile -o outputfile -s minsup
```

- -i Path to input file, default to 'test.in', test example in the paper
- -o Path to output file, default to 'test.out'
- -s MinSup for the frequent subtree, int type, default to '2'

### Specific data

```
make [data-type]-[test-type]
```

- [data-type] could be CSlog, D10, F5, T1M
- [test-type] could be 1, 2, 3


Example:
```
make CSlog-1
```

## Output

The output result is in the /output/ directory.

Each file correspond to [data-type]-[test-data] as described before.

## Report

This also contains a report written in TeX.

The LaTeX Source Code is in the /report/ directory.

Get the pdf by 'make' under the /report/ directory.

P.S. You need xelatex

## Reference

Lei Zou, Yansheng Lu, Huaming Zhang, and Rong Hu.
Prefixtreeespan: A pattern growth algorithm for mining embedded subtrees.
In Proceedings of the 7th international conference on Web Information Systems,
WISE’06, pages 499–505, Wuhan, China, 2006. Springer-Verlag.
