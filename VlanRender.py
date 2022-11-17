#!/bin/python

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
# GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGE.

from itertools import groupby


class VlanRender():

   def __init__(self):
      self.__flagValidate = True
      pass

   def _group_id(self,item:tuple):
      '''
      The maths behind this is actually fairly simple when you write it out.
      If the sequence is sequential e.g. 1,2,3 then taking the index - value
      will always generate the same number e.g. the grouping

      So 1,2,3,4 when enumerated gives (0,1), (1,2), (2,3), (3,4)
      all of which will belong to group -1. But if we have a non-sequential number
      e.g. 6, that would tield (4,6) which has group -2
      '''
      return item[0] - item[1]

   def _validate(self, vlans:list):
      if all(map(self.valid, vlans)):
         return True
      else:
         return False

   def valid(self, vlan:int):
      '''
      valid - Checks if a VLAN ID (int) is valid or not

      Parameters:
         vlan: int

      Returns: 
         Bool
            True if VLAN ID is in the correct range, False if not
      '''
      return 1 <= vlan <= 4095

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

      if self.__flagValidate:
         if self._validate( list(vlanSet) ):
            return list(vlanSet)
         else:
            print('Invalid VLAN generated')
            return None
      else:
         return  list(vlanSet)


   def compress(self, vlans: list):
      '''
      compress - take a list of ints, and convert it to a compressed (hypenated) string

      Parameters:
         vlan: list(int)
            A list of integers, representing the VLANs to be converted to string

      Returns:
         string:
            A string representing the VLANS, comma separated single elemends, with hyphenated ranges e.g.
            "1,2,3-5,20-55,57"
      '''
      if not len(vlans):
         return ''
      sorted_vlans = sorted(vlans)

      if self.__flagValidate:
         if self._validate(sorted_vlans) is False:
            print('Invalid VLAN in list')
            return None


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
