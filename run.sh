#!/bin/bash

python main.py
pdftk biweeklytimesheet2013.pdf fill_form data.fdf output output.pdf flatten
