import bridgedef as bd
from bridgerecord import BridgeRecord as BRec
import csv
class BridgeMatchRec:
    def __init__(self,filename):
        self.games = []
        self.total = 0
        with open(filename) as file:
            dealcount=0
            reader = csv.reader(file)
            for row in reader:
                dealcount = dealcount+1
                if len(row) !=  4 :
                    print "ERROR: Line %d" % dealcount
                    self.done = False
                    return
                if not row[0] in bd.pos_dict or not row [1][1] in bd.suit_dict:
                    print "ERROR: Line %d" % dealcount
                    self.done = False
                    return
                if not checkint(row[1][0],7,1):
                    print "ERROR: Line %d" % dealcount
                    self.done = False
                    return
                if not checkint(row[2],2,0) or not checkint(row[3],7-int(row[1][0]),-6-int(row[1][0])):
                    print "ERROR: Line %d" % dealcount
                    self.done = False
                    return
                self.games.append(BRec(dealcount,row[0],row[1],int(row[2]),int(row[3])))
                self.total = self.total + self.games[-1].score
            self.done = True
    def printRecord(self):
        print "No. Deal.  Vul.  Decl.  Con. Penalty   Re.    N-S     E-W"
        print "---------------------------------------------------------"
        for rec in self.games:
            print rec
        print
    def printTotal(self):
        print " Total Score "
        print "-------------"
        print "N-S:   %+d"%self.total
        print "E-W:   %+d"%-self.total
def checkint(s,up,low):
    try :
        d = int(s)
        if d > up:
            return False
        if d < low :
            return False
        return True
    except ValueError:
        return False