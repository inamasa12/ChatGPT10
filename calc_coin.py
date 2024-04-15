def calc_coin(total, a, b, c, d):
    """
    Finds a combination of coins that equals 'total' yen, using the minimum number of coins.
    Inputs:
        total: the total amount to be paid
        a: number of 10 yen coins
        b: number of 50 yen coins
        c: number of 100 yen coins
        d: number of 500 yen coins
    Returns:
        A tuple containing the number of 10 yen, 50 yen, 100 yen, and 500 yen coins to be used.
        Returns None if it's not possible to make the total with the given coins.
    """
    
    min_coins = float('inf')
    best_combo = None

    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                for l in range(d + 1):
                    if (i * 10 + j * 50 + k * 100 + l * 500 == total):
                        if i + j + k + l < min_coins:
                            min_coins = i + j + k + l
                            best_combo = (i, j, k, l)
                            
    return best_combo

# Test the modified function with the same example, but with total as the first argument
print(calc_coin(1550, 0, 1, 0, 3))  # Example input
