# BERTs of a feather
This folder contains data accompanying the paper [BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance](https://arxiv.org/pdf/1911.02969.pdf), in which we analyzed how 100 instances of BERT fine-tuned on MNLI varied in their performance on the MNLI development set and on the HANS evaluation set.

## Accuracies by model

The files ``berts_of_a_feather_accuracies_by_run.xlsx`` and ``berts_of_a_feather_accuracies_by_run.csv`` give the performance of each of our 100 instances of BERT on each category of example they were evaluated on. (The two files give the same data, just in different file types).

## Model predictions

The file ``all_hans_predictions.txt`` gives each model's prediction for each example in the HANS evaluation set. Each line in this file corresponds to one example in the HANS evaluation set; specifically, it corresponds to the HANS example with the example number that is the line number in ``all_hans_predictions.txt`` minus 1. For instance, line 398 in ``all_hans_predictions.txt`` corresponds to the HANS example with the ID ``ex397``, i.e. the example woth premise _The lawyer helped the artist ._ and hypothesis  _The artist helped the lawyer ._.

The file ``all_mnli_development_set_predictions.txt`` gives each model's prediction for each example in the MNLI development set. Each line in this file corresponds to one example in the MNLI development set; specifically, it corresponds to the MNLI development set example with the example number that is the line number in ``all_mnli_development_set_predictions.txt`` minus 1. For instance, line 398 in ``all_mnli_development_set_predictions.txt`` corresponds to the HANS example with the ID ``397``, i.e. the example woth premise _The percent of total cost for each function included in the model and cost elasticity (with respect to volume) are shown in Table 1._ and hypothesis _Table 1 also shows a picture diagram for each function._

In both of these files, each line lists the predictions made by each of our 100 instances of BERT (in order) for the relevant example in HANS or the MNLI development set.

## Number of correct response

The file ``mnli_development_set_number_of_correct_response.txt`` shows, for each example in the MNLI development set, the number of BERT instances (out of 100) that got that example right.

## Model weights






 

