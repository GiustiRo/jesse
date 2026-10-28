#!/bin/sh
# r62: one generation step of a run after its proposer answered:
#   sh r62_step.sh <run> <gen> <tool_uses> [last_gen]
# ingest the LLM answer, run the local genetic search, then build the next generation's package.
set -e
cd "$(dirname "$0")"
run=$1; gen=$2; tu=$3; last=${4:-9}
ans=data/r62/runs/$run/answer_$gen.json
[ -f "$ans" ] || echo '[]' > "$ans"
python -X utf8 r62_run.py ingest "$run" "$gen" "$ans" "$tu"
python -X utf8 r62_run.py ga "$run" "$gen"
if [ "$gen" -lt "$last" ]; then python -X utf8 r62_run.py pkg "$run" $((gen + 1)); else python -X utf8 r62_run.py final "$run" > /dev/null; echo final; fi
