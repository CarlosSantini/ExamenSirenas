import pandas as pd
from src import config
from feature_processing import feature_process


if __name__ == '__main__':
    sirenas_historico = pd.read_csv(config.SIRENAS_HISTORICO)
    sirenas = pd.read_csv(config.SIRENAS)

    feature_process(sirenas_historico, sirenas)