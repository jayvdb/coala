#!/usr/bin/env bash

set +e

git clone --depth=1 https://github.com/coala/coala-quickstart

cd coala-quickstart
pip install . -r test-requirements.txt
py.test
