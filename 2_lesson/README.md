# Customer Churn Analysis

This project uses `inicial.ipynb` to analyze customer cancellations and test simple actions to reduce churn.

## Files
- `inicial.ipynb`
- `cancellations.csv`

## What the notebook does
1. Loads the data with pandas.
2. Removes unnecessary/missing data.
3. Checks churn rate (`cancelou`).
4. Creates charts with Plotly.
5. Applies filters:
   - remove monthly contracts
   - keep customers with up to 4 call center calls
   - keep customers with up to 20 late days
6. Shows churn rate after each filter.

## Install
```bash
pip install pandas plotly
```

## Run
Open `inicial.ipynb` in VS Code or Jupyter and run cells from top to bottom.