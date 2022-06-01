import numpy as np

def pgcd(a, b):
    while b:
        a, b = b, a%b
    return a


def mult(f, x):
    f_ = [f[0]*(x**2) + f[1], f[1]*(x**2)]
    if(f_[0]<0 or f_[1]<0):
        a = pgcd(x,f[1])
        x //= a
        f_ = [f[0]*(x**2) + f[1]//(a**2), f[1]*(x**2)]
    
    if(f_[0]<0 or f_[1]<0):
        print(f_)
        exit()
    f = f_
    a = pgcd(f[0],f[1])
    if(a!=1):
        f = [f[0]//a, f[1]//a]
    return f


numbers = np.arange(2,81)

def recursive_mult(f, nums, used=[], lasting_set=[], max_value=0):
    if(len(nums)==14):print(used)
    if(f[1]==2*f[0]):
        #print("got it", used)
        return 1
    elif(f[1]<2*f[0]):
        return 0
    else:
        if(len(nums)==0):
            return in_lasting_set(f, lasting_set,used)
        max_f = compute_total_mult(nums,f)
        if(max_f[0]/max_f[1] + max_value[0]/max_value[1]<1/2):
            return 0
        b=recursive_mult(mult(f,nums[0]), nums[1:], used+[nums[0]], lasting_set=lasting_set, max_value=max_value)
        a=recursive_mult(f, nums[1:],used, lasting_set=lasting_set, max_value=max_value)
        
        if(len(nums)>=18 and a+b!=0):print(len(nums),"local total =",a+b)
        return a+b

def in_lasting_set(f, last_set, used):
    rest = [f[1] - 2*f[0], f[1]*2] if f[1]%2!=0 else [f[1]//2 - f[0], f[1]]
    if(rest[0]<0 or rest[1]<0):
        print("Error",f, rest, 2*f[0]>f[1])
        return 0
    a = pgcd(rest[0],rest[1])
    if(a!=1):
        rest = [rest[0]//a, rest[1]//a]
    L = last_set[np.argwhere(last_set[:,1]==rest[1]),:]
    if(len(L)!=0):
        L=L[:,0,:]
        L = L[np.argwhere(L[:,0]==rest[0]),:]
        #if(len(L)!=0): 
            #print("got it !",len(L), used)
        return len(L)
    else: return 0
    
    
    
def prime(p,Lp):
    for i in Lp:
        if(pgcd(p,i)!=1):return False
    return True

primes = [2]
for n in numbers:
    if(prime(n,primes)):
        primes.append(n)
print("prime numbers :",primes)

def multiples(p):
    return [n*p for n in range(1,80//p +1)]

def prod_frac(L):
    f = [1,1]
    for i in L:
        f=mult(f,i)
    return f

def is_pertinent(root=1, used=[], to_use=[]):
    if(len(to_use)==0):
        if(len(used)!=0):
            f = prod_frac(used)
            return f[1]%root!=0
        else:return False
    else:
        return is_pertinent(root,used+[to_use[0]], to_use[1:]) or is_pertinent(root,used, to_use[1:])

pertinent_primes = [2,3]
for p in primes[2:]:
    if(is_pertinent(p,[],multiples(p))):
        pertinent_primes.append(p)
        
print("pertinent primes numbers :",pertinent_primes)

pertinent_numbers = set(numbers)
for p in primes:
    if(p not in pertinent_primes):
        pertinent_numbers-=set(multiples(p))

pertinent_numbers = np.array(list(pertinent_numbers)[2:])
print("pertinent numbers :",pertinent_numbers)

SEP = 40
to_use, high_numbers = pertinent_numbers[pertinent_numbers<SEP], pertinent_numbers[pertinent_numbers>=SEP]
f = [0,1]
f = mult(f,2)# without 2 or 3 we don't get to 1/2
f = mult(f,3)
print("Using numbers :",to_use)


def compute_all_comb(to_use, used=[]):
    if(len(to_use)==0): return [used]
    a = compute_all_comb(to_use[1:], used)
    b = compute_all_comb(to_use[1:], used+[to_use[0]])
    return a + b

def compute_total_mult(L, f=[0,1]):
    for n in L: f=mult(f,n)
    return f

#high_numbers = high_numbers[high_numbers<=45]
all_comb = compute_all_comb(high_numbers)
max_value = compute_total_mult(high_numbers)
print("all high combs :",len(all_comb))
lasting_set = np.array([compute_total_mult(L) for L in all_comb])
print(lasting_set.shape)
print(recursive_mult(f,to_use,used=[2,3], lasting_set=lasting_set, max_value=max_value))

# 2 3 4 5 : 93
# 2 3 4 6 : 107
# 2 3 4 7 : 29 
# 2 3 4 : 229
# 2 3 5 6 : 72
# [2, 3, 4, 7, 8, 9, 10, 12] actual total = 5