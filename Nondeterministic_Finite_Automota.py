class NDFA:
    def __init__(self, K, sigma, delta, S, F):
        self.K = K #states (set)
        self.sigma = sigma #alphabet (set)
        self.delta = delta #transition function {set of (K, sigma -> K)}
        self.S = S #start state
        self.F = F #final states

    def __str__(self):
        return f"K = {self.K} \nsigma = {self.sigma} \ndelta = {self.delta} \nS = {self.S} \nF = {self.F} "



    def isAccepted(self):
        return self.current in self.F


    def computenondeterministic(self,string):
        statesToBeVisited = []
        visitedVisited = []
        statesToBeVisited.append((self.S,string))
        while(len(statesToBeVisited)!=0):

            tempString = statesToBeVisited[0][1]
            tempState = statesToBeVisited[0][0]
            visitedVisited.append((tempState,tempString))
            if(tempString=="" and tempState in self.F):
                return True
            statesToBeVisited.pop(0)
            for i in delta:
                if(tempState == i[0]):
                    if(i[1]=="e" and ((i[2],tempString)not in visitedVisited)):
                        statesToBeVisited.append((i[2],tempString))
                    elif(tempString==""):
                        continue
                    elif(i[1]==tempString[0]):
                        statesToBeVisited.append((i[2],tempString[1:]))
        if (tempString == "" and tempState in self.F):
            return True
        return False

#Some Examples

K = {"A","B","C"}
sigma = {"0", "1","e"}
delta = {("A","e","B"), ("B","e","A"), ("A","1","B"), ("B","0","C")}
S = "A"
F = {"C"}

sample1 = NDFA({"q1", "q2"}, {"a", "b"}, {("q1","a","q2"), ("q1","b","q2"), ("q2","a","q2"), ("q2","b","q2")}, "q1", {"q2"})
NDFAsample1 = NDFA(K, sigma, delta, S, F)


print(NDFAsample1.computenondeterministic("100100101010"))
