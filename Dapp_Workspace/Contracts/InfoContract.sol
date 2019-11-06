pragma solidity ^0.5.0;

contract InfoContract {
    
   string fName;
   uint age;
   
   function setInfo(string memory _fName, uint _age) public {
       fName = _fName;
       age = _age;
   }
   
   function getInfo() public view returns (string memory, uint) {
       return (fName, age);
   }   
}