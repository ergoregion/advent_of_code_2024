import numba
import functools

with (open('data/day22data', 'r') as file):
    lines = file.readlines()


buyers = [int(s.strip('\n')) for s in lines]
print(buyers)

@numba.jit
def mix(number, n):
    return number^n

print(mix(42,15))

@numba.jit
def prune(number):
    return number % 16777216

print(prune(100000000))

@numba.jit
def new_number(n):
    a = prune(mix(n,n*64))
    b= mix(a,a // 32)
    c = prune(mix(2048*b,b))
    return c

print(new_number(123))

@numba.jit
def new_number_n_times(n, times):
    result = n
    for i in range(times):
        result = new_number(result)
    return result

print(new_number_n_times(123,1))
print(new_number_n_times(123,10))


print(new_number_n_times(1,2000))
print(new_number_n_times(10,2000))
print(new_number_n_times(100,2000))
print(new_number_n_times(2024,2000))

result = 0;
for i in buyers:
    result += new_number_n_times(i,2000)
print(result)


@numba.jit
def price(n, times):
    return new_number_n_times(n, times)%10

prices = [price(123,i) for i in range(10)]
print(prices)
print([prices[i+1]-prices[i] for i in range(9)])


def find_sub_list(sl,l):
    sll=len(sl)
    for ind in (i for i,e in enumerate(l) if e==sl[0]):
        if l[ind:ind+sll]==sl:
            return ind,ind+sll-1


def winnings (sequence, n, times):
    prices = [price(n, i) for i in range(times+1)]
    price_jumps = [prices[i+1]-prices[i] for i in range(times)]
    index = find_sub_list(sequence, price_jumps)
    if index is None:
        return 0
    else:
        return prices[index[1]+1]



print(winnings([-1,-1,0,2], 123,10))


@functools.cache
def prices2000(n):
    return [price(n, i) for i in range(2000+1)]

@functools.cache
def priceJumps2000(n):
    prices = prices2000(n)
    return [prices[i + 1] - prices[i] for i in range(2000)]



def winnings2000 (sequence, n):
    prices = prices2000(n)
    price_jumps = priceJumps2000(n)
    index = find_sub_list(sequence, price_jumps)
    if index is None:
        return 0
    else:
        return prices[index[1]+1]


print([winnings2000([-2,1,-1,3], i) for i in [1,2,3,2024]])



def solve():
    best_price = 0
    for i in reversed(range(10)):
        print(f"i = {i}")
        for j in range(10):
            print(f"j = {j}")
            for k in reversed(range(10)):
                for l in range(10):
                    for m in range(10):
                        sequence = [l-m,k-l,j-k,i-j]
                        result = sum([winnings2000(sequence, i) for i in buyers])
                        if result > best_price:
                            best_price = result
                            print(f'new best prince: {best_price}, sequence: {sequence}')
                print('.', end='')
    return best_price

print(f"Best Score: {solve()}")



