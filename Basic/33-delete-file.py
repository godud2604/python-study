# os.remove : 어떤 경로의 파일을 삭제해주는 기능
# os.rmdir : 어떤 경로의 디렉토리를 삭제해주는 기능
# os.removedirs : 빈 폴더 삭제 (즉, 파일을 포함하는 폴더는 삭제가 안 된다.)
# => 만약, 파일을 포함하는 폴더를 삭제한다고 하면 OSError를 발생시킨다.
# shutil.rmtree : 파일을 포함하는 폴더를 삭제


import os
import shutil

path = 'test'

try:
  # os.remove(path)
  # os.rmdir(path)
  shutil.rmtree(path)
except FileNotFoundError:
  print('That file was not found')
except PermissionError:
  print('You do not have permission to delete that')
except OSError:
  print('You cannot delete that using that function')
else:
  print(path + ' was deleted')