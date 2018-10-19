obj = {}
with open("source") as f:
	counter = -1
	start_ascii= ord('A')
	for entry in f:
		matrix=[]
		for raw_row in entry.split(" "):
			row=[]
			for bit in raw_row:
				if bit != "\n":
					if bit == "1":
						row.append(1)
					else:
						row.append(0)
			matrix.append(row)
		obj[chr(counter+ start_ascii)] = matrix
		counter += 1
			
print(obj)
		
		
			
