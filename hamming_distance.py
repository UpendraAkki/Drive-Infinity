def hamming_distance(hash1, hash2):
    """
    Calculate the Hamming distance between two hashes.
    
    :param hash1: First hash value (as a hexadecimal string)
    :param hash2: Second hash value (as a hexadecimal string)
    :return: Hamming distance (integer)
    """
    # Convert the hexadecimal hash strings to binary integers
    hash1_bin = int(hash1, 16)
    hash2_bin = int(hash2, 16)
    
    # XOR the two hashes to find differing bits and count them
    return bin(hash1_bin ^ hash2_bin).count('1')


# Example pHashes (hexadecimal strings)
phash1 = "e58e1c431cadd627"
phash2 = "cb546bd4a496333c"

# Calculate Hamming distance
distance = hamming_distance(phash1, phash2)

# Print the result
print(f"Hamming Distance: {distance}")
