
s = ''

def escape(data):
  data = data.replace(':', '\\:')
  data = data.replace(',', '\\,')
  return data

def deescape(data):
  data = data.replace('\\:', ':')
  data = data.replace('\\,', ',')
  return data

def set(key, value):
  global s
  key = escape(key)
  value = escape(value)
  s += key + ':' + value + ','

def get(key):
  key = deescape(key)
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

def reset():
  global s
  s = ''

def delete(key):
  global s
  key = deescape(key)
  k = ''
  v = ''
  b = ''
  r = ''
  for c in s:
    if c == ':':
      k = b
      b = ''
    elif c == ',':
      if k != key:
        v = b
        r += k + ':' + v + ','
      b = ''
    else:
      b += c
  s = r


if __name__ == '__main__':
  set('olddate', '12/3/2025')
  reset()
  set('date', '12/3/2025')
  set('name', 'keva')
  set('version', 'zero')
  set('version', 'two')
  set('trash', 'qweqwe')
  delete('trash')
  print('name:', get('name'))
  print('trash:', get('trash'))

