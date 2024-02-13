.PHONY: index delete_index install_requirements

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

delete_benchmark: