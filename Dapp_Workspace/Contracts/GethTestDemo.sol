pragma solidity ^0.5.0;

contract Demo{
    uint x;
    function Set(uint y) public payable{
        x = y;
    }
    function Get() public view returns(uint){
        return x;
    }
}