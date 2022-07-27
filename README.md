# README

Reference course is [FUNDAMENTALS OF MACHINE LEARNING FOR PREDICTIVE DATA ANALYTICS Algorithms, Worked Examples, and Case Studies](https://pdfslide.net/documents/fundamentals-of-machine-learning-for-this-is-an-excerpt-from-the-book-fundamentals.html?page=1) from John D. Kelleher, Brian Mac Namee & Aoife D’Arcy


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
