.PHONY: index deleteindex installrequirements benchmark deletebenchmark startvenv start

index: start_venv install_requirements
	@echo "Running index.py..."
	@./ENV/bin/python ./INDEXER/indexer.py
	@echo "Indexing complete."

delete_index:
	@echo "Deleting GENERATED_INDEX folder and its contents..."
	@rm -rf ./GENERATED_INDEX
	@rm -rf ./INDEXER/__pycache
	@echo "Deletion complete."

install_requirements: start_venv
	@echo "Installing requirements..."
	@./ENV/bin/pip install -r ./REQUIREMENTS/requirements.txt
	@echo "Requirements installation complete."

benchmark:
	@echo "Running benchmarks..."
	@./ENV/bin/python ./runBenchmark.py
	@echo "Benchmarks complete."

delete_benchmark:
	@echo "Deleting GENERATED_BENCHMARK folder and its contents..."
	@rm -rf ./GENERATED_BENCHMARK
	@echo "Deletion complete."

start_venv:
	@python -m venv ./ENV
	@echo "Virtual environment created."

install_nltk_data: install_requirements
	@echo "Installing NLTK corpus and stopwords..."
	@./ENV/bin/python -m nltk.downloader punkt stopwords wordnet
	@echo "NLTK corpus and stopwords installation complete."

start: start_venv install_requirements install_nltk_data
	@echo "Starting TheSpoon..."
	@./ENV/bin/python ./__main__.py
	@echo "TheSpoon stopped." 