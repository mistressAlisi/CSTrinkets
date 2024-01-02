#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ***
# kruskal.py: Kruskal's algorithm and test code in a class package.
# CSCI211: Pathfinder: Djikstra vs Kruskal program
# Last edited on 12/12/2023 by D. Mann
# ****
# Libraries we need:
import logging,sys,argparse,math
log = logging.getLogger(__name__)
class Kruskal():
    """ Define an empty graph:"""
    _vertices: 0
    _graph: []

    """ During init, define test code:"""
    def __init__(self,v):
        self._vertices = v
        self._graph = []

    """" Recursive Search:"""
    def _find(self,p,i):
        log.info(f"Find: p {p} i {i}")
        if p[i] == i: return i
        return self._find(p,p[i])

    """ Apply Union Algo"""
    def _union(self,p,r,x,y):
        xr = self._find(p,x)
        yr = self._find(p,y)
        if r[xr] < r[yr]:
            p[xr] = yr
        elif r[xr] > r[yr]:
            p[yr] = xr
        else:
            p[yr] = xr
            r[xr] += 1

    def add_edge(self,u,v,w):
        self._graph.append([u,v,w])

    """ Actually run Kruskal's:"""
    def run(self):
        """Initialise data variables and arrays:"""
        result = []
        i,e = 0,0
        self._graph = sorted(self._graph, key=lambda item: item[2])
        parent = []
        rank = []
        """Now, start populating the parents with vertices at initial rank, 0:"""
        for n in range(self._vertices):
            parent.append(n)
            rank.append(0)
        """ Divide and conquer:"""
        while e < self._vertices-1:
            log.info(f"Kruskal E<v: {self._graph}, I: {i}, {self._graph[i]}")
            u,v,w = self._graph[i]
            log.info(f"Kruskal E<v: E {e}, U {u}, V {v}, W {w}")
            i += 1
            x = self._find(parent,u)
            y = self._find(parent,v)
            if x != y:
                e += 1
                result.append([u,v,w])
                self._union(parent,rank,x,y)

        for u, v, weight in result:
            print(f"{chr(ord('a')+u)} - {chr(ord('a')+v)}: {weight}")


