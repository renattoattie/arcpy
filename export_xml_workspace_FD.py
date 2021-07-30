import arceditor


# Import arcpy module
import arcpy, os, datetime


# Local variables:


arcpy.env.workspace = "conexoes\pgdb_publicacao.sde"
datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []
classe_n_fd = arcpy.ListFeatureClasses()
base = "\\\\maq\\dados_14729$\\Banco_de_dados\\Backups\\pasta\\XML\\"
mydir = os.path.join(base, datetime.datetime.now().strftime('%Y/%m/%d'))

if not os.path.exists(mydir):
    os.makedirs(mydir)

mydir = mydir.replace("/", "\\")

for ds in datasets:
    fd = "Database Connections\\Connection to maq\\" + ds
    file = mydir + "\\" + ds + ".XML"
    arcpy.ExportXMLWorkspaceDocument_management(fd, file, "DATA", "BINARY", "METADATA")

for cs in classe_n_fd:
    fd = "Database Connections\\Connection to maq\\" + cs
    file = mydir + "\\" + cs + ".XML"
    arcpy.ExportXMLWorkspaceDocument_management(cs, file, "DATA", "BINARY", "METADATA")
