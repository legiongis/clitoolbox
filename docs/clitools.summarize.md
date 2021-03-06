## clitools.summarize

Contains a variety of functions that are used by the scripts associated
with the tools in the CLI Toolbox.  These functions use the xlrd and xlwt
modules to create a few different forms of MS Excel spreadsheet summaries
of landscape and their features.  The xlrd and xlwt modules were developed
by David Giffin <david@giffin.org>, and are freely distributable under a 
4-clause BSD-style license.

If the clitools package is moved to the user's native Python installation,
all of these functions will be available to any python scripting.  Use the
following syntax to import the function:

from clitools.summarize import <function_name>

To move the clitools package to the Python folder, find your Python
installation folder (e.g. C:\Python27), and then find the 
...\Lib\site-packages directory.  Perform the following actions:

1. Move this clitools folder and all of its contents into the site-packages
directory.
2. From within the clitools folder, move the xlrd and xlwt folders and
their contents into the site-packages folder.

### Functions

##### CREnterpriseMultipleXLS

``CREnterpriseMultipleXLS(map_document, input_code, output_dir)``

Using the tables available in the map document (only the CR
Catalog and CLI Feature table are necessary), creates a spreadsheet
with the progress of each feature in the landscape.

##### CREnterpriseSingleXLS

``CREnterpriseSingleXLS(map_document, input_code, output_dir)``

Using the tables available in the map document (only the CR
Catalog and CLI Feature table are necessary), creates a spreadsheet
with the progress of each feature in the landscape.

##### ChoosePercStyle

``ChoosePercStyle(value, low_style, mid_style, high_style)``

Chooses a cell format style based on the input value for the cell.
These styles are defined at the beginning of this module, and are not
included in this function.

##### GetFeatureDictFromTables

``GetFeatureDictFromTables(cli_number, cli_table, cr_link, cr_catalog)``

Uses the input CLI number to analyze the tables and return a
dictionary that contains a key per expected landscape feature
(and boundary) and values as lists of info for that feature.

key=CLI_ID, value=[RESNAME,CONTRIB_STATUS,LAND_CHAR,{RESOURCE_TYPE}]

RESOURCE_TYPE is appended to the list of values if that feature
has a spatial feature to represent it.

##### MakeMultipleLandscapeXLS

``MakeMultipleLandscapeXLS(input_geodatabase, out_directory, cli_list=[], exclude_arch=False)``

Creates a spreadsheet with one line per landscape that is included
in the cli_list.  The output spreadsheet will have percentages, totals,
and color coding for the GIS feature contents of each landscape.

##### MakeMultipleSummaryXLSHeaders

``MakeMultipleSummaryXLSHeaders(input_sheet_object, full=True)``

Takes an input xlwt sheet object and adjusts the columns and
writes headers to fit the single landscape summary template.

##### MakePercentage

``MakePercentage(partial_num, whole_num)``

Creates a formatted percentage based on two numbers.  It is used to
deal with 0 value inputs.

Param1: partial number
Param2: full number

The output is a string in this format: %xx.xx

##### MakeSingleLandscapeXLS

``MakeSingleLandscapeXLS(cli_num, input_geodatabase, out_directory, get_comments_from='', overwrite=False)``

This is a flexible spreadsheet creation function that will take an
input geodatabase and analyize it for features that are in the landscape
that is indicated by the cli number.  The spreadsheet will list all
expected features in the landscape.  Those that have geometry in the
geodatabase will have an indication of what type of geometry (pt/ln/py)
is being used to represent the feature.  Those features that have no
geometry will be highlighted.  At the end of the spreadsheet there are
percentages printed, and the location of the input geodatabase.

Comments from a previous spreadsheet summary of this landscape can be
incoporated into the output of this function, by placing the file path
in the get_comments_from parameter.

##### MakeSingleSummaryXLSHeaders

``MakeSingleSummaryXLSHeaders(input_sheet_object)``

Takes an input xlwt sheet object and adjusts the columns and
writes headers to fit the single landscape summary template.

##### MakeXLSFromSelectedRecords

``MakeXLSFromSelectedRecords(in_layer, out_path, out_name, fieldnames=[], open=False)``

This function will create a spreadsheet with some very basic formatting
(grey background and bold font in header row) from the attribute table
of the input layer.  If there is a selection in the layer, only the
selected features will be included.  The user has the option of defining
which fields will be included.

##### strftime

``strftime(...)``

strftime(format[, tuple]) -> string

Convert a time tuple to a string according to a format specification.
See the library reference manual for formatting codes. When the time tuple
is not present, current time as returned by localtime() is used.

