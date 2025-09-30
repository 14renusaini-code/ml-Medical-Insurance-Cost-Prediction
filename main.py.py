from src.data_loader import load_data, preprocess_data
from src.model import train_model, evaluate_model
from sklearn.model_selection import train_test_split

def main():
    df = load_data("data/insurance.csv")
    X_processed, y, preprocessor = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)

    model = train_model(X_train, y_train)
    rmse, r2 = evaluate_model(model, X_test, y_test)

    print(f"RMSE: {rmse:.2f}")
    print(f"R^2 Score: {r2:.2f}")

if __name__ == "__main__":
    main()