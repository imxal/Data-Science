import numpy as np
from scipy import linalg

# (x+y=30)
# (4x+9y=150)

testQuestionVariable = np.array([[1,1],[4,9]])
testQestionValue = np.array([30,150])

print(linalg.solve(testQuestionVariable,testQestionValue)
)

