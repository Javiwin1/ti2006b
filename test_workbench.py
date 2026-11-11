
import pandas as pd
import matplotlib.pyplot as plt

print("Workbench environment is ready!")

data = {
    "Name": ["Javier", "Alex", "Daniel"],
    "Score": [90, 85, 95]
}

df = pd.DataFrame(data)

print(df)
