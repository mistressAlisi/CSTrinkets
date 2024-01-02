#include<iostream>
#include<set>
#include<list>
#include<algorithm>
using namespace std;

struct Vertex {
   int dest;
   int cost;
};

class Graph {
    private:
        int size;
        list<Vertex> *aList;
      
   public:
        Graph() {
            size = 0;
        }

        Graph(int s) {
            size = s;
            aList = new list<Vertex>[size];
        }

        void addEdge(int source, int dest, int cost) {
            Vertex v;
            v.dest = dest;
            v.cost = cost;
            aList[source].push_back(v);
        }

        void shortestPath(Graph g, int *dist, int start) {
            int size = g.size;

            for(int u = 0; u<size; u++) {
                dist[u] = 9999;
            }

            dist[start] = 0;
            list<int> unvisited;

            for(int u = 0; u<size; u++) {
                unvisited.push_back(u);
            }

            while(!unvisited.empty()) {
                list<int> :: iterator i;
                i = min_element(unvisited.begin(), unvisited.end());
                int u = *i;
                unvisited.remove(u);
                list<Vertex> :: iterator it;

                for(it = g.aList[u].begin(); it != g.aList[u].end();it++) {
                    if((dist[u]+(it->cost)) < dist[it->dest]) {
                        dist[it->dest] = (dist[u]+(it->cost));
                    }
                }
            }
        }
};



main() {
   int size = 7;
   Graph g(size);
   int dist[size];
   int start = 0;

   g.addEdge(0, 1, 3);
   g.addEdge(0, 2, 6);
   g.addEdge(1, 0, 3);
   g.addEdge(1, 2, 2);
   g.addEdge(1, 3, 1);
   g.addEdge(2, 1, 6);
   g.addEdge(2, 1, 2);
   g.addEdge(2, 3, 1);
   g.addEdge(2, 4, 4);
   g.addEdge(2, 5, 2);
   g.addEdge(3, 1, 1);
   g.addEdge(3, 2, 1);
   g.addEdge(3, 4, 2);
   g.addEdge(3, 6, 4);
   g.addEdge(4, 2, 4);
   g.addEdge(4, 3, 2);
   g.addEdge(4, 5, 2);
   g.addEdge(4, 6, 1);
   g.addEdge(5, 2, 2);
   g.addEdge(5, 4, 2);
   g.addEdge(5, 6, 1);
   g.addEdge(6, 3, 4);
   g.addEdge(6, 4, 1);
   g.addEdge(6, 5, 1);

   g.shortestPath(g, dist, start);

   for(int i = 0; i<size; i++) {
        cout << start << " to " << i << ", Cost: " << dist[i] << endl;
   }
}