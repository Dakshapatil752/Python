"""Demonstrate common NumPy functions (with fallback behaviors if NumPy missing).

This script shows ufuncs, aggregation, reshaping, dot product, broadcasting and masking.
"""

def main():
    try:
        import numpy as np
    except Exception:
        np = None

    if np is None:
        print("NumPy is not installed. This script needs NumPy for full demonstrations.")
        print("Install with: python -m pip install numpy")
        return

    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])

    print("a:", a)
    print("b:", b)

    print("Vectorized add (ufunc):", np.add(a, b))
    print("Square (ufunc):", np.square(a))
    print("Sum of a:", np.sum(a))
    print("Mean of b:", np.mean(b))

    M = np.arange(12).reshape(3, 4)
    print("Matrix M (3x4):")
    print(M)

    # Dot product
    v = np.array([1, 0, -1])
    w = np.array([2, 3, 4])
    print("Dot product v.w:", np.dot(v, w))

    # Broadcasting
    x = np.array([[1], [2], [3]])
    y = np.array([10, 20, 30])
    print("Broadcast x + y:")
    print(x + y)

    # Masking
    data = np.array([5, 12, 7, 18, 3])
    mask = data > 10
    print("Data:", data)
    print("Mask (data > 10):", mask)
    print("Filtered:", data[mask])

    # Fancy indexing
    print("Select indices 0 and 3:", data[[0, 3]])


if __name__ == '__main__':
    main()
