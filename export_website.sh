#!/bin/bash

python remove_pingendo.py
chmod -R +r *
#scp -r * xkcd@tricycle.cs.washington.edu:/cse/web/homes/xkcd/
rsync -avW * xkcd@tricycle.cs.washington.edu:/cse/web/homes/xkcd
#git add -A
#git commit -m "update"
#git push github master


