from pathfinder.dijkstra import Dijkstra
from pathfinder.kruskal import Kruskal
from time import perf_counter_ns
def main():

    print("***  Testing Dijkstra's  ~~ ***")
    t1s = perf_counter_ns()
    dij = Dijkstra()
    dij.run()
    t1e = perf_counter_ns()
    print(f"Performance: Algorithm R+T: {(t1e-t1s)}nS.")
    print("***  ~~ Done!!  ~~ ***")
    print("***  Testing Kruskal's  ~~ ***")
    t3s = perf_counter_ns()
    krus = Kruskal(6)
    krus.add_edge(0, 1, 4)
    krus.add_edge(0, 2, 4)
    krus.add_edge(1, 2, 2)
    krus.add_edge(1, 0, 4)
    krus.add_edge(2, 0, 4)
    krus.add_edge(2, 1, 2)
    krus.add_edge(2, 3, 3)
    krus.add_edge(2, 5, 2)
    krus.add_edge(2, 4, 4)
    krus.add_edge(3, 2, 3)
    krus.add_edge(3, 4, 3)
    krus.add_edge(4, 2, 4)
    krus.add_edge(4, 3, 3)
    krus.add_edge(5, 2, 2)
    krus.add_edge(5, 4, 3)
    krus.run()
    t3e = perf_counter_ns()
    print(f"Performance: Algorithm R+T: {(t3e-t3s)}nS.")
    print("***  ~~ Done!!  ~~ ***")
    print(f"*** Total Perf: {t3e-t1s}nS ***")
    # print(dij.get_path(T))

