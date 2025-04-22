import numpy as np
#Provides An array object of arbitrary homogeneous items \
#Fast mathematical operations over arrays \
#Linear Algebra, Fourier Transforms, Random Number Generation
print(f"Installed numpy version is: {np.__version__}")

# Create a tensor representing RGB color images
image_tensor=np.zeros((3,224,224,3), dtype=np.uint8)

#Accessing the elements in the tensor
print(image_tensor[0,0,0,0])

#Updating the elements in the tensor
image_tensor [1,100,100,1]= 128
image_tensor [1,100,100,2]= 90

#Dimensions of the tensor
tensor_shape=image_tensor.shape
print("Tensor Shape:", tensor_shape)

#Looping through the tensor
for image_index in range(tensor_shape[0]):
    for row_index in range(tensor_shape[1]):
        for column_index in range(tensor_shape[2]):
            for channel_index in range(tensor_shape[3]):
                if image_tensor[image_index][row_index][column_index][channel_index]: # Print non-zero elements
                    print(f"Tensor Element at Image Index {image_index}, Row Index {row_index}, Column Index {column_index} and Channel Index {channel_index} is:\
                      {image_tensor[image_index][row_index][column_index][channel_index]}")
