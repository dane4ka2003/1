from standart_deviation import StandartDeviation
from stream_parser.parser import StreamParser
import sqlite3
import time


class StandartDeviationAnalize(object):

    def __init__(self, figis: str, bd_name: str, interval: int = 1):
        self.figis = open(f'{figis}.txt', 'r', encoding='utf-8').readlines()
        self.interval = interval
        self.bd = sqlite3.connect(f'{bd_name}.db')
        self.cur = self.bd.cursor()



    def get_historic_data(self):
        result = {}
        for i in range(len(self.figis)):
            action_volume = []
            figi = self.figis[i].split()[0]
            volumes = self.cur.execute(f'SELECT volume FROM {figi}')
            for el in volumes:
                action_volume.append(int(el[0]))
            result[figi] = action_volume
        return result


    def get_stream_data(self):
        result = {}
        for i in range(len(self.figis)):
            stream_parse = StreamParser(self.figis[i].split()[0], 1)
            result[self.figis[i].split()[0]] = stream_parse.parse()
        return result




a = StandartDeviationAnalize('figis', 'stocks07_09')
print(a.get_historic_data())
print(a.get_stream_data())
