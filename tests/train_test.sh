#!/bin/bash
set -e

this_shell_script_full_path=$(realpath $0)
cd $(dirname $this_shell_script_full_path)/../
python3 -B train.py <tests/data/train_input.txt
