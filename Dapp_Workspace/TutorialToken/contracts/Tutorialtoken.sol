pragma solidity ^0.5.0;

import "../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20.sol";

contract Tutorialtoken is ERC20 {

  string public name = "TutorialToken";
  string public symbol = "TT";
  uint8 public decimals = 2;
  uint public INITIAL_SUPPLY = 12000;

  constructor() public {
    _mint(msg.sender, INITIAL_SUPPLY);
  }
}
