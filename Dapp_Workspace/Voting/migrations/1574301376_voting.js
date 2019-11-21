var Voting = artifacts.require("./Voting.sol");
module.exports = function(_deployer) {
  // Use deployer to state migration tasks.
  _deployer.deploy(Voting, ["Rama", "Nick", "Jose"].map(x => web3.utils.asciiToHex(x)));  // 构造函数需要参数
};

