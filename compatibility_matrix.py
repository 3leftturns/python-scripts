#This script downloads the latest Trimble MGIS compatibility guide and current version documents when automated with windows task scheduler.
#This assures you will always have the latest versions.
#Licensed under a creative commons attribution-sharealike 3.0 unported license
#cc 2013 Andy Johnson

import urllib

#set the url to the compatibility matrix
urlSrc1= 'http://trl.trimble.com/docushare/dsweb/Get/Document-160913/'
urlSrc2= 'http://trl.trimble.com/docushare/dsweb/Get/Document-27877/'

#set the destination path
urlDes1= 'C:\Users\Andy\Dropbox\Monsen\Trimble\MGIS\Compatibility\Compatibility_Matrix.pdf'
urlDes2= 'C:\Users\Andy\Dropbox\Monsen\Trimble\MGIS\Compatibility\Current_Versions.pdf'

#download the files and inform the user
print "Downloading latest technical documents... Please wait."
urllib.urlretrieve(urlSrc1, urlDes1)
urllib.urlretrieve(urlSrc2, urlDes2)