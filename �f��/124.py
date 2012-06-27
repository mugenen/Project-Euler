def rad(MAX):
  rad = [1] * MAX
  
  i = 2
  while MAX + 1 > i:
    if rad[i - 1] == 1:
      rad[i - 1] *= i
      temp = i * 2
      while temp < MAX + 1:
        rad[temp - 1] *= i
        temp += i
    
    if i == 2:
      i += 1
    else:
      i += 2
  
  return rad

N = 100000

rad_i = zip(rad(N), xrange(1, N + 1))
rad_i.sort()

print rad_i[9999][1]