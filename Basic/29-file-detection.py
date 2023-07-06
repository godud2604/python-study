# isfile과 isdir 파일 모두 argument로 확인을 원하는 파일 혹은 디렉토리의 경로를 넣어주면 되고, 그 결과로 존재할 경우 True, 존재하지 않을 경우 False를 return하게 된다.

import os

path = '/Users/ihaeyeong/Desktop/coupang-clone'

if os.path.exists(path):
  print('that location exists!')
  if os.path.isfile(path):
    print('that is a file')
  elif os.path.isdir(path): 
    print('that is a directory')
  
else:
  print("that location doesn't exists!")

