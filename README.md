# House_Rental


![House Rental](data\interim\maxresdefault.jpg)
# Aim:
This repository contains a comprehensive data science project focused on predicting rental prices for residential properties. It includes data exploration, feature engineering, model development, and evaluation using Python and Jupyter Notebooks. The workflow demonstrates best practices in data cleaning, feature selection, and performance assessment with real-world rental datasets.

## Data Dictionary

| Column Name           | Description                                                      |
|---------------------- |------------------------------------------------------------------|
| advertised_date       | Date of posting advertisement                                    |
| number_of_bedrooms    | Number of Bedrooms                                               |
| rent                  | Weekly rent                                                      |
| floor_area            | Size of the property                                             |
| level                 | Level of the property                                            |
| suburb                | Name of suburb                                                   |
| furnished             | Furnishing status of the property                                |
| tenancy_preference    | Type of Tenant Preferred by the Owner or Agent                   |
| number_of_bathrooms   | Number of Bathrooms                                              |
| point_of_contact      | Person to reach out for more information                         |
| secondary_address     | Secondary number of the property (such as unit number)           |
| building_number       | Building number of the property                                  |
| street_name           | Street name of the property                                      |
| street_suffix         | Street suffix of the property                                    |
| prefix                | Prefix of the point of contact                                   |
| first_name            | First name of the point of contact                               |
| last_name             | Last name of the point of contact                                |
| gender                | Gender of the point of contact                                   |
| phone_number          | Phone number of the point of contact                             |
| email                 | Email of the point of contact                                    |

# Setup:
Run the `SetYouUp.ipynb` file to get started.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         house_rental and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── house_rental   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes house_rental a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

