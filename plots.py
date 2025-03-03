import numpy as np
import matplotlib.pyplot as plt

# for digit 0
# part1
def f1(x):
    return -4.6875 * x**3 + 1.4063 * 10**1 * x**2 - 1.1375 * 10**1 * x + 5.0000

def f2(x):
    return 1.1719 * x**3 - 7.0313 * x**2 + 1.3938 * 10**1 * x - 5.1250

x1 = np.linspace(1, 1.2, 100)
x2 = np.linspace(1.2, 2, 100)

y1 = f1(x1)
y2 = f2(x2)

plt.plot(x1, y1)
plt.plot(x2, y2)

# part2
def f1(x):
    return -1.1719 * x**3 + 7.0313 * x**2 - 1.3938 * 10**1 * x + 1.3125 * 10**1

def f2(x):
    return 4.6875 * x**3 - 4.2188 * 10**1 * x**2 + 1.2388 * 10**2 * x - 1.1550 * 10**2

x1 = np.linspace(2, 2.8, 100)
x2 = np.linspace(2.8, 3, 100)

y1 = f1(x1)
y2 = f2(x2)

plt.plot(x1, y1)
plt.plot(x2, y2)

# part3
def f1(x):
    return 1.1719 * x**3 - 7.0313 * x**2 + 1.3938 * 10**1 * x - 7.1250

def f2(x):
    return -4.6875 * x**3 + 4.2188 * 10**1 * x**2 - 1.2388 * 10**2 * x + 1.2150 * 10**2

x1 = np.linspace(2, 2.8, 100)
x2 = np.linspace(2.8, 3, 100)

y1 = f1(x1)
y2 = f2(x2)

plt.plot(x1, y1)
plt.plot(x2, y2)

# part4
def f1(x):
    return 4.6875 * x**3 - 1.4063 * 10**1 * x**2 + 1.1375 * 10**1 * x + 1.0000

def f2(x):
    return -1.1719 * x**3 + 7.0313 * x**2 - 1.3938 * 10**1 * x + 1.1125 * 10**1

x1 = np.linspace(1, 1.2, 100)
x2 = np.linspace(1.2, 2, 100)

y1 = f1(x1)
y2 = f2(x2)

plt.plot(x1, y1)
plt.plot(x2, y2)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Digit 0')
plt.legend()
plt.grid(True)
plt.show()

############################################################

# for digit 1
# part1

def f1(x):
    return 1.3605 * x**3 - 4.0816 * x**2 + 4.8435 * x + 1.8776

def f2(x):
    return -3.1746 * x**3 + 1.9048 * 10**1 * x**2 - 3.4476 * 10**1 * x + 2.4159 * 10**1

x1 = np.linspace(1, 1.7, 100)
x2 = np.linspace(1.7, 2, 100)

y1 = f1(x1)
y2 = f2(x2)

plt.plot(x1, y1)
plt.plot(x2, y2)

# part2
y = np.linspace(1, 6, 100)
x = np.full_like(y, 2)

plt.plot(x, y)

# part3
x = np.linspace(1, 3, 100)
y = np.full_like(x, 1)


plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Digit 1')
plt.legend()
plt.grid(True)
plt.show()

############################################################

# for digit 2
# part1

def f1(x):
    return -3.0000 * 10**(-1) * x**3 + 9.0000 * 10**(-1) * x**2 + 1.0000 * x + 3.4000

def f2(x):
    return 3.0000 * 10**(-1) * x**3 - 2.7000 * x**2 + 8.2000 * x - 1.4000

x1 = np.linspace(1, 2, 100)
x2 = np.linspace(2, 3, 100)

y1 = f1(x1)
y2 = f2(x2)

plt.plot(x1, y1)
plt.plot(x2, y2)

# part2

def f1(x):
    return -3.0000 * 10**(-1) * x**3 + 2.7000 * x**2 - 8.2000 * x + 1.5400 * 10**(1)

def f2(x):
    return 3.0000 * 10**(-1) * x**3 - 4.5000 * x**2 + 2.0600 * 10**(1) * x - 2.3000 * 10**(1)

x1 = np.linspace(3, 4, 100)
x2 = np.linspace(4, 5, 100)

y1 = f1(x1)
y2 = f2(x2)

plt.plot(x1, y1)
plt.plot(x2, y2)

# part3 

x = np.linspace(1, 5, 100)

y = x

plt.plot(x, y)

# part4

x = np.linspace(1, 5, 100)

y = np.full_like(x, 1)

plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Digit 2')
plt.legend()
plt.grid(True)
plt.show()

############################################################

# for digit 9
# part1

def f1(x):
    return -5.0000 * 10**(-1) * x**3 + 3.0000 * x**2 - 4.5000 * x + 6.0000

def f2(x):
    return 5.0000 * 10**(-1) * x**3 - 6.0000 * x**2 + 2.2500 * 10**(1) * x - 2.1000 * 10**(1)

x1 = np.linspace(2, 3, 100)
x2 = np.linspace(3, 4, 100)

y1 = f1(x1)
y2 = f2(x2)

plt.plot(x1, y1)
plt.plot(x2, y2)

# part2
def f1(x):
    return 5.0000 * 10**(-1) * x**3 - 3.0000 * x**2 + 4.5000 * x + 4.0000

def f2(x):
    return -5.0000 * 10**(-1) * x**3 + 6.0000 * x**2 - 2.2500 * 10**(1) * x + 3.1000 * 10**(1)

x1 = np.linspace(2, 3, 100)
x2 = np.linspace(3, 4, 100)

y1 = f1(x1)
y2 = f2(x2)

plt.plot(x1, y1)
plt.plot(x2, y2)

# part2 

x = np.linspace(2, 4, 100)

y = 2 * x - 3

plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Digit 9')
plt.legend()
plt.grid(True)
plt.show()

