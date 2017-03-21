from twisted.enterprise import adbapi


dbpool = adbapi.ConnectionPool("sqlite3", db="test.sqlite")

def getData(data):
    return dbpool.runQuery("INSERT INTO chat VALUES %s", (data))


def finish():
	dbpool.close()

def gotData():
	print "successfully"

d = getData("test")
d.addCallback(gotData)




