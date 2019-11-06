pragma solidity ^0.5.0;

contract cat{
   function eat() public pure returns(string memory){
       return "cat eat fish";
   }

   function sleep() public pure returns(string memory){
        return "sleep";
   }
}

contract dog{
   function eat() public pure returns(string memory){
       return "dog miss you";
   }

   function swim() public pure returns(string memory){
        return "sleep";
   }
}

interface animalEat{
     function eat() external returns(string memory);
}

contract animal{
   function test(address _addr) public returns(string memory){
       animalEat generalEat = animalEat(_addr);
       return generalEat.eat();
   }
}