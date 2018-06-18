#!/bin/bash

rm -r _modules
sphinx-apidoc -f -M -o _modules ../datasciencetoolbox/*
make html
