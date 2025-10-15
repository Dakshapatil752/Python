"""Create and print a two-dimensional array using NumPy (with fallback to nested lists).

Run from PowerShell:
    python "c:/Users/HP/Documents/files/Python/Num -function/two-dimensional.py"
"""

def main():
    try:
        import numpy as np
    except Exception:
        np = None

    if np is not None:
        arr2d = np.array([[1, 2, 3], [4, 5, 6]])
        print("2-D NumPy array:")
        print(arr2d)
        print("Shape:", arr2d.shape)
        print("Dtype:", arr2d.dtype)

        # Create a 2D array using zeros and reshape
        a = np.arange(12)
        mat = a.reshape((3, 4))
        print("Reshaped 3x4 array:")
        print(mat)
    else:
        arr2d = [[1, 2, 3], [4, 5, 6]]
        print("NumPy not available — using nested lists:")
        for row in arr2d:
            print(row)


if __name__ == '__main__':
    main()
