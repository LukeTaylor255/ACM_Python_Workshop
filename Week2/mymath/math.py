def sqrt(x):
    return x**0.5


def factorial(x):
    ans = 1
    for k in range(x):
        ans *= k+1
    return ans


class Factorial:
    # Class variables precomputed and index.
    # These allow us to store a state used by all objects of type Factorial
    precomputed = [1, 1]
    index = 1

    @staticmethod # Does not depend on self, so we make factorial a static method
    def factorial(x):
        if(x <= Factorial.index):
            print("Saved time with precomputed factorial")
            return Factorial.precomputed[x]

        ans = Factorial.precomputed[Factorial.index] # Start from known value
        for k in range(Factorial.index + 1, x + 1):
            ans *= k
            if(k >= len(Factorial.precomputed)):
                print("Resizing precomputed values")
                Factorial.precomputed += [0] * len(Factorial.precomputed)
            Factorial.precomputed[k] = ans
            Factorial.index = k
        return Factorial.precomputed[x]


def sin(x):
    ans = 0
    neg = 1
    f = Factorial()
    for k in range(1,5):
        #print("k="+str(k)+",f="+str(f.factorial(2*k-1)))
        print("precomputed=" + str(Factorial.precomputed) + ",index=" + str(Factorial.index))
        ans += neg * x**(2*k-1) / f.factorial(2*k-1)
        neg *= -1
    return ans
