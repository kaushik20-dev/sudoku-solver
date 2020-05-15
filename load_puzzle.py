import pandas as pd


class LoadPuzzle:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)
    
    def get_puzzle(self):
        return df.to_numpy()

