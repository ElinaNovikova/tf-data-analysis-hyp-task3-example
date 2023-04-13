import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id  =  1112920502  # Ваш идентификатор чата, не меняйте название

def solution(x: np.array, y: np.array) -> bool:
    
    
    # Вычисляем средние значения NVP заявок в контрольной и тестовой группах
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    # Вычисляем стандартные отклонения NVP заявок в контрольной и тестовой группах
    x_std = np.std(x)
    y_std = np.std(y)
    
    # Вычисляем статистику t и p-значение
    t_stat, p_value = ttest_ind(x, y, equal_var=False)
    
    # Если p-значение меньше уровня значимости alpha, отвергаем нулевую гипотезу и возвращаем True
    if p_value < 0.05:
        return True
    
    # Иначе не отвергаем нулевую гипотезу и возвращаем False
    else:
        return False
