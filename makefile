.PHONY: index delete_index install_requirements benchmark delete_benchmark start

index:
	@echo "Running index.py..."
	@python ./INDEXER/indexer.py
	@echo "Indexing complete."

delete_index:
	@echo "Deleting GENERATED_INDEX folder and its contents..."
	@rm -rf ./GENERATED_INDEX
	@rm -rf ./INDEXER/__pycache__
	@echo "Deletion complete."

install_requirements:
	@echo "Installing requirements..."
	@pip install -r ./REQUIREMENTS/requirements.txt
	@echo "Requirements installation complete."

benchmark:
	@echo "Running benchmarks..."
	@python ./runBenchmark.py
	@echo "Benchmarks complete."

delete_benchmark:
	@echo "Deleting GENERATED_INDEX folder and its contents..."
	@rm -rf ./GENERATED_BENCHMARK
	@echo "Deletion complete."
start:
	@echo "Starting TheSpoon..."
	@python ./__main__.py 1 > /dev/null 2> /dev/null
	@echo "TheSpoon stopped."