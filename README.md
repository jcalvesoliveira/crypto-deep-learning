crypto-deep-learning
==============================

Team Members:
* Julio Oliveira
* Rachana Sooraj
* Manish Ranjan

Python Environment
------------------

We recommend using [Pipenv](https://github.com/pypa/pipenv) to reproduce this project.

After installing pipenv just run:

```
pipenv install --dev
```

This process will create the pipenv environment with all dependencies for this project. 

To activate the environment run:

```
pipenv shell
```

If using a Jupyter Notebook, select the Kernel created by this pipenv environment. 

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   └── processed      <- The final, canonical data sets for modeling.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        │
        ├── data       <- Scripts to turn raw data into features for modeling
           └── make_dataset.py
        
     


--------

<p><small>Project organization based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
