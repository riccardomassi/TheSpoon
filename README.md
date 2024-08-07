<div align="center">
  <img width="200" height="200" src="https://github.com/riccardomassi/TheSpoon/blob/main/GUI/public/dark/dark-mode-logo.png">
</div>

## What is TheSpoon?
TheSpoon is a tool for searching trough restaurant reviews, built by food enjoyers for food enjoyers.

TheSpoon utilizes Sentiment Analysis and Information Retrieval techniques to allow users to search trough a selection of reviews of restaurants throughout the USA, accessible trough a Next.js front-end.
<div align="center">
  <img width="800" height="410" src="https://github.com/riccardomassi/TheSpoon/blob/main/video.gif">
</div>

## Requirements
Requirements are listed in the `/REQUIREMENTS/requirements.txt` file and can be installed by running `make install_requirements`

To run TheSpoon Internet access is required, both to download the Sentiment Analysis module and to access the Vercel JavaScript front-end.

## Indexing
In the `DATASET` folder there is already a (relatively speaking) small selection of Yelp restaurant reviews retrieved from [Kaggle](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset).

For the sake of ease of sharing (the original dataset was around 6 GB) and because Kaggle needs a user key to retrieve data from their API, the data has been already downloaded and trimmed.

By running `make index` or `python ./INDEXER/indexer.py` those reviews will be indexed and analyzed by using [Sam Lowe's model](https://huggingface.co/SamLowe/roberta-base-go_emotions).

The index can be deleted, alongside the model's cache, by running `make delete_index`.

## Benchmarking
To start benchmarking run `make benchmark` or `python ./runBenchmark.py`. The results will be saved to `./GENERATED_BENCHMARK/`

The benchmarking data can be deleted by running `make delete benchmark`.

The benchmarking suite has both automatic and manual tools. The user will be asked to perform the manual evaluation of the queries by which the NDCG will be calculated.

## Starting up
To start up TheSpoon it is sufficient to run `make start`, then head to our [Vercel deployment](https://thespoon.vercel.app).

## Authors
University of Modena and Reggio Emilia undergraduates in Computer Science [@riccardomassi](https://github.com/riccardomassi/) and [@filipczuba](https://github.com/filipczuba/).

## Licences
This project is licensed under the MIT License.

