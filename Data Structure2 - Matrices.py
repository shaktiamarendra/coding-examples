# Define the matrix
image_matrix=[
    [150, 200, 180],
    [100, 120, 140],
    [90, 80, 110],
    [23, 34, 45]
]

#print type of image_matrix
print(f"Type of image_matrix is:{type(image_matrix)}")

#accessing the elements in the matrix
for i, row in enumerate(image_matrix): # i gives the row index
    for j, column in enumerate(row): # j gives the column index
        print(f"Matrix element at row {i} and column {j} is: {column} ")

#updating the elements in the matrix
for i in range(len(image_matrix)):
    for j in range(len(image_matrix[i])):
       image_matrix[i][j]= i+j
       print(f"Matrix element at row {i} and column {j} is: {image_matrix[i][j]}")
