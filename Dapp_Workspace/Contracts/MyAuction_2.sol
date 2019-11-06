pragma solidity ^0.5.0;

import "./MappingLibrary.sol";

contract SimpleAuction{
    address payable public beneficiary;
    uint public auctionEnd;
    uint k;
    
    address public highestBidder;
    uint public highestBid;
    
    mapping(address => uint) public pendingReturns; // zhun bei tui hui de qian.
    bool ended;
    
    itMaps.itMapAddressUint im_myAddressUintMap;
    itMaps.itMapUintAddress im_myUintAddress;
    uint[] public BidSet;
    mapping(address => uint) public WinnerSet;
    mapping(address => uint) public LoserSet;
    
    event HighestBidIncreased(address bidder, uint amount);
    event AuctionEnded(address winner, uint amount);
    
    constructor(uint _biddingTime, address payable _beneficiary, uint _k) public payable{
        beneficiary = _beneficiary;
        auctionEnd = now +_biddingTime;
        k = _k;
        pendingReturns[beneficiary] = msg.value;
    }
    
    function bid() public payable{
        require(now <= auctionEnd, "Auction already ended.");
        itMaps.insert(im_myAddressUintMap, msg.sender, msg.value);
        itMaps.inserts(im_myUintAddress, msg.sender, msg.value);
    }
    
    function Prepare() public returns(uint[] memory){
        uint Mappinglength = itMaps.size(im_myAddressUintMap);
        for(uint i=0; i<Mappinglength; i++) {
            BidSet.push(itMaps.getValueByIndex(im_myAddressUintMap, i));
        }
        uint first = 0;
        uint last = BidSet.length - 1;
        return Sort(first, last);
    }
    
    function Sort(uint first, uint last) internal returns(uint[] memory){
        if(first >= last){
            return BidSet;
        }
        uint low = first;
        uint high = last;
        uint mid = BidSet[first];
        while(low < high){
            while(low < high && BidSet[high] >= mid){
                high -= 1;
            }
            BidSet[low] = BidSet[high];
            while(low < high && BidSet[low] < mid){
                low += 1;
            }
            BidSet[high] = BidSet[low];
        }
        BidSet[low] = mid;
        Sort(first, low-1);
        Sort(low+1, last);
        SetWinnerAndLoser();
        return BidSet;
    }
    
    function SetWinnerAndLoser() public returns(address key){
        uint length = itMaps.sizes(im_myUintAddress);
        for(uint i=length-1; i>=length-k; i--){
            key = itMaps.gets(im_myUintAddress, BidSet[i]);
            WinnerSet[key] = BidSet[i];
        }
        for(uint i=0; i<length-k; i++){
            key = itMaps.gets(im_myUintAddress, BidSet[i]);
            LoserSet[key] = BidSet[i];
        }
    }    
    
    function withdraw() public returns(bool){
        // Loser can withdraw their bids.
        if (0 != LoserSet[msg.sender]){
            uint amount = LoserSet[msg.sender];
            if(amount > 0){
                LoserSet[msg.sender] = 0;
                if(!msg.sender.send(amount)){
                    LoserSet[msg.sender] = amount;
                    return false;
                }
            }
            return true;
        } else {
            
        }
    }
    
    function auctionEnded() public{
        require(msg.sender == beneficiary, "you can't ended this auction.");
        require(now >= auctionEnd, "Auction not yet ended.");
        require(!ended, "auctionEnd has already been called.");
        ended = true;
        // emit AuctionEnded(highestBidder, highestBid);
        // beneficiary.transfer(highestBid);
        uint amount = pendingReturns[beneficiary];
        uint bonus = amount / k;
        uint length = itMaps.sizes(im_myUintAddress);
        for(uint i=length-1; i>=length-k; i--){
            address payable key = itMaps.gets(im_myUintAddress, BidSet[i]);
            key.transfer(WinnerSet[key]);
            key.transfer(bonus);
            WinnerSet[key] = 0;
        }        
    }
}