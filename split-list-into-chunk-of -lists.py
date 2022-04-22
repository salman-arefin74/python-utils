data = [1,2,3,4,5,6,7,8]

chunks = [data[x:x+2] for x in range(0, len(data), 2)]

print(chunks)