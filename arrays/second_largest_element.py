# code -> https://practice.geeksforgeeks.org/problems/second-largest3735/1
def print2largest(self,arr, n):
		# code here
		largest = arr[0]
		largest2 = -1
		
		for i in range(1, n):
            if arr[i] > largest:
                largest2 = largest
                largest = arr[i]
            """
            arr[i] != largest: This condition checks if the current element arr[i] is not equal to the largest element largest. 
            This condition is necessary to avoid considering duplicate values as the second largest. If arr[i] is equal to largest, 
            we skip this element.

            arr[i] > largest2: This condition checks if the current element arr[i] is greater than the current second largest element 
            largest2. If this condition is true, it means we have found a new candidate for the second largest element. 
            We update the value of largest2 with the current element arr[i].
            """
            elif arr[i] != largest and arr[i] > largest2:
                largest2 = arr[i]
        return largest2
