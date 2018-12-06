# iPhone_healthcare_sample
iPhoneのヘルスケアからデータをExportするサンプル

### usage

```bash
$ git clone https://github.com/masatomix/iPhone_healthcare_sample.git
$ cd iPhone_healthcare_sample
```

iPhoneから書きだしたヘルスケアデータを PC等で解凍すると「書き出したデータ.xml」が得られるので、カレントに配置。


```bash
$ python -m venv ./venv
$ source ./venv/bin/activate
(venv) $ pip install -r requirement.txt
(venv) $ python3 main.py
```


```bash
(venv) $ tail healthcare_data_20181206172036.csv
2017-11-15 14:28:47,2017-11-15 23:52:50 +0900,Cycling,2017-11-15 23:28:47 +0900,HKQuantityTypeIdentifierDistanceCycling,km,7.02
2017-11-18 02:09:16,2017-11-18 12:04:47 +0900,Cycling,2017-11-18 11:09:16 +0900,HKQuantityTypeIdentifierDistanceCycling,km,2.63
2017-11-19 02:48:15,2017-11-19 14:11:40 +0900,Cycling,2017-11-19 11:48:15 +0900,HKQuantityTypeIdentifierDistanceCycling,km,24.85
2017-11-20 23:15:25,2017-11-21 08:34:23 +0900,Cycling,2017-11-21 08:15:25 +0900,HKQuantityTypeIdentifierDistanceCycling,km,4.03
2017-11-21 04:16:56,2017-11-21 13:30:51 +0900,Cycling,2017-11-21 13:16:56 +0900,HKQuantityTypeIdentifierDistanceCycling,km,2.69
2017-11-21 07:54:36,2017-11-21 17:15:55 +0900,Cycling,2017-11-21 16:54:36 +0900,HKQuantityTypeIdentifierDistanceCycling,km,4.46
2017-11-21 07:54:36,2017-11-21 17:15:55 +0900,Cycling,2017-11-21 16:54:36 +0900,HKQuantityTypeIdentifierDistanceCycling,km,4.46
(venv) $

```


### 参考
- [iPhoneのヘルスケアデータから歩数を日別に集計してCSVファイルにする](https://qiita.com/masato/items/72cf6cad5aa3179d64cc)


### リリース履歴

- 0.0.1 新規作成