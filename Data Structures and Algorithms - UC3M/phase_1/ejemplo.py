def _dfs(self,start,visited):
    visited[start] = True
    
    for adj in self._vertices[start]:
        if not visited[adj]:
            self._dfs(adj,visited)
    




def is_connected(self)->bool:
    visited = dict.fromkeys(self._vertices.keys(),False)
    start = list(self._vertices.keys()[0])
    
    self._dfs(start,visited)
    if any(i[1] == False for i in visited.items()):
            return False
    return True

def is_bridge(self,v1,v2):
    #excepciones
    
    if not v2 in self._vertices[v1]:
        return False
    if not v1 in self._vertices[v2]:
        return False
    
    self._vertices[v1].remove(v2)
    self._vertices[v2].remove(v1)
    
    result = self.is_connected()
    
    self._vertices[v1].append(v2)
    self._vertices[v2].append(v1)
    
    return not result