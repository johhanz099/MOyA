# compile code for figs 1-3
figs: make_figs.py fig_fit.py
	@echo "==>> Creating figs R vs theta from data/"
	@mkdir -p fig/
	python make_figs.py
	@echo "Figs created succesfully"
	@echo "==>> Creating figs R vs theta with fit Malus from data/"
	python fig_fit.py
	@echo "Figs with fit Malus created succesfully"


# Clean figs
clean-fig:
	rm -rf fig/