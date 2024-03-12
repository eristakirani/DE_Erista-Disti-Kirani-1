def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(start, count):
    """Generate count prime numbers starting from start."""
    primes = []
    num = start
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def prime_rectangle(height, width, start):
    primes = generate_primes(start, height * width)
    prime_sum = sum(primes)

    for i in range(height):
        row = ' '.join(map(str, primes[i*width : (i+1)*width]))
        print(row)
    
    print(prime_sum)

# Test cases
prime_rectangle(2, 3, 13)
prime_rectangle(5, 2, 1)
