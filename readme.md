### Installation

```
mkdir out_klines
mkdir markets

pip install -r requirements.txt
pip install --force-reinstall -r requirements.txt
```

### Commands

```
python -m venv .env
source .env/bin/activate

python dump_many.py
python dump_unseen.py
python tf2_dump.py && python tf2_predict_unseen.py
```

### Visualisation

```
python binance_markets_dump.py
python visualize_list.py ETC
python visualize_matrix 12h
```

### Weights

```
- bitcoin hashrate
- sequences leading to peaks 
- day of the week
- day/night
- fear index (calculate?)
- 30min
    - 15min(0, 1)
    - 5min(0, 1, 2, 3, 4, 5)
    - 3min(0, 1, 2, 3, 4, 5 … 9)
    - 1min(0, 1, 2, 3, 4, 5 … 29)

```