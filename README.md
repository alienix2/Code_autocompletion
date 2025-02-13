# Code_autocompletion

## Structure of the repository

All the scripts, models, tokenizers, processed_datasets, and the `simple` datasets are in the respective folders.

## Scripts

Most of the scripts present variables for the user to change in order to use them. Look inside the single script for the specifics. The choice to not use command line parameters instead was given by the necessity to run the files easily on a jupyter notebook.
The only file that also requires inputs to be passed as a command line argument is `predict.py` that takes in input the string to start the prediction.
In the **Models** section of this README there is a description of the hyperparameters to be used with the models.
At the end of the file there is a description on how to use the scripts for a specific use case as a reference.

## Unused scripts

The repo contains the script `get_python_repos.py` that could be used to get python repos directly from github, but proved to be very hard to use on a personal machine with slow internet connection and therefore the dataset used was not the one downloaded using this file in the end.

## Datasets

There are two datasets used in this project:

- `python150k` dataset, which is a dataset of python repositories (is not provided in this repository but can be found easily online)
- another simpler dataset, found in the folder `simple_files` which is a dataset made of a single python file containing many diverse snippets of python code with a very simple structure. This was used for testing purposes only

## Preprocessing

The preprocessing can be done using the `preprocess_dataset.py` script with the appropriate folder. This script inserts the delimiters for the beginning and end of sentences based on the presence of a double `\n`

There is an alternate preprocessing script, `preprocess_dataset_no_sentences.py`, that does not insert the delimiters for the beginning and end of sentences in the presence of a double `\n` but instead just puts the delimiters at the beginning and end of every file encountered.

The other processing script, `preprocess_dataset_be_file.py`, inserts different delimiters for the beginning and end of file and beginning and end of sentences. Unfortunately the outcome of this strategy isn't tested as I had no time left to do it on online platforms.

## Tokenizers

The tokenizer chosen is a BPE tokenizer. There are multiple tokenizers each of one is trained with a different dataset:

- `python_tokenizer_no_sentences` is trained with the python150k dataset preprocessed with the `preprocess_dataset_no_sentences.py` script
- `python_simple_tokenizer` is trained with the simplified dataset preprocessed with the `preprocess_dataset.py` script
- `python_tokenizer` is trained with the python150k dataset preprocessed with the `preprocess_dataset.py` script

All these tokenizers are obtained using the `hf_tokenizer.py` that relies on libraries provided in the `tokenizer` library of huggingface. Another theoretical script called `hand_made_tokenizer.py` is a very simple example of implementation of a BPE tokenizer that proved to be way too slow to be used for the project.

All the tokenizers are realized with a vocabulary size of 10000. Other size proved to be very hard to test with the hardware I had but could be more effective.

## Models

There are three kind of models, based on the dataset and tokenizers used to train them:

- `simple` models, trained with the file in the `simple_files` folder
- `no_sentences` models, trained with the repositories present in the python150k dataset preprocessed with the `preprocess_dataset_no_sentences.py` script
- the other models, trained with the repositories present in the python150k dataset with the `preprocess_dataset.py` script

It should be noted that actually the most effective models were the ones trained on the `no_sentences` dataset, and therefore the pre_trained models trained on the python150k dataset are all trained on the `no_senteces` one.

It should also be noted that the `simple` models are the only one really working and giving good suggestions but only on very specific scenarios that are represented in the dataset. Any try to generalize them proved unsuccessful unfortunately.

### Hyperparameters models

Pick the model to be used in the `predict.py` file and adjust the hyperparameters in the `transformer.py` python file accordingly

`python_model_no_sentences_128_context` should be use with:

- `python_model_no_sentences_128_context.pth` model
- `python_tokenizer_no_sentences-merges.txt` and
- `python_tokenizer_no_sentences-vocab.json` for tokenizer
- BLOCK_SIZE = 128, N_EMBEDS = 64, N_HEAD = 8, NUMBER_LAYERS = 16

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

## Example of use of the scripts

Generating a model with the small dataset:

1. preprocess the dataset with `preprocess_dataset.py` inserting the `simple_files` folder in the `os.walk` function and the wanted output name of the dataset in the `open` function. I will pick `simple_python_dataset.txt`
2. tokenize the dataset using the `hf_tokenizer.py` script with `formatted_data_file = "simple_python_dataset"` and the correct folder and file name in the `tokenizer.save_model()` function. Also remember to edit the `special_tokens` value based on your needs, if you stick with the standard `preprocess_dataset` script provided, `special_tokens = ["<s>", "</s>"],` should be fine. I will pick `tokenizer.save_model("tokenizers", "python_simple_tokenizer")`. This will generate both the vocabulary and the merges files for the tokenizer with the appropriate names. Here you can also change the dimension of the vocabulary.
3. train the model using the `train_transformer.py` script with the `data_path`, `vocab_path`, `merges_path`, `save_path` correctly set accordingly to the values chosen in the previous steps. I will pick `data_path = simple_python_dataset.txt`, `vocab_path = python_simple_tokenizer-vocab.json`, `merges_path = python_simple_tokenizer-merges.txt` and `save_path = python_simple_model.pth`. Here you can also change the number of epochs here. Remember to change the special tokens in the `train_model` function of the file `transformer.py` if you changed them in the section 2.

4. Once done you can use the `predict.py` script with the context as parameter. Before calling it you must once again put the correct paths for the vocabulary and merges to initialize the `ByteLevelBPETokenizer` and the special tokens. You must also load the correct model, I picked:

```Python
tokenizer = ByteLevelBPETokenizer(
    "python_tokenizer_no_sentences-vocab.json",
    "python_tokenizer_no_sentences-merges.txt",
)
tokenizer.add_special_tokens(["<s>", "</s>"])
tokenizer.post_processor = TemplateProcessing(
    single="<s> $A", special_tokens=[("<s>", 0)]
)

model.load_state_dict(torch.load("python_simple_model.pth"))
```
