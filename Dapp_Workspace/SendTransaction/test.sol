pragma solidity >0.4.11;

contract test{
    uint public a;
    function seta(uint b) public returns(uint) {
        a = b;
        return a;
    }
}