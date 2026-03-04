# Lesson 3 - Credit Score Prediction

This lesson builds a simple machine learning model to predict customer credit score (`Good`, `Standard`, `Poor`).

## Files

- `inicial.ipynb` - main notebook with the full workflow
- `client.csv` - training dataset
- `new_clients.csv` - new customer data for predictions

## Requirements

- Python 3.9+
- pandas
- scikit-learn

Install dependencies:

```bash
pip install pandas scikit-learn
```

## What the notebook does

1. Loads customer data
2. Encodes categorical columns
3. Splits data into train/test sets
4. Trains two models (Random Forest and KNN)
5. Compares accuracy
6. Uses the best model to predict new customers

## Run

Open `inicial.ipynb` and run cells from top to bottom.
