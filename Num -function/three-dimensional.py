"""Create and print three-dimensional arrays using NumPy (with fallback to nested lists).

Run from PowerShell:
    python "c:/Users/HP/Documents/files/Python/Num -function/three-dimensional.py"
"""

def main():
    try:
        import numpy as np
    except Exception:
        np = None

    if np is not None:
        # Create a simple 3-D array from a nested list
        arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        print("3-D NumPy array (from nested list):")
        print(arr3d)
        print("Shape:", arr3d.shape)
        print("Dtype:", arr3d.dtype)

        # Create a 3-D array using arange and reshape: shape (2,3,4)
        a = np.arange(24)
        mat3 = a.reshape((2, 3, 4))
        print("\n3-D NumPy array (arange reshape 2x3x4):")
        print(mat3)
        print("Shape:", mat3.shape)

        # Useful examples: zeros, ones, random
        print("\nzeros 2x2x2:")
        print(np.zeros((2, 2, 2)))
        print("ones 2x2x2:")
        print(np.ones((2, 2, 2)))
        print("random 2x2x2:")
        print(np.random.rand(2, 2, 2))

    else:
        # Fallback: nested Python lists representing 3-D arrays
        arr3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
        print("NumPy not available — using nested lists for 3-D array:")
        for i, mat in enumerate(arr3d):
            print(f"Layer {i}:")
            for row in mat:
                print(row)


if __name__ == '__main__':
    main()
