#!/usr/bin/env bash
# To run in "watch" mode:
#   ls resume.Rmd | entr ./build.sh
R --no-save <<EOS
library(rmarkdown)
rmarkdown::render(input ='resume.Rmd')
EOS