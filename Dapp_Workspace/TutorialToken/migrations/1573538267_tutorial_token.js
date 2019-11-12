var MyContract = artifacts.require('./contracts/Tutorialtoken.sol');
module.exports = function(_deployer) {
  // Use deployer to state migration tasks.
  _deployer.deploy(MyContract);
};
