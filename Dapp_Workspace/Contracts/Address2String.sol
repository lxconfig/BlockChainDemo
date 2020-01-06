pragma solidity ^0.5.0;
library itMaps {
    /* address => string */
    
    struct entryAddressString {
        uint keyIndex;
        string value;
    }
    
    struct itMapAddressString {
        mapping(address => entryAddressString) data;
        address payable[]  keys;
    }
    
    function insert(itMapAddressString storage self, address payable key, string memory value) internal returns (string memory replaced) {
        entryAddressString storage e = self.data[key];
        e.value = value;
        if (e.keyIndex > 0) {
            // return true;  // 替换某个地址的值
            return 'tihuan';
        } else {
            e.keyIndex = ++self.keys.length;
            self.keys[e.keyIndex - 1] = key;
            // return false;   // 插入新地址的值
            return 'xindezhi';
        }
    }
    
    function size(itMapAddressString storage self) internal view returns(uint) {
        return self.keys.length;
    }
    
    function getKeys(itMapAddressString storage self) internal view returns (address payable[] memory) {
        return self.keys;
    }
    
   function contains(itMapAddressString storage self, address key) internal view returns (bool exists) {
        return self.data[key].keyIndex > 0;
    }
    
    function getKeyAndVal(itMapAddressString storage self, uint index) internal view returns(address, string memory) {
        address addr = self.keys[index];
        string memory val = self.data[addr].value;
        return (addr, val);
    }
}