file_name = "input.xlsx"
sheet = "Table 1"
import pandas as pd
import csv

df = pd.read_excel(io=file_name, sheet_name=sheet, skiprows=1)
i = 0
with open('output_python.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    for index, row in df.iterrows():
        new_row = [str(row['Layer Number']), 
             str(row['Layer Soil Type']), 
             str(row['Depth to Bottom of Soil Layer (feet)']), 
             str(row['Total Unit Weight\n(2) (pcf)']), 
             str(row['Deformation Modulus (ksi)']), 
             str(row['Effective Friction Angle (degrees)']),
             str(row['Undrained Shear Strength or Rock Eff. Cohesion (ksf)']),
             str(row['Rock/Concrete Ultimate Bond Strength (ksf) (3)'])]
        print(new_row)
        if str(row['Boring Number']).startswith('B-'):
            b_row = [str(row['Boring Number'])]
            writer.writerow(b_row)
        writer.writerow(new_row)
        i+=1
        if i == 20:
            break
