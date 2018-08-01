#!/bin/sh

THIS_DIR=$(cd $(dirname $0); pwd)
DATA_DIR=${THIS_DIR}/../data
OUTPUT_FILE=${1:-${DATA_DIR}/bubblesort_train.pkl}
LOG=bubblesort_train_result.log
export PYTHONPATH=${THIS_DIR}
cd $THIS_DIR

mkdir -p "$DATA_DIR"

rm -f "$LOG"
echo python npi/bubblesort/create_training_data.py "$OUTPUT_FILE" 1000 "$LOG"
python npi/bubblesort/create_training_data.py "$OUTPUT_FILE" 1000 "$LOG"
