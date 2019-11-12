pragma solidity ^0.5.0;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/InfoContract.sol";

contract TestInfoContract {
    InfoContract info = InfoContract(DeployedAddresses.InfoContract()); // 返回InfoContract合约的实例
    string name;
    uint age;

    function testInfo() public {
        info.setInfo("ABC", 10);
        (name, age) = info.getInfo();

        Assert.equal(name, "ABC", "设置名字出错");
        Assert.equal(age, 10, "设置年龄出错");
    }
}