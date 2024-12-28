import sys

class Route:
    def __init__(self, instance, nodes, nodesSet):
        self.instance = instance
        self.nodes = nodes
        self.nodesSet = nodesSet
        self.feasible = self.isFeasible()
        if self.feasible:
            # 事先check路径是否可行
            self.distance = self.computeDistance()
        else:
            self.distance = sys.maxsize
            self.load = sys.maxsize

    
    def isFeasible(self):
        """check if the route is feasible
        """
        # check if the route starts and ends at depot 
        if self.nodes[0] != self.instance.depot or self.nodes[-1] != self.instance.depot:
            return False
        curTime = 0 # record current time
        curLoad = 0 # record load in vehicle 
        for i in range(1, len(self.nodes)):
            preID, postID = self.nodes[i - 1].id, self.nodes[i].id
            curTime += self.instance.distMatrix[preID][postID]
            if curTime > self.nodes[i].dueTime:
                print("Break time window!!")
                return False
            curTime = max(curTime, self.nodes[i].readyTime) + self.nodes[i].serviceTime
            curLoad += self.nodes[i].demand
            if curLoad > self.instance.capacity:
                # check capacity constraint
                print("Break capacity capacity!!")
                return False
        self.load = curLoad
        return True
    
    def computeDistance(self):
        """calculate total distance of the route

        Returns:
            _type_: _description_
        """
        totalDist = 0
        for i in range(1, len(self.nodes)):
            prevID, postID = self.nodes[i - 1].id, self.nodes[i].id
            totalDist += self.instance.distMatrix[prevID][postID]
        return totalDist
    
    def calculateServiceStartTime(self):
        """calculate the begin of service time for each customer of this route
        """
        curTime = 0
        for i in range(1, len(self.nodes) - 1):
            prevNode = self.nodes[i - 1]
            curNode = self.nodes[i]
            dist = self.instance.distMatrix[prevNode.id][curNode.id]
            curTime = max(curNode.readyTime, curTime + prevNode.serviceTime + dist)
            self.nodes[i].serviceStartTime = curTime
    
    def copy(self):
        nodesCopy = self.nodes.copy()
        nodesSetCopy = self.nodesSet.copy()
        return Route(self.instance, nodesCopy, nodesSetCopy)
    
