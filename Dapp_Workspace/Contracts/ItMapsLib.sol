pragma solidity ^0.5.0;

library itMaps {

    /* itMapAddressUint
         address =>  Uint
    */
    struct entryAddressUint {
        // Equal to the index of the key of this item in keys, plus 1.
        uint keyIndex;
        uint value;
    }
    
    struct itMapAddressUint {
        mapping(address => entryAddressUint) data;
        address[] keys;
    }    
    
    struct entryUintAddress{
        uint valueIndex;
        address key;
    }
    
    struct itMapUintAddress{
        mapping(uint => entryUintAddress) data;
        uint[] values;
    }

    function insert(itMapAddressUint storage self, address key, uint value) internal returns (bool replaced) {
        entryAddressUint storage e = self.data[key];
        e.value = value;
        if (e.keyIndex > 0) {
            return true;
        } else {
            e.keyIndex = ++self.keys.length;
            self.keys[e.keyIndex - 1] = key;
            return false;
        }
    }

    function remove(itMapAddressUint storage self, address key) internal  returns (bool success) {
        entryAddressUint storage e = self.data[key];
        if (e.keyIndex == 0)
            return false;

        if (e.keyIndex <= self.keys.length) {
            // Move an existing element into the vacated key slot.
            self.data[self.keys[self.keys.length - 1]].keyIndex = e.keyIndex;
            self.keys[e.keyIndex - 1] = self.keys[self.keys.length - 1];
            self.keys.length -= 1;
            delete self.data[key];
            return true;
        }
    }

    function destroy(itMapAddressUint storage self) internal  {
        for (uint i; i<self.keys.length; i++) {
          delete self.data[ self.keys[i]];
        }
        delete self.keys;
        return ;
    }

    function contains(itMapAddressUint storage self, address key) internal  returns (bool exists) {
        return self.data[key].keyIndex > 0;
    }

    function size(itMapAddressUint storage self) internal  returns (uint) {
        return self.keys.length;
    }

    function get(itMapAddressUint storage self, address key) internal  returns (uint) {
        return self.data[key].value;
    }

    function getKeyByIndex(itMapAddressUint storage self, uint idx) internal  returns (address) {
        return self.keys[idx];
    }

    function getValueByIndex(itMapAddressUint storage self, uint idx) internal  returns (uint) {
        return self.data[self.keys[idx]].value;
    }
    
    function sizes(itMapUintAddress storage selfs) internal returns(uint){
        return selfs.values.length;
    }
    
    function gets(itMapUintAddress storage selfs, uint value) internal  returns (address) {
        return selfs.data[value].key;
    }
    
    function inserts(itMapUintAddress storage selfs, address key, uint value) internal returns (bool replaced) {
        entryUintAddress storage h = selfs.data[value];
        h.key = key;
        if (h.valueIndex > 0){
            return true;
        }else{
            h.valueIndex = ++selfs.values.length;
            selfs.values[h.valueIndex - 1] = value;
            return false;
        }
    }    
    
}

contract Test{
    // using itMpas for itmap.itMapAddressUint;
    itMaps.itMapAddressUint im_myAddressUintMap;
    itMaps.itMapUintAddress im_myUintAddress;
    uint[] public test;
    mapping(address => uint) public WinnerSet;
    mapping(address => uint) public LoserSet;
    
    function Insert(address key, uint value) public returns(uint){
        itMaps.insert(im_myAddressUintMap, key, value);
        itMaps.inserts(im_myUintAddress, key, value);
        return itMaps.sizes(im_myUintAddress);
        // return im_myAddressUintMap.data[key].value;
    }
    
    function Prepare() public returns(uint[] memory){
        uint Mappinglength = itMaps.size(im_myAddressUintMap);
        for(uint i=0; i<Mappinglength; i++) {
            test.push(itMaps.getValueByIndex(im_myAddressUintMap, i));
        }
        uint first = 0;
        uint last = test.length - 1;
        return Sort(first, last);
    }
    
    function Sort(uint first, uint last) internal returns(uint[] memory){
        if(first >= last){
            return test;
        }
        uint low = first;
        uint high = last;
        uint mid = test[first];
        while(low < high){
            while(low < high && test[high] >= mid){
                high -= 1;
            }
            test[low] = test[high];
            while(low < high && test[low] < mid){
                low += 1;
            }
            test[high] = test[low];
        }
        test[low] = mid;
        Sort(first, low-1);
        Sort(low+1, last);
        GetKeys();
        return test;
    }
    
    function GetKeys() public returns(address key){
        uint k = 2;
        uint length = itMaps.sizes(im_myUintAddress);
        for(uint i=length-1; i>=length-k; i--){
            key = itMaps.gets(im_myUintAddress, test[i]);
            WinnerSet[key] = test[i];
        }
        for(uint i=0; i<length-k; i++){
            key = itMaps.gets(im_myUintAddress, test[i]);
            LoserSet[key] = test[i];
        }
    }
}