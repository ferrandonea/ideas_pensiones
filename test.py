import cython_test
import time

numero = 20000
start_vanilla = time.time()
hola = cython_test.prime_finder_vanilla(numero)
end_vanilla = time.time()
print ("VANILLA", end_vanilla - start_vanilla)

start_vanilla = time.time()
hola = cython_test.prime_finder_optimized(numero)
end_vanilla = time.time()
print ("CYTHON", end_vanilla - start_vanilla)