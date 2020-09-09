import yaml
# a = {}
# with open("./hello.yaml", "r") as f:
#     data = yaml.unsafe_load(f)
#     print(data)
#     print(type(data))
#     a["name"] = "asdf"

# 写入yaml文件
data = {
    'Search_Data':
        {
          'search_test_002': {
              'expect': {'value': '你好'},
              'value': '你好'
          },
          'search_test_001': {
              'expect': [4, 5, 6],
              'value': 456
          }
        }
}

with  open("hello.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True)








