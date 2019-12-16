# Finding examples that contradict the heuristics

This directory contains scripts for finding examples in the MNLI training set which contradict the heuristics targeted by HANS. The `lex_finder.py` script was used to generate the file [mnli_contradicting_examples](https://github.com/tommccoy1/hans/blob/master/mnli_contradicting_examples).


How to use these scripts with MNLI:

Move these scripts into the same directory as MNLI, which can be downloaded
from here: https://www.nyu.edu/projects/bowman/multinli/

In particular, these scripts all read from the file `multinli_1.0_train.txt` 

To look for examples of the lexical overlap heuristic, run:
python lex_finder.py

To look for examples of the subsequence heuristic, run:
python subseq_finder.py

To look for examples of the constituent heuristic, run:
python const_finder.py

Each of these scripts will first print out all examples from
multinli_1.0_train.txt that contradict the heuristic. At the
end, the script then prints out a summary of how many examples which could potentially relate to the heuristic were
entailment, contradiction, or neutral (where the ones that contradict the heuristic are ones with labels of contradiction or neutral). These numbers should match the table
near the start of Section 2 of the HANS paper
(https://arxiv.org/pdf/1902.01007.pdf).


If you want to use these scripts with a corpus other than MNLI, there are two
options:
1) Format that corpus in the same way that MNLI is formatted, such
that these scripts can run on it.
2) Modify these scripts to deal with the format of the other corpus.
For the lexical overlap and subsequence heuristics, it should be
straightforward to modify them for other corpora. For the constituent
heuristic, it might be a bit trickier, because that script relies on the
parses that are provided with MNLI. Therefore, if your corpus is not parsed,
you will need to parse it to tell whether the constituent heuristic applies.



