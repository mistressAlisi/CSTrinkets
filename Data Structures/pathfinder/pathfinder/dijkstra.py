#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# dijkstra.py: Dijkstra's algorithm and test code in a class package.
# CSCI211: Pathfinder: Djikstra vs Kruskal program
# Last edited on 12/12/2023 by D. Mann
# ****
# Libraries we need:
import logging,sys,argparse,math
log = logging.getLogger(__name__)
class Dijkstra():
    """ Constructing the graph:"""
    """ Vertex matrix in 2D 7x7"""
    _vertices = [[0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]]

    """ Edge matrix in 2D 7x7"""
    _edges = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]

    """ Keep track of visited nodes in its own 2D array:"""
    _visited = [[0,0]]

    """ Initialise graph if overriding default, and v+d array:"""
    def __init__(self,vertices=False,edges=False):
        if vertices:
            self._vertices = vertices
        if edges:
            self._edges = edges
        self._visited = [[0, 0]]
        for i in range(self._get_vcount()-1):
            self._visited.append([0,sys.maxsize])



    """ Get Vertices count:"""
    def _get_vcount(self):
        log.info(f"VCount: {len(self._vertices[0])}")
        return len(self._vertices[0])

    """ Get next node to visit:"""
    def _to_visit(self):
        v = -10

        for i in range(self._get_vcount()):
            log.info(f"Visiting {i}...")
            if self._visited[i][0] == 0 and (v <0 or self._visited[i][1] <= self._visited[v][1]):
                v = i
        return v


    """ Actual Algo:"""
    def run(self):
        for v in range(self._get_vcount()):
            tv = self._to_visit()
            log.info(f"To Visit: {tv}")
            for n in range(self._get_vcount()):
                """ Update Distance:"""
                if self._vertices[tv][n] == 1 and self._visited[n][0] == 0:
                    """New Distance calc:"""
                    nd = self._visited[tv][1] + self._edges[tv][n]
                    log.info(f"ND: {nd} and [{n}][1] visited: {self._visited[n][1]}")
                    if self._visited[n][1] > nd:
                        self._visited[n][1] = nd
                self._visited[tv][0] = 1

        i = 0
        for d in self._visited:
            print(f"Distance of  Node  '{chr(ord('a')+i)}' from the source vertex: {d[1]}")
            i += 1
        #return self._visited


