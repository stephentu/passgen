all: p.pdf

p.pdf: p.tex 
	pdflatex -shell-escape p.tex

.PHONY: clean
clean:
	rm -f *.aux p.{aux,bbl,lof,log,lot,pdf,toc}
