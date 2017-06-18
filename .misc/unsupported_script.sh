#!/usr/bin/env bash

set +e

coverage run setup.py install | tee setup.log
SETUP_EXIT_CODE=$?

grep -q 'coala supports only python 3.4 or later' setup.log
GREP_EXIT_CODE=$?

# Error if setup.py does not fail, or no lines selected by grep
if [[ $SETUP_EXIT_CODE == 0 || $GREP_EXIT_CODE == 1 ]]; then
  exit 1
fi
