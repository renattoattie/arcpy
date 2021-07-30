import arcpy, os, csv

arcpy.env.workspace = "../pgdb.sde"

datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

header = ['dataset', 'feature_class']
with open('C:\output\metadado\metadado.csv', 'w') as f:

    writer = csv.writer(f)

    writer.writerow(header)

    for ds in datasets:
        for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
            writer.writerow([ds, fc])   
