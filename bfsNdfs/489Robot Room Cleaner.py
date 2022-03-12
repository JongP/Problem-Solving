class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        #x,y,dx,dy=0,0,0,1
        visited=set()
        
        def turnBack(robot):
            robot.turnRight()
            robot.turnRight()
        
        def dfs(robot,x,y,dx,dy):
            visited.add((x,y))
            robot.clean()
            
            for _ in range(4):
                dx,dy= dy,-dx
                robot.turnRight()
                if (x+dx,y+dy) not in visited and robot.move():
                    dfs(robot,x+dx,y+dy,dx,dy)
                
            
            turnBack(robot)
            robot.move()
            turnBack(robot)
        
        
        dfs(robot,0,0,0,1)