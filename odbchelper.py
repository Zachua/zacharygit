def buildConnectionString(params):
	"""Build a connection string from a dictionary of parameters.

	Returns string."""
	return ";".join(["%s=%s" %(k,v) for k, v in params.items()])

if __name__== "__main__":   #using __ instead of _
	myParams = {"server":"mpilgrim", \
		    "database":"master", \
		    "uid":"sa1", \
		    "pwd":"secret" \
		    }
	print buildConnectionString(myParams)

#import odbchelper
#params = {"server":"mpilgrim","database":"master","uid":"sa", "pwd":"sercet"}
#print odbchelper.buildConnectionString(params)
