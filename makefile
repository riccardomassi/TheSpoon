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

start: start_venv install_requirements
    @echo "Starting TheSpoon..."
    @./ENV/bin/python ./__main.py
    @echo "TheSpoon stopped."