'''
pip install hdfs pyarrow pandas
'''

from hdfs import InsecureClient
import pyarrow.parquet as pq
import pandas as pd
import io

# HDFS 클라이언트 설정
hdfs_client = InsecureClient('http://10.10.20.134:9870', user='itcous')


# HDFS 디렉토리에서 Parquet 파일 목록 가져오기
hdfs_directory = '/database/its/master/tb_atrd/2024/05/21'
files = hdfs_client.list(hdfs_directory)
print(files)

# Parquet 파일 읽기
for file in files:
    if file.endswith('.parquet'):
        file_path = f'{hdfs_directory}/{file}'
        with hdfs_client.read(file_path) as reader:
            file_content = reader.read()
            table = pq.read_table(file_content)
            df = table.to_pandas()
            print(df)
