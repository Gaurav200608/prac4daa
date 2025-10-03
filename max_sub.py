def max_subarray_with_constraint(resources, constraint):
    def max_crossing_subarray(arr, left, right, mid):
        left_sum = -float('inf')
        total = 0
        for i in range(mid, left-1, -1):
            total += arr[i]
            if total > left_sum:
                left_sum = total
        
        right_sum = -float('inf')
        total = 0
        for i in range(mid + 1, right + 1):
            total += arr[i]
            if total > right_sum:
                right_sum = total
        
        return left_sum + right_sum
    
    def max_subarray(arr, left, right, constraint):
        if left == right:
            return (arr[left], [arr[left]]) if arr[left] <= constraint else (None, [])
        
        mid = (left + right) // 2
        left_sum, left_subarray = max_subarray(arr, left, mid, constraint)
        right_sum, right_subarray = max_subarray(arr, mid + 1, right, constraint)
        cross_sum = max_crossing_subarray(arr, left, right, mid)
        
        best_sum = -float('inf')
        best_subarray = []
        
        if left_sum is not None and left_sum <= constraint:
            best_sum = left_sum
            best_subarray = left_subarray
        
        if right_sum is not None and right_sum <= constraint and right_sum > best_sum:
            best_sum = right_sum
            best_subarray = right_subarray
        
        if cross_sum <= constraint and cross_sum > best_sum:
            best_sum = cross_sum
            best_subarray = []
        
        return best_sum, best_subarray

    if len(resources) == 0:
        return None, []
    
    return max_subarray(resources, 0, len(resources) - 1, constraint)

resources = [2, 1, 3, 4]
constraint = 5
result = max_subarray_with_constraint(resources, constraint)
print("Best subarray:", result[1], "Sum:", result[0])
