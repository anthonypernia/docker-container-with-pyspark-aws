import pandas as pd

def test():
    print("Creating a DataFrame...")
    return pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

if __name__ == "__main__":
    print(test())
    print("Done!")