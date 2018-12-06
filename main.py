# -*- coding: utf-8 -*-

from lxml import objectify
import pandas as pd
from pandas import DataFrame
from datetime import datetime
import sys
from logging import getLogger


def main(args):
    log = logger_configure(getLogger(__name__))
    log.debug('Parse開始')

    parsed = objectify.parse(open('書き出したデータ.xml'))
    log.debug('Parse完了')

    log.debug('Data配列作成開始')
    dict_array = create_dict_array(parsed)
    log.debug('Data配列作成完了')

    log.debug('DataFrame作成開始')
    df = DataFrame(dict_array)
    df.index = pd.to_datetime(df['startDate'])
    log.debug('DataFrame作成完了')

    log.info(df.head(100))

    df.to_csv('./healthcare_data_{0}.csv'.format(datetime.now().strftime('%Y%m%d%H%M%S')),
              float_format='%.4f')


def create_dict_array(parsed):
    root = parsed.getroot()
    headers = ['type', 'unit', 'startDate', 'endDate', 'value', 'sourceName']

    # ゼロ番目の element を表示してみた
    # [('type', 'HKQuantityTypeIdentifierBodyMassIndex'), ('sourceName', 'omron connect'),
    #  ('sourceVersion', '003.004.00000.001'), ('unit', 'count'), ('creationDate', '2017-12-10 16:48:55 +0900'),
    #  ('startDate', '2017-12-10 16:46:43 +0900'), ('endDate', '2017-12-10 16:46:43 +0900'), ('value', 'xx.4')]
    # for i, element in enumerate(root.Record):
    #     if i == 0: print(element.attrib.items())

    #  なので、element.attrib.items() のキー 'type','sourceName',... がheaders に含まれている文字ならば
    #  Dict内包表記で、
    #  { k1:v1, k2:v2, ..} つまり
    #  {
    #    'type': 'HKQuantityTypeIdentifierBodyMassIndex',
    #    'sourceName': 'omron connect'
    #    ...
    #  } ってなる
    data = [({key: value for key, value in element.attrib.items() if key in headers}) for element in root.Record]
    return data


def logger_configure(logger):
    # cf: https://qiita.com/mimitaro/items/9fa7e054d60290d13bfc

    from logging import StreamHandler, Formatter, DEBUG, INFO

    logger.propagate = False

    # ハンドラに渡すエラーメッセージの最低レベル
    logger.setLevel(DEBUG)

    # Handler 作成
    console_handler = StreamHandler()
    # 出力するエラーメッセージの最低レベル(loggerには、ハンドラが複数設定出来るので、ハンドラごとに出力レベルを設定出来る)
    console_handler.setLevel(DEBUG)
    formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    # Handler 作成 以上

    logger.addHandler(console_handler)
    return logger


if __name__ == "__main__":
    main(sys.argv)
