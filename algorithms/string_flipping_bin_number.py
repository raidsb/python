def flippingBits(n):
    bin_n = f'{n:032b}'
    bin_n_2 = ""
    for i in range(0, len(bin_n)):
        bin_n_2 += '1' if bin_n[i] == '0' else '0'
    
    flipped_int = int(bin_n_2, 2)    
    return flipped_int
    
