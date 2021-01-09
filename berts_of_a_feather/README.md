# BERTs of a feather
This folder contains data accompanying the paper [BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance](https://www.aclweb.org/anthology/2020.blackboxnlp-1.21.pdf), in which we analyzed how 100 instances of BERT fine-tuned on MNLI varied in their performance on the MNLI development set and on the HANS evaluation set.

## Accuracies by model

The files ``berts_of_a_feather_accuracies_by_run.xlsx`` and ``berts_of_a_feather_accuracies_by_run.csv`` give the performance of each of our 100 instances of BERT on each category of example they were evaluated on. (The two files give the same data, just in different file types).

## Model predictions

The file ``all_hans_predictions.txt`` gives each model's prediction for each example in the HANS evaluation set. Each line in this file corresponds to one example in the HANS evaluation set; specifically, it corresponds to the HANS example with the example number that is the line number in ``all_hans_predictions.txt`` minus 1. For instance, line 398 in ``all_hans_predictions.txt`` corresponds to the HANS example with the ID ``ex397``, i.e. the example woth premise _The lawyer helped the artist ._ and hypothesis  _The artist helped the lawyer ._.

The file ``all_mnli_development_set_predictions.txt`` gives each model's prediction for each example in the MNLI development set. Each line in this file corresponds to one example in the MNLI development set; specifically, it corresponds to the MNLI development set example with the example number that is the line number in ``all_mnli_development_set_predictions.txt`` minus 1. For instance, line 398 in ``all_mnli_development_set_predictions.txt`` corresponds to the MNLI example with the ID ``397``, i.e. the example woth premise _The percent of total cost for each function included in the model and cost elasticity (with respect to volume) are shown in Table 1._ and hypothesis _Table 1 also shows a picture diagram for each function._

In both of these files, each line lists the predictions made by each of our 100 instances of BERT (in order) for the relevant example in HANS or the MNLI development set. That is, on a given line, the first prediction will be the prediction made by the model saved as `bert_00.zip` on our [Zenodo repository](https://zenodo.org/record/4110593#.X_lj3-lKjGJ), the second will be the prediction made by `bert_01.zip`, etc.

## Number of correct response

The file ``mnli_development_set_number_of_correct_response.txt`` shows, for each example in the MNLI development set, the number of BERT instances (out of 100) that got that example right. This file includes the premises and hypotheses from the MNLI dataset introduced in the paper [A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference](https://www.aclweb.org/anthology/N18-1101/) by Adina Williams, Nikita Nangia, and Samuel Bowman; please see that paper for license details for the MNLI dataset.

## Model weights

The weights for our 100 fine-tuned instances of BERT are available on Zenodo: [https://zenodo.org/record/4110593#.X_lj3-lKjGJ](https://zenodo.org/record/4110593#.X_lj3-lKjGJ). Warning: Each of these zip files takes up about 1.2 GB of memory.

## Getting predictions from our model weights

If you want to use the saved weight files from Zenodo to replicate the numbers in our paper, follow the steps below. You should also be able to get predictions on your own data by tweaking this pipeline.

1. Clone the HANS GitHub repository and go into the berts_of_a_feather directory:

```
git clone https://github.com/tommccoy1/hans.git
cd hans/berts_of_a_feather
```

2. Clone the Google BERT GitHub repo inside hans/berts_of_a_feather:

```
git clone https://github.com/google-research/bert.git
cd bert/
```

3. Checkout the specific timestamp of the BERT repo that we used. (This step is probably unnecessary, as the code should remain compatible with different versions of the BERT repository):

```
git checkout 88a817c
```

4. Download and unzip the bert-base-uncased model:

```
wget https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip
unzip uncased_L-12_H-768_A-12.zip
```

5. Create a file named `download_glue_data.py` and copy this script into it: [https://gist.github.com/W4ngatang/60c2bdb54d156a41194446737ce03e2e](https://gist.github.com/W4ngatang/60c2bdb54d156a41194446737ce03e2e)

6. Use that script to download MNLI (make sure you are using Python 3):

```
python download_glue_data.py --data_dir glue_data --tasks MNLI
```

7. Insert the HANS evaluation set:

```
cd glue_data
mkdir HANS
cd HANS
cp ../../../files_for_replication/test_matched.tsv .
```

8. Replace the MNLI test set with the MNLI development set, since we evaluated on the development set.

```
cd ../MNLI
mv dev_matched.tsv test_matched.tsv
cd ../../
```

9. For each BERT instance that you want to run, download the corresponding zip file from the [Zenodo repository](https://zenodo.org/record/4110593#.X_lj3-lKjGJ) into the folder `bert/`. You can use the download links from the Zenodo page, or you can use a command line command as in the following example for BERT instance 47 (just replace `47` with whichever index you want). Be warned that each of these zip files takes up about 1.2 GB.

```
wget https://zenodo.org/record/4110593/files/bert_47.zip
```

10. Unzip the weight file(s) that you downloaded in the previous step:

```
unzip bert_47.zip
```

11. Use our script `prediction_script_maker.py` to generate scripts for getting predictions from the weight files.

```
cp ../files_for_replication/prediction_script_maker.py .
python prediction_script_maker.py
chmod +x predict*sh
``` 

12. The previous step should have created 100 prediction scripts, e.g. `predict_47.sh`. Run the prediction script(s) for the model number(s) that you downloaded in step 9. To run this script, you will need to have TensorFlow installed - see [Google's BERT GitHub repo](https://github.com/google-research/bert) for more information on running BERT.

```
bash predict_47.sh
```

13. The model's MNLI predictions will be written to `bert_47/MNLI/test_results.tsv`, and the model's HANS predictions will be written to `bert_47/HANS/test_results.tsv` (except replace `47` with whichever model number you are using). These `test_results.tsv` files have one row for each example in the evaluation set, with 3 tab-separated probabilities for the 3 output classes (`contradiction`, `entailment`, and `neutral`, in that order). To change the output into a more readable format, you can use our script `process_test_results.py`:

```
cp ../files_for_replication/process_test_results.py .
python process_test_results.py bert_47/HANS
python process_test_results.py bert_47/MNLI
```

This will create new files called `bert_47/HANS/preds.txt` and `bert_47/MNLI/preds.txt` containing the predictions on these two evaluation sets. The `preds.txt` files are written in the format that can be passed into our [script for summarizing HANS results](https://github.com/tommccoy1/hans/blob/master/evaluate_heur_output.py). though this script will only work for the HANS output, not the MNLI output.

The predictions that you get in this way should match the [HANS predictions](https://github.com/tommccoy1/hans/blob/master/berts_of_a_feather/all_hans_predictions.txt) and [MNLI predictions](https://github.com/tommccoy1/hans/blob/master/berts_of_a_feather/all_mnli_development_set_predictions.txt) featured in [our paper](https://www.aclweb.org/anthology/2020.blackboxnlp-1.21.pdf); see [Model predictions](https://github.com/tommccoy1/hans/tree/master/berts_of_a_feather#model-predictions) for a description of the format of the files storing the predictions used for our paper. You might get slight discrepancies (we found that the models' predictions changed slightly depending on which machine we ran our pipeline on), but the predictions should change for fewer than a tenth of a percent of examples.


## Fine-tuning BERT on MNLI

If you want to create new fine-tuned instances of BERT using the same procedure as we did, below is a description of that procedure, which comes from the [Google BERT GitHub repo](https://github.com/google-research/bert). For more details, see the Google BERT repo.


1. Clone the Google BERT GitHub repo:

```
git clone https://github.com/google-research/bert.git
cd bert/
```

2. Checkout the specific timestamp of the BERT repo that we used. (This step is probably unnecessary, as the code should remain compatible with different versions of the BERT repository):

```
git checkout 88a817c
```

3. Download and unzip the bert-base-uncased model:

```
wget https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip
unzip uncased_L-12_H-768_A-12.zip
```

4. Create a file named `download_glue_data.py` and copy this script into it: [https://gist.github.com/W4ngatang/60c2bdb54d156a41194446737ce03e2e](https://gist.github.com/W4ngatang/60c2bdb54d156a41194446737ce03e2e)

5. Use that script to download MNLI (make sure you are using Python 3):

```
python download_glue_data.py --data_dir glue_data --tasks MNLI
```

6. Run the following command to fine-tune BERT on MNLI:

```
export BERT_BASE_DIR=uncased_L-12_H-768_A-12
export GLUE_DIR=glue_data

python run_classifier.py \
  --task_name=MNLI \
  --do_train=true \
  --do_eval=true \
  --data_dir=$GLUE_DIR/MNLI \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --max_seq_length=128 \
  --train_batch_size=32 \
  --learning_rate=2e-5 \
  --num_train_epochs=3.0 \
  --output_dir=mnli_save
``` 


## Citing

If you use code or data from this folder, please cite our [paper](https://www.aclweb.org/anthology/2020.blackboxnlp-1.21) (BibTex can be found [here](https://www.aclweb.org/anthology/2020.blackboxnlp-1.21.bib)).



