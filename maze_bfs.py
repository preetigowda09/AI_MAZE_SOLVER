


maze = [    
    ['S', '.', '.', '#', '.', '.', '.'],
    ['#', '.', '.', '#', '.', '#', '.'],
    ['.', '.', '#', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', 'G']
]
for row in maze:
    print(row);
start=None;
goal=None;
for i in range(len(maze)):
    for j in range(len(maze[i])):
                   if maze[i][j] =='S':     
                        start=(i,j)
                   if maze[i][j] == 'G':
                          goal=(i,j)
print("Start:", start)
print("Goal:", goal) 
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
print(get_neighbors((start)))
def bfs(start,goal):
      queue=[start]
      visited={start}
      parent={}
      while queue:
            current=queue.pop(0)
            if current == goal:
                  break
            for n in get_neighbors(current):
                  if n not in visited:
                        visited.add(n)
                        parent[n]=current
                        queue.append(n)
      path=[]  
      current=goal
      while current!=start:
           path.append(current) 
           current=parent[current]         
      path.append(start)
      path.reverse() 
      return path
path=bfs(start,goal)
print("Shortest Path:", path)