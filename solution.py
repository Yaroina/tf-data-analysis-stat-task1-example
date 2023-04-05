import pandas as pd
import numpy as np


chat_id = 395384260 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x = 2 * x / (75 ** 2)
    return x.mean() # Ваш ответ
