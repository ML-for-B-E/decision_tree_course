# README

Reference course is [FUNDAMENTALS OF MACHINE LEARNING FOR PREDICTIVE DATA ANALYTICS Algorithms, Worked Examples, and Case Studies](https://pdfslide.net/documents/fundamentals-of-machine-learning-for-this-is-an-excerpt-from-the-book-fundamentals.html?page=1) from John D. Kelleher, Brian Mac Namee & Aoife D’Arcy


# Setup your execution environment
We assume here a Linux environnement for the CLI.

* Put yourself at the root of project. Depending of your current working directory, you may have to adjust `cd decision_tree_course` 
* Run the command `python3 -m venv venv`
* Activate the venv: `source venv/bin/activate`
* Upgrade pip if needed `pip install --upgrade pip`
* Install packages needed with `pip install -r requirements/dev.txt`
* Install our package `summer` with `pip install -e .`
* Create a jupyter kernel linked to this venv. Follow instructions here https://queirozf.com/entries/jupyter-kernels-how-to-add-change-remove. 
  - `ipython kernel install --name "venv" --user`
* You can now open a notebook by running `jupyter notebook --no-browser`
* Select the kernel `venv` to run the notebook.
