# Pickle file loading 
import pickle 

# Data reading 
import pandas as pd

# Defining the component function
def main(
        input_data_path: str, 
        input_model_path: str,
) -> None: 
    """
    Evaluates a linear regression model.

    Args: 
        input_data_path: Path to the data file
        input_model_path: Path to the model
        output_data_path: Path to the data with predictions
    """
    # Reading the data
    data = pd.read_parquet(input_data_path)
    print(f"Number of rows in all data: {data.shape[0]}")

    # Loading the model
    with open(input_model_path, "rb") as f:
        model = pickle.load(f)

    # Predicting the data
    data["y_pred"] = model.predict(data[['x']])

    # Printing the MSE statistic 
    mse = ((data["y"] - data["y_pred"]) ** 2).mean()
    print(f"MSE: {mse}")

    return

if __name__ == '__main__':
    # Argument parsing 
    import argparse

    # Parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_data_path", type=str, help="Path to the data file")
    parser.add_argument("--input_model_path", type=str, help="Path to the model")
    args = parser.parse_args()

    # Calling the main function
    main(
        input_data_path=args.input_data_path,
        input_model_path=args.input_model_path
    )