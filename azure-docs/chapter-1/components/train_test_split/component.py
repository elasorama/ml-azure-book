# Sklearn data spliting 
from sklearn.model_selection import train_test_split

# Pandas for data manipulation
import pandas as pd 

# Defining the component function 
def main(
        input_file_path: str, 
        train_test_ratio: float, 
        train_output_path: str, 
        test_output_path: str
) -> None: 
    """
    Splits the data into train and test sets.

    Args: 
        input_file_path: Path to the data file
        train_test_ratio: Percentage of the data to use for training
        train_output_path: Path to the train data
        test_output_path: Path to the test data
    """
    # Infering the file type 
    file_type = input_file_path.split(".")[-1]

    # Reading the input data
    if file_type == "csv":
        data = pd.read_csv(input_file_path)
    elif file_type == "json":
        data = pd.read_json(input_file_path)
    elif file_type == "xlsx":
        data = pd.read_excel(input_file_path)
    elif file_type == 'parquet':
        data = pd.read_parquet(input_file_path)
    else:
        raise Exception("Unsupported file type")

    data = pd.read_csv(input_file_path)
    print(f"Number of rows in all data: {data.shape[0]}")

    # Spliting the data
    train, test = train_test_split(data, train_size=train_test_ratio)
    print(f"Number of rows in train data: {train.shape[0]}")
    print(f"Number of rows in test data: {test.shape[0]}")

    # Saving the data (only to parquet for this example sake)
    train.to_parquet(train_output_path, index=False)
    test.to_parquet(test_output_path, index=False)

    return

if __name__ == '__main__': 
    # Argument parsing 
    import argparse

    # Parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file_path", type=str, help="Path to the data file")
    parser.add_argument("--train_test_ratio", type=float, help="Share of the data to use for training")
    parser.add_argument("--train_output_path", type=str, help="Path to the train data")
    parser.add_argument("--test_output_path", type=str, help="Path to the test data")
    args = parser.parse_args()

    # Calling the main function
    main(
        input_file_path=args.input_file_path, 
        train_test_ratio=args.train_test_ratio, 
        train_output_path=args.train_output_path, 
        test_output_path=args.test_output_path
    )