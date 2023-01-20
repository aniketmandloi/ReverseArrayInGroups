def reverseInGroups(self, arr, N, K):
		i=0
	    while(i<N):
	        #If (ith index +k) is less than total number of elements it means
            #k elements exist from current index so we reverse k elements 
            #starting from current index.
	        if (i+K<N):
	            #reversed function used to reverse any part of the array.
	            arr[i:i+K]=reversed(arr[i:i+K])
	            #updating index from i to i+k.
	            i+=K
	            
	        #Else k elements from current index doesn't exist. 
            #In that case we just reverse the remaining elements.
	        else:
	            #reversed function used to reverse any part of the array.
	            arr[i:]=reversed(arr[i:])
	            #updating index from i to i+k.
	            i+=K
