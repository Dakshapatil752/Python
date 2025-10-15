def main():
	try:
		import numpy as np
	except Exception:
		np = None

	if np is not None:
		arr = np.array([1, 2, 3, 4, 5])
		print("1-D array (np.array):", arr)

		arr2 = np.arange(0, 10, 2)
		print("1-D array (np.arange 0..8 step2):", arr2)

		# show type and shape
		print("Type:", type(arr), "Shape:", arr.shape)
	else:
		arr = [1, 2, 3, 4, 5]
		arr2 = list(range(0, 10, 2))
		print("NumPy not installed — using Python lists")
		print("1-D list:", arr)
		print("1-D list (range 0..8 step2):", arr2)


if __name__ == '__main__':
    main()

