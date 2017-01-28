.PHONY: clean run capture parse
.DEFAULT_GOAL := run

clean:
	rm -f *.xml *.csv

run: capture parse

capture: stream.xml

stream.xml:
	python capture.py

parse: streamdata.csv

streamdata.csv:
	python parse.py
