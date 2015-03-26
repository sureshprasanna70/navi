def main():
    print "hello"
    all_tables=[]
    zone_index=[]
    print "Total cars.(>2)"
    tot_cars=int(raw_input())
    if tot_cars > 2:
        dup_cars=tot_cars
        print "Coverage area"
        coverage_area=int(raw_input())
        while(tot_cars>0):
            all_tables.append(build_neighbor(dup_cars,tot_cars))
            tot_cars=tot_cars-1
        print all_tables
        zone_index=build_zone_index(all_tables,coverage_area)
        print 'Car {0} is the zone index'.format(chr(zone_index+97))
        print all_tables[zone_index]
    else:
        print "Enter greater than 2"
def build_neighbor(dup_cars,tot_cars):
    n_table=[0]*dup_cars
    no_cars=dup_cars-1
    count=0
    while(count<tot_cars):
        n_table[no_cars]=int(raw_input())
        count=count+1
        no_cars=no_cars-1
    print n_table
    return n_table
def build_zone_index(all_tables,coverage_area):
    print "zone index calc"
    count=[]
    for j in range(len(all_tables)):
        temp=0
        for i in range(len(all_tables[j])):
            row=j
            column=i
            if(all_tables[j][i]==0):
                print "Swap"
                row=i
                column=j
            if(all_tables[row][column]>=coverage_area):
                temp=temp+1
        count.append(temp)
    greatest=max(count)
    return count.index(greatest)
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxint
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start):
    print '''Dijkstra's shortest path'''
    start.set_distance(0)
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()
        for next in current.adjacent:
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

main()
