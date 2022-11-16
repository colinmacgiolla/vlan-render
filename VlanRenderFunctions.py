#!/bin/python

from itertools import groupby


class VlanRenderFunctions:

   def __init__(self):
      pass

   def _groupid(self,item):
      return item[0] - item[-1]

   def expand(self, vlan:str ):
      vlanSet = set()
      stripped_list = [entry.strip() for entry in vlan.split(',')]
      for entry in stripped_list:
         if '-' in entry:
            # expand
            vlan_range = entry.split('-')
            expanded = set( range( int(vlan_range[0]),int(vlan_range[1])+1) )
            vlanSet.update(expanded)

         else:
            vlanSet.add( int(entry) )

      return list(vlanSet)


   def compress(self, vlans: list(int)):

      if not len(vlans):
         return ''

      values = list()

      for _group_id, members in groupby(enumerate(vlans),key=_group_id):
         block = list(members)
         first, last = block[0][1],block[-1][1]

         if first == last:
            values.append(str(first))
         else:
            sep = ',' if len(members) == 2 else '-'
            values.append(f'{first}{sep}{last}')

         return ','.join(values)
