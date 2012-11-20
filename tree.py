"""
File: tree.py
Author: huxuan
E-mail: i(at)huxuan.org
Created: 2012-11-13
Last modified: 2012-11-14
Description:
    Assistant Class for Tree

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""

class Node(object):
    """Node in a tree

    Attributes:
        label: the label of the node
        scope: scope range in string represented tree
    """
    def __init__(self, label=""):
        """Init Node"""
        self.label = label
        self.scope = 0
