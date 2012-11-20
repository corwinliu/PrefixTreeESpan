"""
File: main.py
Author: huxuan
E-mail: i(at)huxuan.org
Created: 2012-11-12
Last modified: 2012-11-14
Description:
    Implementation of PrefixTreeESpan
    A Frequent Subtree Mining Algorithm

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""

import os
import sys
import getopt
import datetime

from tree import Node
from project import Project

TREE_DB = []
MINSUP = 0
TREEDATA = 'in.in'
OUTPUT = 'test.out'

def init():
    """
    Global Initialization
    """

    # Check exist of output file, remove if exists
    if os.path.exists(OUTPUT):
        os.remove(OUTPUT)

def get_opt():
    """
    Handle the options
    """

    global MINSUP
    global TREEDATA
    global OUTPUT

    # Parse options and arguments
    optlist, args = getopt.getopt(sys.argv[1:], 'i:s:o:')

    # Deal with predefined options
    for opt, arg in optlist:
        if opt == '-i':
            TREEDATA = arg
        elif opt == '-s':
            MINSUP = int(arg)
        elif opt == '-o':
            OUTPUT = arg
        else:
            continue

    return 0

def output_pre_tree(pre_tree):
    """
    Append result to output file
    """
    output_file = file(OUTPUT, 'a+')
    print >> output_file, ' '.join(pre_tree)
    output_file.close()

def get_fre(pre_tree, n, pros_db):
    """
    PrefixTreeESpan Algorithm (Part 2)
    Get n+1 order frequent subtree according to
    prefix tree and projection database
    """

    # Count growth elements
    growth_elems_count = {}
    for pros in pros_db:
        tree = TREE_DB[pros.tid]
        # Traversal each project database
        for i in xrange(len(pros.scope_list)):
            for j in xrange(pros.offset_list[i], pros.scope_list[i]):
                if tree[j].label != '-1':
                    growth_elem = (tree[j].label, i + 1)
                    # Treat the count as set of tree id
                    if growth_elem not in growth_elems_count:
                        growth_elems_count[growth_elem] = set([])
                    growth_elems_count[growth_elem].add(pros.tid)

    # print '=' * 80
    # print "F%d Growth Elements Counts:" % (n + 1, )
    # for growth_elem in growth_elems_count:
    #     print growth_elem, len(growth_elems_count[growth_elem])

    # Get frequent growth elements via comparison with MINSUP
    fre_elems = set([ growth_elem
        for growth_elem in growth_elems_count
            if len(growth_elems_count[growth_elem]) >= MINSUP ])

    # print '=' * 80
    # print "F%d Frequent Elements:" % (n + 1, )
    # print fre_elems

    # Get projection database for each frequent growth elements
    for fre_elem in fre_elems:

        # print '=' * 80
        # print "F%d Frequent Element:" % (n + 1, )
        # print fre_elem

        # Generate new prefix tree
        pre_tree_new = pre_tree[:]
        pre_tree_new.insert(- fre_elem[1], fre_elem[0])
        pre_tree_new.insert(- fre_elem[1], '-1')
        # Output the result
        output_pre_tree(pre_tree_new)

        # Generate new projection database
        pros_db_new = []
        for i in xrange(len(pros_db)):
            pros = pros_db[i]
            tree = TREE_DB[pros.tid]
            for j in xrange(len(pros.offset_list)):
                for k in xrange(pros.offset_list[j], pros.scope_list[j]):
                    if tree[k].label == fre_elem[0]:
                        pros_new = Project(pros.tid)
                        if tree[k + 1].label != '-1':
                            pros_new.add(k + 1, tree[k].scope)
                        l = tree[k].scope + 1
                        while tree[l].label != "-1" and l < pros.scope_list[j]:
                            pros_new.add(l, tree[l].scope)
                            l = tree[l].scope + 1
                        pros_db_new.append(pros_new)

        # print '=' * 80
        # print 'F%d Projected Database:' % (n + 1, )
        # for pros in pros_db_new:
        #     print pros

        # Get next level frequent subtree
        get_fre(pre_tree_new, n + 1, pros_db_new)

    return 0

def prefixtreeespan():
    """
    PrefixTreeESpan algorithm (Part 1)
    Get first level frequent nodes and corresponding projection database
    """
    # Read date file, compute useful params
    growth_elems_count = {}
    tree_data = file(TREEDATA)
    for tree_string in tree_data.readlines():

        # Get label list
        tree_labels = tree_string.strip().split(' ')
        # print "Labels:", tree_labels

        # DFS to compute scope
        root = Node(tree_labels[0])
        stack = [(root, 0)]
        tree = [root]
        index = 1
        while stack:
            elem = Node(tree_labels[index])
            if elem.label == '-1':
                stack[-1][0].scope = index
                stack.pop()
            else:
                stack.append((elem, index))
            tree.append(elem)
            index += 1

        # Add tree in to global TREE_DB
        TREE_DB.append(tree)

        # print '=' * 80
        # print "F1 Elements:"
        # for elem in tree:
        #     print tree.index(elem), elem.label, elem.scope

        # Count all node as growth elements in set
        growth_elems = set([ (elem.label, 0)
            for elem in tree
                if elem.label != '-1' ])
        for growth_elem in growth_elems:
            if growth_elem not in growth_elems_count:
                growth_elems_count[growth_elem] = 0
            growth_elems_count[growth_elem] += 1

    # print '=' * 80
    # print "F1 Growth Elements Count:"
    # for growth_elem in growth_elems_count:
    # print growth_elem, growth_elems_count[growth_elem]

    # Get frequent one level nodes
    fre_elems = set([ growth_elem
        for growth_elem in growth_elems_count
            if growth_elems_count[growth_elem] >= MINSUP ])

    # print '=' * 80
    # print "F1 Frequent Elements:"
    # print fre_elems

    # Generate projection dateabase for each frequent node
    for fre_elem in fre_elems:

        # print '=' * 80
        # print "F1 Frequent Element:"
        # print fre_elem

        pre_tree = [fre_elem[0], '-1']
        output_pre_tree(pre_tree)

        pros_db = []
        for i in xrange(len(TREE_DB)):
            tree = TREE_DB[i]
            for j in xrange(len(tree)):
                if tree[j].label == fre_elem[0] and tree[j + 1].label != '-1':
                    pros = Project(i)
                    pros.add(j + 1, tree[j].scope)
                    pros_db.append(pros)

        # print '=' * 80
        # print 'F1 Projected Database:'
        # for pros in pros_db:
        #     print pros

        get_fre(pre_tree, 1, pros_db)

def main():
    """
    Main process
    """
    # Get Options for input/output file and minsup
    get_opt()

    # Some Initilization
    init()

    # Mark start time for calculating time consuming
    time_start = datetime.datetime.now()

    # Call prefixtreeespan algorithm
    prefixtreeespan()

    # Mark end time and calculate time consuming
    time_end = datetime.datetime.now()
    output_file = file(OUTPUT, 'a+')
    print >> output_file, "Time used: ", time_end - time_start
    output_file.close()

if __name__ == '__main__':
    main()
