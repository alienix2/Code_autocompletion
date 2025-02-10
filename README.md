# Code_autocompletion

## Structure of the repository

All the scripts are in the root of the repository.
Other than those, all the models, tokenizers, processed_datasets, and the `simple` datasets are in the respective folders.

## Unused scripts

The repo contains the script `get_python_repos.py` that could be used to get python repos directly from github, but proved to be very hard to use on a personal machine with slow internet connection and therefore the dataset used was not the one downloaded using this file in the end.

## Datasets

There are two datasets used in this project:

- `python150k` dataset, which is a dataset of python repositories (is not provided in this repository but can be found easily online)
- another simpler dataset, found in the folder `simple_files` which is a dataset made of a single python file containing many diverse snippets of python code with a very simple structure. This was used for testing purposes only

## Preprocessing

The preprocessing can be done using the `preprocess_dataset.py` script with the appropriate folder. This script inserts the delimiters for the beginning and end of sentences based on the presence of a double `\n`

There is an alternate preprocessing script, `preprocess_dataset_no_sentences.py`, that does not insert the delimiters for the beginning and end of sentences in the presence of a double `\n` but instead just puts the delimiters at the beginning and end of every file encountered.

## Tokenizers

The tokenizer chosen is a BPE tokenizer. There are multiple tokenizers each of one is trained with a different dataset:

- `python_tokenizer_no_sentences` is trained with the python150k dataset preprocessed with the `preprocess_dataset_no_sentences.py` script
- `python_simple_tokenizer` is trained with the simplified dataset preprocessed with the `preprocess_dataset.py` script
- `python_tokenizer` is trained with the python150k dataset preprocessed with the `preprocess_dataset.py` script

All these tokenizers are obtained using the `hf_tokenizer.py` that relies on libraries provided in the `tokenizer` library of huggingface. Another theoretical script called `hand_made_tokenizer.py` is a very simple example of implementation of a BPE tokenizer that proved to be way too slow to be used for the project.

## Models

There are three kind of models, based on the dataset and tokenizers used to train them:

- `simple` models, trained with the file in the `simple_files` folder
- `no_sentences` models, trained with the repositories present in the python150k dataset preprocessed with the `preprocess_dataset_no_sentences.py` script
- the other models, trained with the repositories present in the python150k dataset with the `preprocess_dataset.py` script

It should be noted that actually the most effective models were the ones trained on the `no_sentences` dataset, and therefore the pre_trained models trained on the python150k dataset are all trained on the `no_senteces` one.

It should also be noted that the `simple` models are the only one really working and giving good suggestions but only on very specific scenarios that are represented in the dataset. Any try to generalize them proved unsuccessful unfortunately.

### How to use the models

Pick the model to be used in the `predict.py` file and adjust the hyperparameters in the `transformer.py` python file accordingly

`python_model_no_sentences_128_context` should be use with:

- `python_model_no_sentences_128_context.pth` model
- `python_tokenizer_no_sentences-merges.txt` and
- `python_tokenizer_no_sentences-vocab.json` for tokenizer
- BLOCK_SIZE = 128, N_EMBEDS = 64, N_HEAD = 8, NUMBER_LAYERS = 16

`python_model_no_sentences_256_context` should be used with:

- `python_simple_model.pth` model
- `python_simple_tokenizer-merges.txt` and
- `python_simple_tokenizer-vocab.json` for tokenizer
- BLOCK_SIZE = 256, N_EMBEDS = 64, N_HEAD = 8, NUMBER_LAYERS = 16

`python_simple_32_context.pth` should be used with:

- `python_simple_32_context.pth` model
- `python_simple_tokenizer-merges.txt` and
- `python_simple_tokenizer-vocab.json` for tokenizer
- BLOCK_SIZE = 32, N_EMBEDS = 64, N_HEAD = 8, NUMBER_LAYERS = 12

`python_simple_64_context.pth` should be used with:

- `python_simple_64_context.pth` model
- `python_simple_tokenizer-merges.txt` and
- `python_simple_tokenizer-vocab.json` for tokenizer
- BLOCK_SIZE = 64, N_EMBEDS = 64, N_HEAD = 8, NUMBER_LAYERS = 12
