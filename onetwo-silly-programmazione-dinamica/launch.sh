#!/bin/bash
sudo docker run --rm -i -v $PWD:/problems:ro turingarena/turingarena evaluate --language python < solution.py
