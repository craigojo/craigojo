import os

def list_files(base, suffix):
  assert os.path.isdir(base)
  for file in os.listdir(base):
    path = os.path.join(base, file)
    if path.endswith(suffix):
      print(path)
    if os.path.isdir(path):
      list_files(path, suffix)