import os

from tfx.components import CsvExampleGen
from tfx.proto import example_gen_pb2

base_dir = os.getcwd()
data_dir = os.path.join(os.pardir, "data")

# 기존 하위 디렉터리를 설정합니다.
input = example_gen_pb2.Input(splits=[
    example_gen_pb2.Input.Split(name='train', pattern='train/*'),
    example_gen_pb2.Input.Split(name='eval', pattern='eval/*'),
    example_gen_pb2.Input.Split(name='test', pattern='test/*')
])

# input_config 인수를 추가합니다.
example_gen = CsvExampleGen(input_base=os.path.join(base_dir, data_dir), input_config=input)
