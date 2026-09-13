import heapq
maze=[
    ['S', '.', '.', '#', '.', '.', '.'],
    ['#', '.', '.', '#', '.', '#', '.'],
    ['.', '.', '#', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', 'G']
]
for row in maze:
    print(row)
start=None
goal=None
for i in range(len(maze)):
    for j in range(len(maze[0])):
       if maze[i][j]=='S':
        start=(i,j)
       if maze[i][j]=='G':
        goal=(i,j) 
print(start)  
print(goal)
def heruistic(position,goal):
    row,col=position
    goal_row,goal_col = goal
    return abs(row-goal_row) + abs(col-goal_col)
def get_neighbors(position):
    neighbors = []
    row, col = position
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    for  dr in directions:    
       new_row=row+dr[0]
       new_col=col+dr[1]
       if 0<=new_row<len(maze) and 0<=new_col<len(maze[0]) and maze[new_row][new_col] != '#':
             neighbors.append((new_row, new_col))
    return neighbors         
print(heruistic(start,goal))
def astar(start,goal):
   
   g_cost={start:0}
   parent={}
   f=g_cost[start]+heruistic(start,goal)
   open_list=[(f,start)]
   heapq.heapify(open_list)
   while open_list:
      current=heapq.heappop(open_list)[1]
      if current==goal:  
         break
      for neighbor in get_neighbors(current):
         new_g=g_cost[current]+1
         if neighbor not in g_cost or new_g<g_cost[neighbor]:
            g_cost[neighbor]=new_g
            h=heruistic(neighbor,goal)
            f=new_g+h
            heapq.heappush(open_list,(f,neighbor))
            parent[neighbor]=current
   path=[]    
   current=goal
   while current!=start:
      path.append(current)
      current=parent[current]
   path.append(start)   
   path.reverse()
   return path
path=astar(start,goal)  
print("Astar path: ",path)