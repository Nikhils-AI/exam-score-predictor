from joblib import load
import numpy as np

pipe = load('pipe.joblib')

sample = np.array([23, 1, 0.0, 1.2, 1.1, 0, 85.0,
                   8.0, 1, 6, 2, 1, 8, 1]).reshape(1, -1)


print(pipe.predict(sample))

