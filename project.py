"""
File: project.py
Author: huxuan
E-mail: i(at)huxuan.org
Created: 2012-11-13
Last modified: 2012-11-14
Description:
    Assist Classes for Projection Database

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""

class Project(object):
    """Summary of Project

    Attributes:
        tid: id of the tree
        offset_list: offset for each subset of projection database
        scope_list: corresponding scope for each offset
    """
    def __init__(self, tid):
        """Init Project"""
        self.tid = tid
        self.offset_list = []
        self.scope_list = []

    def add(self, offset, scope):
        """Add a ProjectItem in to list"""
        self.offset_list.append(offset)
        self.scope_list.append(scope)

    def __str__(self):
        """Redefine the output of Project"""
        return "Tid: %d %s %s" % (self.tid, self.offset_list, self.scope_list)
