.PHONY: clean distclean run capture parse
.DEFAULT_GOAL := run

clean:
	rm -f *.xml *.csv

distclean: clean
	rm -f *.pyc

run: capture parse

capture: stream.xml

stream.xml:
	python capture.py

parse: streamdata.csv

streamdata.csv:
	python parse.py
