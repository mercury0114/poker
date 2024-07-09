#!/bin/bash
set -e

this_shell_script_full_path=$(realpath $0)
cd $(dirname $this_shell_script_full_path)/../
python3 -B -m binaries.count_hands <tests/data/play_input.txt
