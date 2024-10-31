import json

# data.json 파일 읽기
with open('./topology.json', 'r', encoding='utf-8') as infile:
    data = json.load(infile)

# 한 줄로 줄인 JSON 데이터를 compress.json에 쓰기
with open('./topology-compress.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, separators=(',', ':'))
