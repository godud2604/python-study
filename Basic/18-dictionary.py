capitals = {
  'USA': 'Washington DC',
  'India': 'New Dehli',
  'China': 'Beijing',
  'Russia': 'Moscow'
}

print(capitals['USA'])

# capitals['Germany']처럼 존재하지 않는 키(Germany)로 값을 가져오려고 할 경우,
# capitals['Germany']는 Key 오류를 발생시키고 a.get('Germany')는 None을 돌려준다는 차이가 있다.
# print(capitals['Germany'])
print(capitals.get('Germany')) # None


print(capitals.keys()) # dict_keys(['USA', 'India', 'China', 'Russia'])
print(capitals.values()) # dict_values(['Washington DC', 'New Dehli', 'Beijing', 'Moscow'])
print(capitals.items()) # dict_items([('USA', 'Washington DC'), ('India', 'New Dehli'), ('China', 'Beijing'), ('Russia', 'Moscow')])

for key, value in capitals.items():
  print('key', key)
  print('value', value)


capitals.update({ 'Germany': 'Berlin' })
capitals.pop('China')
capitals.clear()

print(capitals)