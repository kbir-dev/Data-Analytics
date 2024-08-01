import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
y = np.arange(10, 110, 10)

print("x:", x)
print("y:", y)

plt.figure(figsize=(6, 6))
plt.plot(x, y, 'r--')
plt.title("Linear Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

