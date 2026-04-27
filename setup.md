# Setup Guide for Team Members

## Step 1 — Install Miniconda
Download from: https://docs.conda.io/en/latest/miniconda.html
Install with default settings.

## Step 2 — Clone the Repository
Open Anaconda Prompt and run:

git clone https://github.com/AhmadA1i/AI_Project.git
cd AI_Project

## Step 3 — Create the Environment
conda create -n ai-project python=3.11
conda activate ai-project

## Step 4 — Install Dependencies
pip install -r requirements.txt

## Step 5 — Register Jupyter Kernel
python -m ipykernel install --user --name=ai-project --display-name "Python (ai-python)"

## Step 6 — Add the Dataset
Download all 4 CSV files from Kaggle:
https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset

Place them inside the /data folder:
- dataset.csv
- Symptom-severity.csv
- symptom_Description.csv
- symptom_precaution.csv

## Step 7 — Launch Jupyter
jupyter notebook

Open your assigned phase notebook.
Make sure the kernel is set to "Python (ai-lab)".

## Step 8 — Daily Workflow
# Before starting work
git pull origin main

# After finishing work
git add .
git commit -m "phase2: implemented BFS and DFS (for example)"
git push origin main