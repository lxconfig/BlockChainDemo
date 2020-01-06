pragma solidity ^ 0.5.0;
// pragma experimental ABIEncoderV2;

import './Address2string.sol';

contract location_preserve {
    uint node_count;
    uint K;
    uint taskTime;
    address owner;
    // uint i = 0;  // she zhi ren wu shi yong dao de xun huan bian liang.
    uint j = 0;  // huo qu ren wu shi yong dao de xun huan bian liang.
    uint getTaskTime;  // ren wu bei qu zou de shi jian.
    
    struct Task {
        string position;
        string content;
        uint expire;
    }
    
    struct Node {
        uint is_delete;
        address node_addr;
    }
    
    Task[] public task;
    // Node[] public node;
    mapping(address => uint) public Deposit;
    mapping(address => Task) public taskExecutor;
    itMaps.itMapAddressString submitTaskInfo;
    address payable[] public AwardAccount;
    // mapping(address => string) public SubmitTaskAddr;
    
    function init(uint _nodeCount, uint _K, uint _taskTime) public payable {
        owner = msg.sender;
        node_count = _nodeCount;
        K = _K;
        taskTime = _taskTime;
        Deposit[msg.sender] += msg.value;
    }
    
    function SetTask(string memory _pos, string memory _con, uint _exp) public returns(bool) {
        require(msg.sender == owner);
        // require(i < K, 'The task has been set up!');
        // if (i < K) {
        //     Task memory task_info = Task(_pos, _con, _exp);
        //     task.push(task_info);
        //     i++;
        // }
        Task memory task_info = Task(_pos, _con, _exp);
        task.push(task_info);
        return true;
    }
    
    function GetTaskLength() public view returns(uint) {
        return task.length;
    }
    
    function GetTask(uint index) public payable returns(bool) {
        // require(j < K, 'There is no tasks!');
        // Node memory node_info = Node(0, msg.sender);
        // if (j < K) {
        //     taskExecutor[msg.sender] = task[j];
        //     position = taskExecutor[msg.sender].position;
        //     content = taskExecutor[msg.sender].content;
        //     expire = taskExecutor[msg.sender].expire;
        //     position = task[j].position;
        //     content = task[j].content;
        //     expire = task[j].expire;
        //     j++;
        // }

        // uint len = task.length;
        taskExecutor[msg.sender] = task[index];
        delete task[index];
        
        Deposit[msg.sender] += msg.value;
        getTaskTime = now;
        return true;
    }
    
    function ViewTask() public view returns(string memory position, string memory content, uint expire) {
        position = taskExecutor[msg.sender].position;
        content = taskExecutor[msg.sender].content;
        expire = taskExecutor[msg.sender].expire;
        return (position, content, expire);
    }
    
    function SubmitTask(string memory info) public returns(string memory) {
        // require((getTaskTime + taskExecutor[msg.sender].expire) > now, 'Task has expired!');
        if ((getTaskTime + taskExecutor[msg.sender].expire) > now) {
            itMaps.insert(submitTaskInfo, msg.sender, info);
            // SubmitTaskAddr[msg.sender] = info;
        } else {
            // fang hui ren wu.
            Task memory task_info = Task(taskExecutor[msg.sender].position, taskExecutor[msg.sender].content, taskExecutor[msg.sender].expire);
            task.push(task_info);
            return "renwu guoqi";
        }
        // itMaps.insert(submitTaskInfo, msg.sender, info);
        // return getTaskTime + taskExecutor[msg.sender].expire;
    }
    
    function ReturnTaskInfo(uint index) public view returns(string memory, string memory, uint, address addr, string memory val) {
        (addr,val) = itMaps.getKeyAndVal(submitTaskInfo, index);
        string memory position = taskExecutor[addr].position;
        string memory content = taskExecutor[addr].content;
        uint expire = taskExecutor[addr].expire;
        return (position, content, expire, addr, val);
    }
    
    function Prepare() internal {
         AwardAccount = itMaps.getKeys(submitTaskInfo);
    }
    
    function Bonus() public {
        require(msg.sender == owner, "You can't distribute rewards" );
        Prepare();
        uint num = AwardAccount.length;
        uint bonus = Deposit[msg.sender] / num;
        // uint jiangli = Deposit[msg.sender] - uint(0.002)*num;
        // uint s = (num * num + num) / 2;
        // uint d = jiangli / s;
        for (uint m=0; m<num; m++) {
            // uint bonus = uint(0.002) + (m+1) * d;
            AwardAccount[m].transfer(bonus);
        }
        Deposit[msg.sender] = 0;
    }
    
    function Withdraw() public returns(bool) {
        if (itMaps.contains(submitTaskInfo, msg.sender)) {
            msg.sender.transfer(Deposit[msg.sender]);
            Deposit[msg.sender] = 0;
            return true;
        } else {
            return false;
        }

    }
    

}