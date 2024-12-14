﻿"""
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.
"""


import json
import os
import pickle

def json_to_pickle(directory='.'):
    for file in os.listdir(directory):
        file_name, file_exten = os.path.splitext(file)
        if file_exten == '.json':
            with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
                data = json.load(f)
            with open(os.path.join(directory, file_name + '.pickle'), 'wb') as f:
                pickle.dump(data, f)


if __name__=='__main__':
    json_to_pickle()