
mem = {}

def set(key, value):
  mem[key] = value

def get(key):
  return mem[key]

if __name__ == '__main__':
  set('name', 'keva')
  print('name:', get('name'))
