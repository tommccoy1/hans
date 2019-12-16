

fi = open("multinli_1.0_train.txt", "r")

count_entailment = 0
count_neutral = 0
count_contradiction = 0

def parse_phrase_list(parse, phrases):

    #print(parse)
    if parse == "":
        return phrases
    
    phrase_list = phrases

    

    words = parse.split()
    this_phrase = []
    next_level_parse = []
    for index, word in enumerate(words):
        if word == "(":
            next_level_parse += this_phrase
            this_phrase = ["("]

        elif word == ")" and len(this_phrase) > 0 and this_phrase[0] == "(":
            phrase_list.append(" ".join(this_phrase[1:]))
            next_level_parse += this_phrase[1:]
            this_phrase = []
        elif word == ")":
            next_level_parse += this_phrase
            next_level_parse.append(")")
            this_phrase = []
        else:
            this_phrase.append(word)
            #next_level_parse.append(word)

    #next_level_parse += this_phrase
    #print(phrase_list, " ".join(next_level_parse))

    return parse_phrase_list(" ".join(next_level_parse), phrase_list)

first = True

counter = 0
for line in fi:
    #if counter % 1000 == 0:
    #    print(counter)
    counter += 1

    if first:
        first = False
        continue


    parts = line.strip().split("\t")

    premise = parts[5]
    hypothesis = parts[6]
    label = parts[0]
    parse = parts[1]

    parse_new = []
    for word in parse.split():
        if word not in [".", "?", "!"]:
            parse_new.append(word.lower())

    all_phrases = parse_phrase_list(" ".join(parse_new), [])

    prem_words = []
    hyp_words = []

    for word in premise.split():
        if word not in [".", "?", "!"]:
            prem_words.append(word.lower().replace(".", "").replace("?", "").replace("!", ""))

    for word in hypothesis.split():
        if word not in [".", "?", "!"]:
            hyp_words.append(word.lower().replace(".", "").replace("?", "").replace("!", ""))

    prem_filtered = " ".join(prem_words)
    hyp_filtered = " ".join(hyp_words)

    #print(hyp_filtered, all_phrases)
    if hyp_filtered in all_phrases:
        #print(premise, hypothesis, label)
        #print(label)
        if label == "entailment":
            count_entailment += 1
        if label == "neutral":
            count_neutral += 1
            print(premise, hypothesis, label)
        if label == "contradiction":
            count_contradiction += 1
            print(premise, hypothesis, label)

    #print(premise, hypothesis, label)

    #break

print("Entailment:", count_entailment)
print("Contradiction:", count_contradiction)
print("Neutral:", count_neutral)
