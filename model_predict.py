import sys
import tensorflow as tf
import numpy as np
import pandas as pd
from datetime import datetime

from src.parameters_usdt import market, assets
from src.service.reporter import render_console_table
from src.service.predictor_unseen import data_load_parallel_all, make_prediction_ohlc_close

np.set_printoptions(precision=4)
pd.set_option("display.precision", 4)

interval = sys.argv[1]
start_at = datetime.now()
report = []

model = tf.keras.models.load_model('model/gru-a.keras')

collection = data_load_parallel_all(assets=assets, market=market, interval=interval)

time_download = datetime.now() - start_at

for data in collection:
    asset, x_df, last_item = data

    y_df = make_prediction_ohlc_close(x_df, model)

    report.append((asset, last_item, x_df, y_df))

time_prediction = datetime.now() - start_at

render_console_table(report)

print(f'start: {start_at}')
print(f'interval: {interval}')
print(f'download: {time_download}')
print(f'prediction: {time_prediction}')
