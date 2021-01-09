import sys

prefix = sys.argv[1]

fi = open(prefix + "/" + "test_results.tsv", "r")
fo = open(prefix + "/" + "preds.txt", "w")


fo.write("pairID,gold_label\n")
counter = 0
labels = ["contradiction", "entailment", "neutral"]
for line in fi:
	parts = [float(x) for x in line.strip().split("\t")]

	max_ind = 0
	max_val = parts[0]

	for ind, part in enumerate(parts):
		if part > max_val:
			max_val = part
			max_ind = ind

	fo.write("ex" + str(counter) + "," + labels[max_ind] + "\n")
	counter += 1


