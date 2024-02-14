<div align="center">
  <img width="200" height="200" src="https://github.com/riccardomassi/TheSpoon/blob/main/GUI/public/dark/dark-mode-logo.png">
</div>

## What is TheSpoon?
TheSpoon is a tool for searching trough restaurant reviews, built by food enjoyers for food enjoyers.

TheSpoon utilizes Sentiment Analysis and Information Retrieval techniques to allow users to search trough a selection of reviews of restaurants throughout the USA, accessible trough a JavaScript front-end.

## Requirements
Requirements are listed in the `/REQUIREMENTS/requirements.txt` file and can be installed by running `make install_requirements`

## Indexing
In the `DATASET` folder there is already a (relatively speaking) small selection of Yelp restaurant reviews retrieved from [Kaggle](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset).

For the sake of ease of sharing (the original dataset was around 6 GB) and because Kaggle needs a user key to retrieve data from their API, the data has been already downloaded and trimmed.

By running `make index` or `python ./INDEXER/indexer.py` those reviews will be indexed and analyzed by using [Sam Lowe's model](https://huggingface.co/SamLowe/roberta-base-go_emotions).

The index can be deleted, alongside the model's cache, by running `make delete_index`.

## Benchmarking
To start benchmarking run `make benchmark` or `python ./BENCHMARK/benckmark.py`. The results will be saved to `./GENERATED_RESULTS/`

The benchmarking data can be deleted by running `make delete benchmark`.

## Starting up
To start up TheSpoon it is sufficient to run `make run`, then head to our [Vercel deployment](https://thespoon.vercel.app).

## Authors
 University of Modena and Reggio Emilia undergraduates in Computer Science [@riccardomassi](https://github.com/riccardomassi/) and [@filipczuba](https://github.com/filipczuba/).
