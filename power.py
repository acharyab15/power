file_name = "input.xlsx"
sheet = "Table 1"
import pandas as pd
import csv

df = pd.read_excel(io=file_name, sheet_name=sheet, skiprows=1)
rows = []
for index, row in df.iterrows():
    b_row = ""
    if str(row['Boring Number']).startswith('B-'):
        with open(row['Boring Number']+'.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            b_row = [str(row['Boring Number'])]
            writer.writerow(b_row)
            for r in rows:
                writer.writerow(r)
    new_row = [str(row['Layer Soil Type']), 
         str(row['Depth to Bottom of Soil Layer (feet)']), 
         str(row['Total Unit Weight\n(2) (pcf)']), 
         str(row['Deformation Modulus (ksi)']), 
         str(row['Effective Friction Angle (degrees)']),
         str(row['Undrained Shear Strength or Rock Eff. Cohesion (ksf)']),
         str(row['Rock/Concrete Ultimate Bond Strength (ksf) (3)'])]

    rows.append(new_row)
