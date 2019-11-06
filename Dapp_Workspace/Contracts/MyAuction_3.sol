pragma solidity ^0.5.0;

import "./MappingLibrary.sol";

contract SimpleAuction{
    address payable public seller;
    uint auctionEnd;
    uint k;
    uint i = 0;
    
    address payable highestBidder;
    uint public highestBid;
    
    mapping(address => uint) public pendingReturns; // zhun bei tui hui de qian.
    bool ended;
    
    itMaps.itMapAddressUint im_myAddressUintMap;
    address payable [] WinnerKey;
    mapping(address => uint) public WinnerSet;
    mapping(address => uint) public LoserSet;
    
    
    constructor(uint _biddingTime, address payable _seller, uint _k) public payable{
        seller = _seller;
        auctionEnd = now +_biddingTime;
        k = _k;
        pendingReturns[seller] = msg.value;
    }
    
    function bid() public payable{
        require(now <= auctionEnd, "Auction already ended.");
        if (msg.value > highestBid && i < k) {
            highestBidder = msg.sender;
            highestBid = msg.value;
            WinnerSet[msg.sender] = msg.value;
            WinnerKey.push(highestBidder);
            ++i;
        } else {
            LoserSet[msg.sender] = msg.value;
        }
    }
    
    function refund() public returns(bool){
        // Loser call this function to refund their deposit.
        uint amount = LoserSet[msg.sender];
        if(amount > 0){
            LoserSet[msg.sender] = 0;
            if(!msg.sender.send(amount)){
                LoserSet[msg.sender] = amount;
                return false;
            }
        }
        return true;
    }
    
    function withdraw() public returns(bool){
        // Winner call this function to withdraw their deposit.
        uint amount = WinnerSet[msg.sender];
        if (amount > 0) {
            WinnerSet[msg.sender] = 0;
            if (!msg.sender.send(amount)) {
                WinnerSet[msg.sender] = amount;
                return false;
            }
        }
        return true;
    }
    
    function Bonus(bool isOver) public {
        require(msg.sender == seller);
        uint amount = pendingReturns[seller];
        uint bonus = amount / k;
        uint length = WinnerKey.length;
        if (isOver) {
            for(uint j=0; j<length; j++) {
                WinnerKey[j].transfer(bonus);
            }
        } else {
            seller.transfer(amount);
        }
        pendingReturns[seller] = 0;
    }
    
    function auctionEnded() public{
        require(msg.sender == seller, "you can't ended this auction.");
        require(now >= auctionEnd, "Auction not yet ended.");
        require(!ended, "auctionEnd has already been called.");
        ended = true;
    }
}