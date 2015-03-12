def main():
    print "hello"
    all_tables=[]
    zone_index=[]
    print "Total cars"
    tot_cars=int(raw_input())
    print "Coverage area"
    coverage_area=int(raw_input())
    #while(tot_cars>0):
        #all_tables.append(build_neighbor())
        #tot_cars=tot_cars-1
    all_tables=[[-1, 2, 3], [1, -1, 3]]
    print all_tables
    zone_index=build_zone_index(all_tables,coverage_area)
    print 'Car {0} is the zone index'.format(zone_index)
def build_neighbor():
    n_table=[]
    x=raw_input()
    while(int(x)!=0):
        n_table.append(int(x))
        x=raw_input()
    print n_table
    return n_table
def build_zone_index(all_tables,coverage_area):
    print "zone index calc"
    count=[]
    for j in range(len(all_tables)):
        temp=0
        for i in range(len(all_tables[j])):
            if(all_tables[j][i]>=coverage_area):
                temp=temp+1
        count.append(temp)
    greatest=max(count)
    return count.index(greatest)
def proximity_measure():
main()
