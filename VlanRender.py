#!/bin/python

from itertools import groupby


class VlanRender():

   def __init__(self):
      pass

   def _group_id(self,item):
      '''
      The maths behind this is actually fairly simple when you write it out.
      If the sequence is sequential e.g. 1,2,3 then taking the index - value
      will always generate the same number e.g. the grouping

      So 1,2,3,4 when enumerated gives (0,1), (1,2), (2,3), (3,4)
      all of which will belong to group -1. But if we have a non-sequential number
      e.g. 6, that would tield (4,6) which has group -2
      '''
      return item[0] - item[1]

   def expand(self, vlan:str ):
      '''
      expand - Expand the string rendering of a VLAN list to be a list of ints

      Parameters:
         vlan: string
            A string with the switch rendering of the VLANs for trunk ports e.g.
            "2-5,11,23,55-98"

      Returns:
         list(int)
            A list of integers, being all the VLAN IDs
      '''
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


   def compress(self, vlans: list):
      '''
      comnpress - take a list of ints, and convert it to a compressed (hypenated) string

      Parameters:
         vlan: string
            A string with the switch rendering of the VLANs for trunk ports e.g.
            "2-5,11,23,55-98"

      Returns:
         list(int)
            A list of integers, being all the VLAN IDs
      '''
      if not len(vlans):
         return ''
      sorted_vlans = sorted(vlans)
      values = list()

      for group_id, members in groupby(enumerate(sorted_vlans),key=self._group_id):
         block = list(members)
         first, last = block[0][1],block[-1][1]

         if first == last:
            values.append(str(first))
         else:
            sep = ',' if len(block) == 2 else '-'
            values.append(f"{first}{sep}{last}")

      return ','.join(values)