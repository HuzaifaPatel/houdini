make:
	latexmk -shell-escape -pdf -pdflatex="pdflatex %O %S" thesis.tex
	makeglossaries thesis
	latexmk -shell-escape -pdf -pdflatex="pdflatex %O %S" thesis.tex
	latexmk -shell-escape -pdf -pdflatex="pdflatex %O %S" thesis.tex
clean:
	rm thesis.aux  thesis.fdb_latexmk  thesis.fls  thesis.log thesis.alg thesis.blg thesis.glo thesis.ist thesis.acr thesis.glg thesis.gls thesis.acn thesis.bbl thesis.out