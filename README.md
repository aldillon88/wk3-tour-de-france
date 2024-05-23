# Tour de France
### The evolution of road cyclings toughest stage race

## Project Overview
The Tour de France is one of the world's oldest and most iconic road cycling races, taking place for the first time in 1903.

- *How has the race changed since its inception, from terrain to rider performance?*
- *What characteristics are commong among the champions of the race?*

This project aims to answer these questions through a thorough analysis of over 100 years of data.

## Installation and Setup
### Codes and Resources Used
- Jupyter Notebook 7.2.0
- Python 3.11.7
### Python Packages Used
- General Purpose: `re`, `datetime`, `ast`, `threading`, `webbrowser`
- Data Manipulation: `pandas` and `numpy`
- Data Visualization: `plotly`
- Other: `dash` and `kaleido`

To install external libraries, first navigate to the `./project/` directory and activate `venv`
1. <pre>cd ./project</pre>
2. <pre>source venv/bin/activate</pre>
Use `pip` to install external libraries:
1. <pre>pip install notebook</pre>
2. <pre>pip install pandas</pre>
3. <pre>pip install plotly==5.22.0</pre>
4. <pre>pip install dash</pre>
5. <pre>pip install -U kaleido</pre>

## Data
### Source Data
The data for this project was sourced from Maven Analytics: [https://mavenanalytics.io/challenges/maven-tour-de-france-challenge](https://mavenanalytics.io/challenges/maven-tour-de-france-challenge/4cf1cbec-e206-4f42-8725-dfea9ab38aa1)
By downloading the .zip file available from the above url you will receive 5 unique datasets in .csv format:
  1. `data_dictionary.csv` - this includes an explanation for all columns in the dataset.
  2. `tdf_finishers.csv` - a list of all riders who have finished the entire Tour de France.
  3. `tdf_stages.csv` - information about each stage of the Tour de France.
  4. `tdf_tours.csv` - information about every tour.
  5. `tdf_winners.csv` - a list of all Tour de France winners with additional information.
### Data Preprocessing
**Step 1.** Create a notebook for each individual dataset (excluding the `data_dictionary.csv`).\
**Step 2.** Use `pd.read_csv` to create the dataframes. This required the use of the `encoding='cp1252'` parameter for the `tdf_finishers.csv` and `tdf_winners.csv` files because of the characters used in some of the rider names.\
**Step 3.** Apply custom functions to trim all whitespace from column names and values, replace " " with "_" in column names and change all column names and string values to lowercase for ease of use.\
**Step 4.** Clean and format the data so it can be used for analysis. This involved extracting parts from string values, interpreting string values for finishing times and returning those values as lists showing "[hours, minutes, seconds]", handling missing values and modifying data types, adding new columns for calculated data and dropping unused columns to reduce the size of the dataset.\
**Step 4.** Exporting the clean data to the `data/clean` directory for use in `main_notebook.ipynb` notebook.

## Code Structure
|---project\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---data\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---clean\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---finishers.csv\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---stages.csv\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---tours.csv\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---winners.csv\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---raw\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---data_dictionary.csv\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---tdf_finishers.csv\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---tdf_stages.csv\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---tdf_tours.csv\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---tdf_winner.csv\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---images\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---notebooks\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---finishers.ipynd\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---functions.py\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---main_notebook.ipynd\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---stages.ipynd\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---tours.ipynd\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---winners.ipynd\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---pandas\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---requirements-dev.in\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---requirements-dev.txt\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---requirements.in\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---requirements.txt\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---slides\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---venv\

## Results and Evaluation
![km](https://github.com/aldillon88/wk3-tour-de-france/assets/169060819/3892d0c8-7b32-4f34-b3d2-765a13afb6e8)
![time](https://github.com/aldillon88/wk3-tour-de-france/assets/169060819/c36fa5c0-844e-4ec6-b566-793dc9082ffa)
![stage_type](https://github.com/aldillon88/wk3-tour-de-france/assets/169060819/3a75e550-8aad-4ad3-9ecf-ad78822ff445)
![age](https://github.com/aldillon88/wk3-tour-de-france/assets/169060819/4b4ee1fd-de81-439c-ab8b-bde8066a0c8d)
