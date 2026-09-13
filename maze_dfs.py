maze = [
    ['S', '.', '#', '.', '.', '.', '.'],
    ['#', '.', '#', '.', '#', '#', '.'],
    ['.', '.', '.', '.', '#', '.', '.'],
    ['.', '#', '#', '.', '.', '.', '#'],
    ['.', '.', '.', '.', '#', '.', 'G']
]
for row in maze:
    print(row)
start=None
goal=None
for i in range(len(maze)):
    for j in range(len(maze[i])):
      if maze[i][j] == 'S':
         start=(i,j)
      if maze[i][j] == 'G':
         goal=(i,j)
print("Start:", start)
print("Goal:", goal)
def get_neighbors(start):
   neighbour=[]
   rol,col=start
   directions=[(-1,0),(1,0),(0,-1),(0,1)]
   for dr in directions:
        new_row=rol+dr[0]
        new_col=col+dr[1]
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#':
            neighbour.append((new_row, new_col))
   return neighbour
def dfs(start,goal):
    stack=[start]
    visited={start}
    parent={}

    while stack:
        current=stack.pop()
        if current==goal:
            break
        for n in get_neighbors(current):
            if n not in visited:
                visited.add(n)
                parent[n]=current
                stack.append(n)
    path=[]
    current=goal
    while current!=start:
        path.append(current)
        current=parent[current]
    path.append(start) 
    path.reverse()  
    return path
path=dfs(start,goal)
print("DFS Path:",path)