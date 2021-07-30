'''
Esse código exportar cada camada do Geodatabase para ShapeFile
Isso servirá para fazer backup de camada por camada
'''

'''
teSte
v1.1.0 modif master
'''


import sys, arcpy, os, traceback, glob
from zipfile import ZipFile
from os.path import basename



# OBTENDO CONEXaO
arcpy.env.workspace = "../pgdb.sde"

# OBTENDO A LISTA DE FEATURE DATA SET
datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

for ds in datasets:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        # GERA SHAPE FILES
        arcpy.FeatureClassToShapefile_conversion([fc], 'C:\output\\tmp')
        
        # ZIPA ARQUIVOS
        with ZipFile('C:\output\\gerados\\'+ fc +'.zip', 'w', allowZip64=True) as zipObj:
            for folderName, subfolders, filenames in os.walk('C:\output\\tmp\\'):
                for filename in filenames:
                    filePath = os.path.join(folderName, filename)
                    zipObj.write(filePath, basename(filePath))
            zipObj.close()
        
        # REMOVE TEMPORARIOS
        files = glob.glob('C:\output\\tmp\\*')
        for f in files:
            os.remove(f)   