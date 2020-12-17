# Retrieve values greater than array AVG

## Requirements:
- REQ-1: the application must be able to receive an array of numbers and determine the average value of it.
- REQ-2: the application must be able to retrieve a new array with the numbers of the initial array that are greater than the average value previously calculated.

## Acceptance Criteria
- CRI-1-1: the average value of the array is equal to the summatory of all the numbers in it, divided by the number of elements in the array.

## Scenarios
- SCE-1-1-1: [3,2,1] = [3]
- SCE-1-1-2: [13, 23, -51] = [13, 23]
- SCE-1-1-3: [13, 22, 31, 41, 53, 67, -8 , 28] = 	[31, 41, 53, 67]
- SCE-1-1-4: [-5 , 10, 5, 645] = [645]
- SCE-1-1-5: [8, 11, 12, 13, 14, 15, 268, -52] = [268]
