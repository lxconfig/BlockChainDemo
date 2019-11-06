pragma solidity ^0.5.0;

// bool isActive = false;
// int8 x = 1;
// uint24 y = 9;

contract calc{
    function add(int x, int y) public pure returns(int z){
        z = x + y;
    }
    
    function divide(int x, int y) public pure returns(int z){
        z = x / y;
    }
    
    function leftshift(int x, uint y) public pure returns(int z){
        z = x << y;
    }
    
    function rightshift(int x, uint y) public pure returns(int z){
        z = x >> y;
    }
}

contract FixedSizeByteArray{
    function BytesArray() public pure returns(int y){
        bytes1 x = "A";
        y = x.length;
    }
}

contract HexadecimalLiteral{
    function hexLiteralBytes() public pure returns(bytes2, bytes1, bytes1){
        bytes2 a = hex"AABB";
        return (a, a[0], a[1]);  // 0xAABB, 0xAA, 0xBB
    }
}

contract Enums{
    enum ActionChoices{GoLeft, GoStraight, GoRight, SitStill}  // {0,1,2,3}
    ActionChoices choices;
    ActionChoices constant defaultChoices = ActionChoices.GoRight;
    
    function setGoStraight() public{
        choices = ActionChoices.SitStill;
    }
    
    function GetGoStraight() public view returns(ActionChoices){
        return choices;
    }
    
    function GetDefaultChoices() public pure returns(uint){
        return uint(defaultChoices);
    }
}

contract FunctionType{
    function select(bool useb, uint x) public pure returns(uint z){
        function (uint256) pure returns(uint256) f = a;
        if (useb) f = b;
        return f(x);
    }
    
    function otherSelect(uint x) public view returns(uint z){
        z = this.a(x);
    }
    
    function a(uint x) public pure returns(uint z){
        z = x * x;
    }
    
    function b(uint x) public pure returns(uint z){
        z = 2 * x;
    }
}

contract DataLocation{
    uint[] x = [1,2,3];  // storage
    function DataCopy(uint[] memory array) public  returns(uint[] memory){
        x = array;
        array[0] = 9;
        return x;
    }
    
    function DataCopy2() public returns(uint[] memory){
        uint[] storage y = x;
        y[0] = 99;
        return x;
    }
    
    function DataCopy3(uint a, uint b) public pure returns(uint, uint){
        a = 10;
        b = a;
        b = 20;
        return (a,b);
    }
}

contract Arrays{
    uint[] public u = [1,2,3];
    string s = "abcdefg";
    uint[] c;
    function arrays() public payable returns(uint[] memory){
        c = new uint[](7);
        c.length = 10;
        c[9] = 10;
        return c;
    }
    
    function StringLength() public view returns(uint){
        return bytes(s).length;
    }
    
    function h() public view returns(byte){
        return bytes(s)[1];
    }
}

contract MyStruct{
    struct MyType{
        uint a;
        bool b;
        mapping(address => uint) d;
        uint[3] e;
    }
    uint[3] f = [1,2,3];
    function StructType() public view returns(uint, bool, uint[3] memory){
        MyType memory c = MyType({a: 2, b: false, e: f});
        return (c.a, c.b, c.e);
    }
}

contract MappingExample{
    mapping(address => uint) public balances;
    
    function update(uint newBalance) public payable{
        balances[msg.sender] = newBalance;
    }
    
    function test() public view returns(address){
        return msg.sender;
    }
}

contract testBalance{
    function balanceOf() public view returns(uint){
        return address(this).balance;
    }
}

contract grandfather{
    uint public money = 100;
    function Study() pure external returns(string memory){
        return "学习";
    }
}

contract father is grandfather{
    uint public car = 2;
    function Sing() pure public returns(string memory){
        return "唱歌";
    }
}

contract son is father{
    function getMoney() public view returns(uint){
        return money;
    }
    function getStudy() public view returns(string memory){
        return this.Study();
    }
    function getCar() public view returns(uint){
        return car;
    }
    function getSing() public pure returns(string memory){
        return Sing();
    }
}

contract GetFunction{
    uint public num = 100;
    mapping(uint => string) public map;
    // function test() public view returns(uint){
    //     return this.num();
    // }
    function setMaping() public payable{
        map[1] = "lixuan";
    }
    function getMapping(uint key) public view returns(string memory){
        return this.map(key);
    }
}

contract FunctionOverloading{
    event FunctionOverloadingCalled(string);
    function test() public payable returns(string memory){
        emit FunctionOverloadingCalled("---FunctionOverloading.test()---");
    }
    function get() public pure returns(string memory){
        return "xxx";
    }
}

contract Base1 is FunctionOverloading{
    event Base1Called(string);
    function test() public payable returns(string memory){
        emit Base1Called("---Base1.test()---");
        super.test();
    }
}

contract Base2 is FunctionOverloading{
    event Bse2Called(string);
    function test() public payable returns(string memory){
        emit Bse2Called("---Base2.test()---");
        super.test();
    }
}

contract Final is Base1, Base2{  // Final-> Base2 -> Base1 -> FunctionOverloading
    event FinalCalled(string);
    function getTest() public payable returns(string memory){
        emit FinalCalled("---Final.test()");
        return test(); // Base2.test()
    }
}
