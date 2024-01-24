# Linear regression model 
from sklearn.linear_model import LinearRegression

# Data reading 
import pandas as pd

# Pickle file saving 
import pickle

# Defining the component function
def main(
        input_data_path: str, 
        output_model_path: str
) -> None: 
    """
    Trains a linear regression model.

    Args: 
        input_data_path: Path to the data file
        output_model_path: Path to the model
    """
    # Reading the data
    data = pd.read_parquet(input_data_path)
    print(f"Number of rows in all data: {data.shape[0]}")

    # Spliting the data
    X = data.drop("y", axis=1)
    y = data["y"]

    # Training the model
    model = LinearRegression()
    model.fit(X, y)

    # Saving the model
    with open(output_model_path, "wb") as f:
        pickle.dump(model, f)

    return

if __name__ == '__main__':
    # Argument parsing 
    import argparse

    # Parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_data_path", type=str, help="Path to the data file")
    parser.add_argument("--output_model_path", type=str, help="Path to the model")
    args = parser.parse_args()

    # Calling the main function
    main(
        input_data_path=args.input_data_path,
        output_model_path=args.output_model_path
    )