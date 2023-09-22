import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
# %matplotlib inline

randomNumber = np.random.rand(10)

print(randomNumber)

style.use('ggplot')
plt.plot(randomNumber,'g',label='line one', linewidth=2)
plt.xlabel('Range')
plt.ylabel('Numbers')
plt.title('First Plot')

plt.legend()
plt.show()
