pragma solidity ^0.5.0;

contract test{
    uint taskEnd;  // ren wu jie shu shi jian.
    uint k;
    uint i=0;
    uint j=0;
    address payable public TaskPoster;  // ren wu fa qi ren de di zhi.
    struct  Task {
        string position;  // wei zhi xin xi.
        string content;   // ren wu nei rong.
    }
    Task[3] public task;
    mapping(address => Task) public taskPerformer;  // ren wu zhi xing ren.
    mapping(address => uint) Winner;  // huo de ren wu de ren.
    bool ended;
    mapping(address => uint) public Deposit;  // ren wu fa qi zhe de bao zheng jin.
    address payable[] public SubmitTaskInfo;  // wan cheng ren wu de ren.
    
    constructor(uint _taskTime, uint _k, address payable _TaskPoster) public payable {
        taskEnd = now + _taskTime;
        k = _k;
        TaskPoster = _TaskPoster;
        Deposit[TaskPoster] += msg.value;
    }
    
    function setTask(string memory _pos, string memory _con) public {
        // she zhe ren wu.
        require(i < k, "任务已全部设置!");
        Task memory _task = Task(_pos, _con);
        if (i < k) {
            task[i] = _task;
        }
        i++;
    }
    
    function getTask() public returns(uint) {
        // ling qu ren wu.
        require(now <= taskEnd, "任务时间已过!");
        require(j < k, "任务已全部被领取!");
        if (j < k) {
            taskPerformer[msg.sender] = task[j];
            Winner[msg.sender] = 1;
        }
        j++;
    }
    function SubmitTask(bool _isFinished) public {
        require(now <= taskEnd, "任务提交时间已过!");
        require(Winner[msg.sender] == 1, '您没有获得任务!');
        if (_isFinished) {
            SubmitTaskInfo.push(msg.sender);    
        }
    }
    
    function Bonus() public returns(string memory) {
        require(msg.sender == TaskPoster, "您无权分配奖励金!");
        uint Bonus_num = SubmitTaskInfo.length;  // zhen zheng neng huo de shang jin de ren shu.
        uint bonus = Deposit[TaskPoster] / Bonus_num;
        if (Bonus_num > 0) {
            for (uint n=0; n<Bonus_num; n++) {
                SubmitTaskInfo[n].transfer(bonus);
            }            
        } else {
            TaskPoster.transfer(Deposit[TaskPoster]);
        }
        Deposit[TaskPoster] = 0;
    }
}