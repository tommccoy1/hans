
from templates import *

template_list = [
        ("lexical_overlap", "ln_subject/object_swap", "non-entailment", lex_simple_templates), 
        ("lexical_overlap", "ln_preposition", "non-entailment", lex_prep_templates), 
        ("lexical_overlap", "ln_relative_clause", "non-entailment", lex_rc_templates), 
        ("lexical_overlap", "ln_passive", "non-entailment", lex_pass_templates), 
        ("lexical_overlap", "ln_conjunction", "non-entailment", lex_conj_templates), 
        ("lexical_overlap", "le_relative_clause", "entailment", lex_rc_ent_templates), 
        ("lexical_overlap", "le_around_prepositional_phrase", "entailment", lex_cross_pp_ent_templates), 
        ("lexical_overlap", "le_around_relative_clause", "entailment",lex_cross_rc_ent_templates), 
        ("lexical_overlap", "le_conjunction", "entailment",lex_ent_conj_templates), 
        ("lexical_overlap", "le_passive", "entailment",lex_ent_pass_templates), 
        ("subsequence", "sn_NP/S", "non-entailment",subseq_nps_templates), 
        ("subsequence", "sn_PP_on_subject", "non-entailment",subseq_pp_on_subj_templates), 
        ("subsequence", "sn_relative_clause_on_subject", "non-entailment",subseq_rel_on_subj_templates), 
        ("subsequence", "sn_past_participle", "non-entailment",subseq_past_participle_templates), 
        ("subsequence", "sn_NP/Z", "non-entailment",subseq_npz_templates), 
        ("subsequence", "se_conjunction", "entailment",subseq_conj_templates), 
        ("subsequence", "se_adjective", "entailment", subseq_adj_templates), 
        ("subsequence", "se_understood_object", "entailment",subseq_understood_templates), 
        ("subsequence", "se_relative_clause_on_obj", "entailment",subseq_rel_on_obj_templates), 
        ("subsequence", "se_PP_on_obj", "entailment",subseq_pp_on_obj_templates), 
        ("constituent", "cn_embedded_under_if", "non-entailment",const_under_if_templates), 
        ("constituent", "cn_after_if_clause", "non-entailment",const_outside_if_templates),
        ("constituent", "cn_embedded_under_verb", "non-entailment",const_quot_templates), 
        ("constituent", "cn_disjunction", "non-entailment",const_disj_templates), 
        ("constituent", "cn_adverb", "non-entailment",const_advs_nonent_templates), 
        ("constituent", "ce_embedded_under_since", "entailment",const_adv_embed_templates), 
        ("constituent", "ce_after_since_clause", "entailment",const_adv_outside_templates),
        ("constituent", "ce_embedded_under_verb", "entailment",const_quot_ent_templates), 
        ("constituent", "ce_conjunction", "entailment",const_conj_templates), 
        ("constituent", "ce_adverb", "entailment",const_advs_ent_templates)
        ]

def no_the(sentence):
    return sentence.replace("the ", "")









lemma = {}
lemma["professors"] = "professor"
lemma["students"] = "student"
lemma["presidents"] = "president"
lemma["judges"] = "judge"
lemma["senators"] = "senator"
lemma["secretaries"] = "secretary"
lemma["doctors"] = "doctor"
lemma["lawyers"] = "lawyer"
lemma["scientists"] = "scientist"
lemma["bankers"] = "banker"
lemma["tourists"] = "tourist"
lemma["managers"] = "manager"
lemma["artists"] = "artist"
lemma["authors"] = "author"
lemma["actors"] = "actor"
lemma["athletes"] = "athlete"

def repeaters(sentence):
    condensed = no_the(sentence)
    words = []
    
    for word in condensed.split():
        if word in lemma:
            words.append(lemma[word])
        else:
            words.append(word)

    if len(list(set(words))) == len(words):
        return False
    else:
        return True

fo = open("heuristics_evaluation_set.txt", "w")
#fo.write("heuristic\tsubcase\ttemplate\tlabel\tpremise\thypothesis\tpremise_parse\thypothesis_parse\tpremise_binary_parse\thypothesis_binary_parse\n")
fo.write("gold_label\tsentence1_binary_parse\tsentence2_binary_parse\tsentence1_parse\tsentence2_parse\tsentence1\tsentence2\tpairID\theuristic\tsubcase\ttemplate\n")

example_counter = 0

for template_tuple in template_list:
    heuristic = template_tuple[0]
    category = template_tuple[1]
    label = template_tuple[2]
    template = template_tuple[3]

    example_dict = {}
    count_examples = 0

    while count_examples < 1000:
        example = template_filler(template)

        example_sents = tuple(example[:2])

        if example_sents not in example_dict and not repeaters(example[0]):
            example_dict[example_sents] = 1
            pairID = "ex" + str(example_counter)
            fo.write(label + "\t" + example[5] + "\t" + example[6] + "\t" + example[3] + "\t" + example[4] + "\t" + example[0] + "\t" + example[1] + "\t" + pairID + "\t" + heuristic + "\t" + category + "\t" + example[2] + "\n")
            #fo.write(heuristic + "\t" + category + "\t" + example[2] + "\t" + label + "\t" + example[0] + "\t" + example[1] + "\t" + example[3] + "\t" + example[4] + "\t" + example[5] + "\t" + example[6] + "\n")
            count_examples += 1
            example_counter += 1
            





