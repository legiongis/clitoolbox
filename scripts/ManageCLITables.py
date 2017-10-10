# ---------------------------------------------------------------------------
# Title: UpdateCLITables.py
# Version: 1.0
# Created by Adam Cox
#   
# Description:  This is a shell script that only needs to pass the current map document
# 	 object to the function that is held in the clitools.management module. The
# 	 construction must be this way so that the management module is able to locate
# 	 the tables that will be updated.
# ---------------------------------------------------------------------------

import arcpy
import os
from clitools.enterprise import UpdateCLITables
from clitools.enterprise import ConvertFeatureXLSToGDBTable

method = arcpy.GetParameterAsText(0)

if method == "Update Local Tables From CR Enterprise Tables":
    try:
        mxd = arcpy.mapping.MapDocument("CURRENT")
    except:
        arcpy.AddError("You must run this from ArcMap, and you must use the"\
                   "CR Enterprise Access map document.")
    UpdateCLITables(mxd)
elif method == "Process Local Prepared Excel Workbook (.xls)":
    xls = arcpy.GetParameterAsText(1)
    ul = arcpy.GetParameter(2)
    retain = arcpy.GetParameter(3)
    ConvertFeatureXLSToGDBTable(xls,retain_copy=retain,update_local=ul)
