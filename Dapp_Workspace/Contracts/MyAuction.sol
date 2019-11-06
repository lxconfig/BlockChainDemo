pragma solidity ^0.5.0;


contract Auction{
    address payable seller;
    address payable buyer;
    uint public AuctionDuringTime;  // pai mai chi xu shi jian
    uint public MaxBidAmount;  // zui gao chu jia
    bool isFinished;
    uint reservedAmount;  // zui di chu jia 
    
    mapping(address => uint) public escrowAmount;  // ji lu bao zheng jin 
    
    constructor(address payable _seller, uint _AuctionDuringTime, uint _reservedAmount, uint _escrowAmout) public{
        seller = _seller;
        AuctionDuringTime = _AuctionDuringTime;
        reservedAmount = _reservedAmount;
        escrowAmount[seller] = _escrowAmout;  // ji lu mai jia de bao zheng jin 
        isFinished = false;
    }
    
    // function Submit() public payable{
    //     // mai jia ti jiao bao zheng jin
    //     require(!isFinished);
    //     require(now < AuctionDuringTime + now);
    //     escrowAmount[msg.sender] = msg.value;
    // }
    
    function Bid() public payable{
        require(!isFinished);
        require(now < AuctionDuringTime + now);
        require(msg.value >= reservedAmount);
        require(msg.value > MaxBidAmount);
        //require(escrowAmount[msg.sender] > 0); // mai jia shi fou ti jiao bao zheng jin
        if(MaxBidAmount > 0 && address(0) != buyer){
            buyer.transfer(MaxBidAmount);
        }
        buyer = msg.sender;
        MaxBidAmount = msg.value;
    }
    
    function EndAuction() public payable{
        require(now >= AuctionDuringTime);
        require(!isFinished);
        isFinished = true;
        seller.transfer(MaxBidAmount);
    }
    
    function GetBalance() public view returns(uint){
        return address(this).balance;
    }
}