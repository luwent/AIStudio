import numpy as np
import IStudio as iv

transform = iv.IPFFTTransform(1024, 0, 0)

a = np.array([1+1.j, 2+2j], dtype=np.complex128)
b = np.empty([2], dtype=np.complex128)
print(a.dtype)
transform.SendRevComplex(a, b)
print(a)
print(b)