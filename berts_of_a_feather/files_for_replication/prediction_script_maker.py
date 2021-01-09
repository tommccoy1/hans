
for i in range(100):
    bert_num = str(i)
    if i < 10:
        bert_num = "0" + bert_num
    
    fo = open("predict_" + bert_num + ".sh", "w")

    fo.write("export BERT_BASE_DIR=uncased_L-12_H-768_A-12\n")
    fo.write("export GLUE_DIR=glue_data\n")
    fo.write("export TRAINED_CLASSIFIER=bert_" + bert_num + "\n\n")

    fo.write("python run_classifier.py --task_name=MNLI --do_predict=true --data_dir=$GLUE_DIR/HANS --vocab_file=$BERT_BASE_DIR/vocab.txt --bert_config_file=$BERT_BASE_DIR/bert_config.json --init_checkpoint=$TRAINED_CLASSIFIER --max_seq_length=128 --output_dir=$TRAINED_CLASSIFIER/HANS\n")

    fo.write("python run_classifier.py --task_name=MNLI --do_predict=true --data_dir=$GLUE_DIR/MNLI --vocab_file=$BERT_BASE_DIR/vocab.txt --bert_config_file=$BERT_BASE_DIR/bert_config.json --init_checkpoint=$TRAINED_CLASSIFIER --max_seq_length=128 --output_dir=$TRAINED_CLASSIFIER/MNLI\n")



