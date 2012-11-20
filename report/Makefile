run:
	xelatex report.tex
	-bibtex report.aux
	xelatex report.tex
	xelatex report.tex
clean:
	find . -name '*.aux' -print0 | xargs -0 rm -rf
	rm -rf *.lof *.log *.lot *.out *.toc *.bbl *.blg *.thm
depclean: clean
	rm -rf *.pdf
