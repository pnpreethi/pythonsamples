"""First plot sample code to import matplotlib"""
import matplotlib.pyplot as plt
year = [1900, 1950, 1975,2000]
pop = [3.0, 4.0, 7.0, 9.0]
plt.scatter(year, pop)
plt.show()
print(year[len(year)-1])
