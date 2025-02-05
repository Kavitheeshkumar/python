def find_pairs_with_sum(nums, k):
    pairs = set()
   
    seen = set()
    
    for num in nums:
        complement = k - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    
    return list(pairs)

nums = [1, 2, 3, 4, 3, 2, 1]
k = 5
pairs = find_pairs_with_sum(nums, k)
print("Pairs that sum to", k, ":", pairs)
