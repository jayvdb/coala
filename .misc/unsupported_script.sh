#!/usr/bin/env bash

set +e

coverage run setup.py install | tee setup.log

retval=$?

if [[ $retval != 4 ]]; then
  echo "Unexpected error code $?"
  if [[ $retval == 0 ]]; then
    exit 127
  fi
  exit $retval
fi

# error when no lines selected by grep
set -e

grep 'coala supports only python 3.4 or later' setup.log
