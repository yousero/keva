
mem = {}

def set(key, value):
  mem[key] = value

def get(key):
  return mem.get(key, '')

def reset():
  global mem
  mem = {}

def delete(key):
  mem.pop(key, None)

if __name__ == '__main__':  
  set('olddate', '12/3/2025')
  reset()
  set('date', '12/4/2025')
  set('name', 'keva')
  set('version', 'zero')
  set('version', 'two')
  set('trash', 'qweqwe')
  delete('trash')
  print('name:', get('name'))
  print('trash:', get('trash'))
