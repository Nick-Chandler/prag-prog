def change_pen(pen:int):
	pen += 1

if __name__ == "__main__":
	pen = 0
	print(f"Pen Value is {pen}")
	pen = change_pen(pen)
	print(f"Pen Value is {pen}")