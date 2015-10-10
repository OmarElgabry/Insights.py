'''

@author: Omar
'''

from urllib.request import urlopen
import json

class WebData():
    """
    WebData class for reading data returned from URL, and parsing JSON to dictionary object.
    """
    
    def __init__(self, url):
        """
        Constructor method.
            URL is a string URL, to read data from it.
        """
        self._url   = url
        self._data  = None
        self._readData()
        
    def _readData(self):
        """
        reading data from a URL.
        Raises:
            ConnectionError: If received an error from server and data couldn't be fetched.
        """
        webUrl = urlopen(self._url)
        if (webUrl.getcode() == 200):
            self._data = webUrl.read().decode('utf-8')
        else:
            raise ConnectionError("Received an error {} from server, cannot retrieve results ".format(str(webUrl.getcode())))
        return self
    
    def getData(self):
        """
        Returns the resulting data as a string.
        """
        return self._data
    
    def parseJson(self):
        """
        Parses the string JSON data to a dictionary object, and returns it.
        """
        return json.loads(self.getData())
    
