import odbchelper
params = {"server":"mpilgrim","database":"master","uid":"sa", "pwd":"sercet"}
print odbchelper.buildConnectionString(params)

#import odbchelper
#params = {"server":"mpilgrim","database":"master","uid":"sa", "pwd":"sercet"}
#print odbchelper.buildConnectionString(params)
