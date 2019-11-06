pragma solidity ^0.5.0;

contract FirstDapp{
    string name;
    uint8 age;
    event InfoChange(string name, uint8 age);
    
    function SetInfo(string memory _name, uint8 _age)  public{
        name = _name;
        age = _age;
        emit InfoChange(name, age);
    }
    
    function Get() view public returns(string memory, uint8){
        return(name, age);
    }
}

