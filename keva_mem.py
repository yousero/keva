
mem = {}

def set(key, value):
  mem[key] = value

def get(key):
  return mem.get(key, '')

def reset():
  mem = {}

def delete(key):
  del mem[key]

if __name__ == '__main__':
  set('date', '12/3/2025')
  set('name', 'keva')
  set('version', 'zero')
  set('version', 'two')
  set('trash', 'qweqwe')
  delete('trash')
  print('name:', get('name'))
  print('trash:', get('trash'))
