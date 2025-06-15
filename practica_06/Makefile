# compile code for figs
figs: make_figs.py
	@echo "Creating figs I vs theta from data/"
	@mkdir -p fig/
	python make_figs.py
	@echo "Figs created succesfully"


# Clean figs
clean-fig:
	rm -rf fig/