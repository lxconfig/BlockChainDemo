pragma solidity ^0.5.0;

library SafeMath{
    function Mul(uint a, uint b) pure public returns(uint){
        uint c = a * b;
        assert(c/a == b);
        return c;
    }
    
    function Div(uint a, uint b) pure public returns(uint){
        uint c = a / b;
        assert(a == b*c + a%b);
        return c;
    }
    
    function Sub(uint a, uint b) pure public returns(uint){
        assert(a >= b);
        return a - b;
    }
    
    function Add(uint a, uint b) pure public returns(uint){
        uint c = a + b;
        assert(c >= a);
        return c;
    }
}

contract UsingLibrary{
    function test(uint a, uint b) pure public returns(uint, uint, uint, uint){
        uint add = SafeMath.Add(a, b);
        uint sub = SafeMath.Sub(a, b);
        uint mul = SafeMath.Mul(a, b);
        uint div = SafeMath.Div(a, b);
        return (add, sub, mul, div);
    }
    
    using SafeMath for uint;
    function UsingForTest(uint a, uint b) pure public returns(uint, uint, uint, uint){
        uint add = a.Add(b);
        uint sub = a.Sub(b);
        uint mul = a.Mul(b);
        uint div = a.Div(b);
        return (add, sub, mul, div);
    }
}

