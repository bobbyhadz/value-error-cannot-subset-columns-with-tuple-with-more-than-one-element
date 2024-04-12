# Cannot subset columns with tuple with more than one element

import pandas as pd

df = pd.DataFrame({
    'ID': [1, 1, 1, 2, 2, 2],
    'Animal': ['Cat', 'Cat', 'Cat', 'Dog', 'Dog', 'Dog'],
    'Max Speed': [25, 35, 45, 55, 65, 75]
})


print(
    df.groupby('Animal')[['Animal', 'Max Speed']].apply(lambda x: x)
)