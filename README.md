# README

Reference course can be found here:
https://www.r-bloggers.com/2014/09/in-depth-introduction-to-machine-learning-in-15-hours-of-expert-videos/


# Setup directory
* Ask @BWhannou to give you access to data https://www.dropbox.com/sh/smaw3u7blio7lw8/AAAtzyTqXKNeuP3asM22p8PBa?dl=0
* unzip the downloaded folder `data.zip` in `summer-camp-2021/cours_de_stats/`

# Use a virtual env (to follow good IT practices of isolation)
We assume here a Linux environnement for the CLI.

* Put yourself in `cd summer-camp-2021` 
* Run the command `python3 -m venv venv`
* Activate the venv: `source venv/bin/activate`
* Upgrade pip if needed `pip install --upgrade pip`
* Install packages needed with `pip install -r requirements/dev.txt`
* Install our package `summer` with `pip install -e .`
* Create a jupyter kernel linked to this venv. Follow instructions here https://queirozf.com/entries/jupyter-kernels-how-to-add-change-remove. 
  - `ipython kernel install --name "venv" --user`
* You can now open a notebook by running `jupyter notebook --no-browser`
* Select the kernel `venv` to run the notebook.
