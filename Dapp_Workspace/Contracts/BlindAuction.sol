pragma solidity >0.4.23 <0.7.0;

contract BlindAuction{
    struct Bid{
        bytes32 blindedBid;
        uint deposit;
    }
    
    address payable public beneficiary;
    uint public biddingEnd;
    uint public revealEnd;
    bool public ended;
    
    mapping(address => Bid[]) public bids;
    
    address public highestBidder;
    uint public highestBid;
    
    mapping(address => uint) pendingReturns;
    
    event AuctionEnded(address winner, uint highestBid);
    
    modifier onlyBefore(uint _time){
        require(now < _time);
        _;
    }
    
    modifier onlyAfter(uint _time){
        require(now > _time);
        _;
    }
    
    constructor(uint _biddingTime, uint _revealTime, address payable _beneficiary) public{
        beneficiary = _beneficiary;
        biddingEnd = now + _biddingTime;
        revealEnd = biddingEnd + _revealTime;
    }
    
    function bid(bytes32 _blindedBid) onlyBefore(biddingEnd) public payable{
        bids[msg.sender].push(Bid({blindedBid: _blindedBid, deposit: msg.value}));
    }
    
    function reveal(uint[] memory _values, bool[] memory _fake) onlyAfter(biddingEnd) onlyBefore(revealEnd) public{
        uint length = bids[msg.sender].length;
        require(_values.length == length);
        require(_fake.length == length);
        // require(_secret.length == length);
        
        uint refund;
        for(uint i=0; i<length; i++){
            Bid storage bid = bids[msg.sender][i];
            (uint value, bool fake) = (_values[i], _fake[i]);
            if(bid.blindedBid != keccak256(abi.encodePacked(value, fake))){
                continue;
            }
            refund += bid.deposit;
            if(!fake && bid.deposit >= value){
                if(placeBid(msg.sender, value))
                    refund -= value;
            }
            bid.blindedBid = bytes32(0);
        }
        msg.sender.transfer(refund);
    }
    
    function placeBid(address bidder, uint value) internal returns(bool success){
        if(value <= highestBid){
            return false;
        }
        if(highestBidder != address(0)){
            pendingReturns[highestBidder] += highestBid;
        }
        highestBid = value;
        highestBidder = bidder;
        return true;
    }
    
    function withdraw() public{
        uint amount = pendingReturns[msg.sender];
        if(amount > 0){
            pendingReturns[msg.sender] = 0;
            msg.sender.transfer(amount);
        }
    }
    
    function auctionEnd() onlyAfter(revealEnd) public{
        require(!ended);
        emit AuctionEnded(highestBidder, highestBid);
        ended = true;
        beneficiary.transfer(highestBid);
    }

}