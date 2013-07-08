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
