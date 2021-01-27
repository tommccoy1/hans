# HANS
This repository contains the HANS (Heuristic Analysis for NLI Systems) dataset.

## Data:

The file ``heuristics_evaluation_set.txt`` contains the HANS evaluation set introduced in our paper, [Right for the Wrong Reasons: Diagnosing Syntactic Heuristics in Natural Language Inference](https://arxiv.org/abs/1902.01007). This file is formatted similarly to the MNLI release, so if your system is trained on MNLI you may be able to feed this file directly into your system. Otherwise, you may need to reformat the data to fit your system's input format. 

The fields in this file are:
- ``gold_label``: The correct label for this sentence pair (either ``entailment`` or ``non-entailment``)
- ``sentence1_binary_parse``: A binary parse of the premise, generated using a template based on the Stanford PCFG; this is necessary as input for some tree-based models.
- ``sentence2_binary_parse``: A binary parse of the hypothesis, generated using a template based on the Stanford PCFG; this is necessary as input for some tree-based models.
- ``sentence1_parse``: A parse of the premise, generated using a template based on the Stanford PCFG
- ``sentence2_parse``: A parse of the hypothesis, generated using a template based on the Stanford PCFG
- ``sentence1``: The premise
- ``sentence2``: The hypothesis
- ``pairID``: A unique identifier for this sentence pair
- ``heuristic``: The heuristic that this example is targeting (``lexical_overlap``, ``subsequence``, or ``constituent``)
- ``subcase``: The subcase of the heuristic that is being targeted; each heuristic has 10 subcases, described in the appendix to the paper
- ``template``: The specific template that was used to generate this pair (most of the subcases have multiple templates; e.g., for subcases depending on relative clauses, there might be one template for relative clauses modifying the subject, and another for relative clauses modifying the direct object). This template ID corresponds to the ID in ``templates.py``.

The file ``heuristics_train_set.txt`` contains the set of HANS-like examples that were used for the data augmentation experiments in Section 7 of [the HANS paper](https://arxiv.org/pdf/1902.01007.pdf). This file is set up exactly like ``heuristics_evaluation_set.txt`` (i.e., it also contains 1000 examples from each of the 30 HANS subcases), but none of the specific examples that appear in ``heuristics_evaluation_set.txt`` appear in ``heuristics_train_set.txt``, so that ``heuristics_train_set.txt`` can be used for data augmentation during training while still preserving the validity of ``heuristics_evaluation_set.txt`` as an evaluation set (e.g., in the paper we trained models on the union of ``heuristics_train_set.txt`` and the MNLI training set, and then evaluated on ``heuristics_evaluation_set.txt``).

The training set and evaluation set are also both include as JSON lines files, with the ``.jsonl`` extension.

## Evaluation:

We provide a script for evaluating a model's predictions. These predictions must be formatted in a text file with the following properties:
 - The first line should be "pairID,gold_label"
 - The rest of the lines should contain the ``pairID`` for a premise/hypothesis pair, followed by a comma, followed by the model's prediction for that pair (either ``entailment`` or ``non-entailment``; for this purpose, you will need to change both ``contradiction`` and ``neutral`` into ``non-entailment``).
 - This file should have 30,001 lines: 1 line for the header, plus 30,000 more lines for the 30,000 examples in HANS
 
There are several example files provided here: ``bert_preds.txt``, ``decomp_attn_heur_preds.txt``, ``spinn_preds_heur.txt``, and ``esim_heur_preds.txt``.

To evaluate a file formatted in this way, simply run:

``python evaluate_heur_output.py FILENAME``

This will give you results broken down at three levels of granularity. 
- First, it will give results for the 3 heuristics, showing for each heuristic the model's accuracy on examples where the correct label is ``entailment`` and its accuracy on examples where the correct label is ``non-entailment``.
- Second, it will give accuracies for all 30 subcases of the heuristics (e.g. subject/object swap, NP/S, etc.)
- Finally, it will give accuracies for each template

## Finding contradicting examples

The file [mnli_contradicting_examples](https://github.com/tommccoy1/hans/blob/master/mnli_contradicting_examples) contains a list of the examples in the MNLI training set that contradict the heuristics targeted by HANS. For the scripts that we used to find these examples, see the folder [heuristic_finder_scripts](https://github.com/tommccoy1/hans/tree/master/heuristic_finder_scripts).

## License:

This repository is licensed under an [MIT License](https://github.com/tommccoy1/hans/blob/master/LICENSE.md). 


## Citing

If you use data from this repository, please cite our [paper](https://www.aclweb.org/anthology/P19-1334/) (BibTex [here](https://www.aclweb.org/anthology/P19-1334.bib)).


 

