import arcpy

arcpy.env.workspace = r"c:\temp\pgdb.sde\sgbde.sisdia.cobertura_solo_2018"


in_data = "../pgdb.sde"
out_file = "c:/output/XML/sgbde.sisdia.cobertura_solo_2018.xml"
export_option = "DATA" # DATA OU SCHEMA_ONLY
storage_type = "BINARY"
export_metadata = "METADATA"

# Execute ExportXMLWorkspaceDocument
arcpy.ExportXMLWorkspaceDocument_management(in_data, out_file, export_option, storage_type, export_metadata)