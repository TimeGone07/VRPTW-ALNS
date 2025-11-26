import sys
from route import Route
class Repair:
    
    def __init__(self, instance, solution):
        self.instance = instance
        self.solution = solution 
    
    def executeMultiGreedyInsertion(self, randomGen):
        sortByRules = randomGen.randint(1, 7)
        tempArray = []
        if sortByRules == 1:
            self.solution.notServed = sorted(self.solution.notServed, key=lambda node: node.demand, reverse=True)
        elif sortByRules == 2:
            self.solution.notServed = sorted(
                self.solution.notServed,
                key=lambda node: (node.x - self.instance.depot.x)**2 + (node.y - self.instance.depot.y)**2,
                reverse=True
            )
        elif sortByRules == 3:
            self.solution.notServed = sorted(
                self.solution.notServed,
                key=lambda node: (node.x - self.instance.depot.x)**2 + (node.y - self.instance.depot.y)**2,
                reverse=False
            )
        elif sortByRules == 4:
            self.solution.notServed = sorted(self.solution.notServed, key=lambda node: node.dueTime - node.readyTime, reverse=False)
        elif sortByRules == 5:
            self.solution.notServed = sorted(self.solution.notServed, key=lambda node: node.readyTime, reverse=False)
        elif sortByRules == 7:
            self.solution.notServed = sorted(self.solution.notServed, key=lambda node: node.dueTime, reverse=True)
        else:
            randomGen.shuffle(self.solution.notServed)

        tempArray = self.solution.notServed.copy()
        
        for cus in tempArray:
            # cus = self.solution.notServed[0]
            curMinIncrement = sys.maxsize
            curBestRoute = None
            curBestRouteIdx = None
            for idx, potentialRoute in enumerate(self.solution.routes):
                afterInsert, costIncrement = potentialRoute.greedyInsert(cus)
                if randomGen.random() < 0.99:
                    if afterInsert:
                        if costIncrement < curMinIncrement:
                            curMinIncrement = costIncrement
                            curBestRoute = afterInsert
                            curBestRouteIdx = idx

            if curBestRoute == None:
                # means cannot find a way to insert ... 
                nodeList = [self.instance.depot, cus, self.instance.depot]
                newRoute = Route(self.instance, nodeList, set(nodeList))
                self.solution.routes.append(newRoute)
                self.solution.distance += (self.instance.distMatrix[0][cus.id] + self.instance.distMatrix[cus.id][0])
            else:
                self.solution.routes[curBestRouteIdx] = Route(self.instance, curBestRoute, set(curBestRoute))
                self.solution.distance += curMinIncrement

            # print(cus in self.solution.notServed)
            self.solution.notServed.remove(cus)
            self.solution.served.append(cus)


    
    def executeGreedyInsertion(self, randomGen):

        while len(self.solution.notServed) > 0:
            
            cus = randomGen.choice(self.solution.notServed)
            # random select the customer ... 
            curMinIncrement = sys.maxsize
            curBestRoute = None 
            curBestRouteIdx = None
            
            for idx, potentialRoute in enumerate(self.solution.routes):
                afterInsert, costIncrement = potentialRoute.greedyInsert(cus)
                if randomGen.random() < 0.99:
                    if afterInsert:
                        if costIncrement < curMinIncrement:
                            curMinIncrement = costIncrement
                            curBestRoute = afterInsert
                            curBestRouteIdx = idx

            if curBestRoute == None:
                # means cannot find a way to insert ... 
                nodeList = [self.instance.depot, cus, self.instance.depot]
                newRoute = Route(self.instance, nodeList, set(nodeList))
                self.solution.routes.append(newRoute)
                self.solution.distance += (self.instance.distMatrix[0][cus.id] + self.instance.distMatrix[cus.id][0])
            else:
                self.solution.routes[curBestRouteIdx] = Route(self.instance, curBestRoute, set(curBestRoute))
                self.solution.distance += curMinIncrement

            self.solution.notServed.remove(cus)
            self.solution.served.append(cus)


# if __name__ == "__main__":