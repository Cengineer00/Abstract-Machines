class DFS:
    def __init__(self, K, sigma, delta, S, F):
        self.K = K #states (set)
        self.sigma = sigma #alphabet (set)
        self.delta = delta #transition function {set of (K, sigma -> K)}
        self.S = S #start state
        self.F = F #final states

        self.current = S

        if(S in F):
            self.is_final = True
        else:
            self.is_final = False

    def __str__(self):
        return f"K = {self.K} \nsigma = {self.sigma} \ndelta = {self.delta} \nS = {self.S} \nF = {self.F} "

    def __invert__(self):
        K = self.K
        sigma = self.sigma
        delta = self.delta
        S = self.S
        F = set()
        for i in self.K:
            if i not in self.F:
                F.add(i)
        return DFS(K, sigma, delta, S, F)

    def transition(self, letter): #TODO dont forget to remove letter from the string
        for i in self.delta:
            if(letter == i[1] and self.current == i[0]):
                self.current = i[2]
                return


    def isAccepted(self):
        return self.current in self.F


    def compute(self, string): #TODO give letters one by one to the transition, if string is finished and isAccepted return True else return False
        for i in string:
            if (i not in self.sigma):
                print("string contains a letter which is not defined in the alphabet")
                return
            self.transition(i)
        if(self.isAccepted()):
            return True
        else:
            return False

    def step(self, string):
        x = 0
        for i in string:
            input()
            print(f"current state: {self.current} \t string: {string[x:]}")
            if (i not in self.sigma):
                print("string contains a letter which is not defined in the alphabet")
                return
            self.transition(i)
            x += 1
        input()
        print(f"current state: {self.current} \t string: e")
        if(self.isAccepted()):
            return "\nAccepted"
        else:
            return "\nNot Accepted"



#Some Examples

K = {"q0", "q1", "q2", "q3"}
sigma = {"a", "b"}
delta = {("q0","a","q0"), ("q0","b","q1"), ("q1","a","q0"), ("q1","b","q2"), ("q2","a","q0"), ("q2","b","q3"), ("q3","a","q3"), ("q3","b","q3")}
S = "q0"
F = {"q0", "q1", "q3"}

sample1 = DFS({"q1", "q2"}, {"a", "b"}, {("q1","a","q2"), ("q1","b","q2"), ("q2","a","q2"), ("q2","b","q2")}, "q1", {"q2"})
sample2 = DFS(K, sigma, delta, S, F)

print(sample1)

print(sample2.step("abaab"))

sample3 = ~sample2

print(sample3)
