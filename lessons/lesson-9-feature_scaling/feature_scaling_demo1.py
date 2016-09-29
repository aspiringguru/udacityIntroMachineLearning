def featureScaling(arr):
    return ( arr[1]-arr[0] )*1.0 / ( arr[2]-arr[0] )

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)
data = [115, 140, 115]
print featureScaling(data)
