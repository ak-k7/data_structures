def quick_sort(arr,low,high):
	i = low - 1
	if low < high:
		for j in range(low, high):
			if arr[j] < arr[high]:
				i += 1
				arr[i], arr[j] = arr[j], arr[i]
		arr[i+1], arr[high] = arr[high], arr[i+1]
		quick_sort(arr,low,i)
		quick_sort(arr,i+1,high)

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Given array is : {0}".format(arr)) 
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array is : {0}".format(arr))
