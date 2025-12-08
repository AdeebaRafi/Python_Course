T=int(input())
for t in range(T):
  N=int(input())
  avg=N//2

  for r in range(N):
    row=""
    for c in range(N):
      if c == 0 or c == N-1:
        row +="#"
      elif r<= avg and c==r:
        row+="#"
      elif r<= avg and c==N-1-r:
        row +="#"
      else:
        row += "."
    print(row)