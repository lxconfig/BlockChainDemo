var MyContract = artifacts.require("../contracts/InfoContract.sol");
module.exports = function(_deployer) {
    // Use deployer to state migration tasks.
    _deployer.deploy(MyContract);
};

// 删除事件版本