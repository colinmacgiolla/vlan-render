<a id="VlanRender"></a>

# VlanRender

<a id="VlanRender.VlanRender"></a>

## VlanRender Objects

```python
class VlanRender()
```

<a id="VlanRender.VlanRender.valid"></a>

#### valid

```python
def valid(vlan: int)
```

valid - Checks if a VLAN ID (int) is valid or not

**Arguments**:

- `vlan` - int
  

**Returns**:

  Bool
  True if VLAN ID is in the correct range, False if not

<a id="VlanRender.VlanRender.expand"></a>

#### expand

```python
def expand(vlan: str)
```

expand - Expand the string rendering of a VLAN list to be a list of ints

**Arguments**:

- `vlan` - string
  A string with the switch rendering of the VLANs for trunk ports e.g.
  "2-5,11,23,55-98"
  

**Returns**:

  list(int)
  A list of integers, being all the VLAN IDs

<a id="VlanRender.VlanRender.compress"></a>

#### compress

```python
def compress(vlans: list)
```

compress - take a list of ints, and convert it to a compressed (hypenated) string

**Arguments**:

- `vlan` - list(int)
  A list of integers, representing the VLANs to be converted to string
  

**Returns**:

  string:
  A string representing the VLANS, comma separated single elemends, with hyphenated ranges e.g.
  "1,2,3-5,20-55,57"

