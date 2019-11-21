pragma solidity ^0.5.0;


contract Voting {
  mapping(bytes32 => uint) public VotesReceived;
  bytes32[] public CandidateList;

  constructor(bytes32[] memory CandidateNames) public {
    CandidateList = CandidateNames;
  }

  function voteForCandidate(bytes32 Candidate) public {
    require(vaildCandidate(Candidate), "Invaild Candidate Name");
    VotesReceived[Candidate] += 1;
  }

  function vaildCandidate(bytes32 Candidate) public view returns(bool) {
    for (uint i = 0; i < CandidateList.length; i++) {
      if (CandidateList[i] == Candidate) {
        return true;
      }
    }
    return false;
  }
  
  function totalVotesFor(bytes32 Candidate) public view returns(uint) {
    require(vaildCandidate(Candidate), "Invaild Candidate Name");
    return VotesReceived[Candidate];
  }
}
