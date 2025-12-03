
s = ''

def set(key, value):
  global s
  s += key + ':' + value + ','

def get(key):
  k = ''
  v = ''
  b = ''
  for c in s:
    if c == ':':
      k = b
      b = ''
    elif c == ',':
      if k == key:
        v = b
      b = ''
    else:
      b += c
  return v

if __name__ == '__main__':
  set('date', '12/3/2025')
  set('name', 'keva')
  set('version', 'zero')
  print('name:', get('name'))
