# Medical Insurance Cost Prediction

A regression project to predict medical insurance costs using demographic and health-related features.

## Project Structure

```
insurance-cost-prediction/
│
├── data/
│   └── insurance.csv
├── notebooks/
│   └── insurance_eda_and_model.ipynb
├── src/
│   ├── data_loader.py
│   └── model.py
├── main.py
├── requirements.txt
└── README.md
```

## Dataset

- The dataset (`insurance.csv`) contains features such as age, sex, BMI, children, smoker status, region, and charges.
- [Source: Kaggle - Medical Cost Personal Datasets](https://www.kaggle.com/datasets/mirichoi0218/insurance)

## How to Run

1. **Clone the repository**  
   ```
   git clone <this-repo-url>
   cd insurance-cost-prediction
   ```

2. **Create a virtual environment (optional but recommended)**
   ```
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Run main script**
   ```
   python main.py
   ```

5. **Explore the notebook**
   - Open `notebooks/insurance_eda_and_model.ipynb` in Jupyter Notebook or VS Code for EDA and model training.

## Features

- Data loading and preprocessing
- Exploratory data analysis (EDA)
- Model training (Linear Regression)
- Model evaluation (RMSE, R²)
- Easy-to-read code and modular structure

## License

This project is for educational purposes.

## Contact

For any questions, contact [14renusaini-code](https://github.com/14renusaini-code).
