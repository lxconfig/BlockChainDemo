pragma solidity ^0.5.0;

contract test {
    struct Book {
        uint id;
        string book_name;
        string book_author;
        address payable book_owner;
        address payable reader;
        uint available_time;
        bool is_available;
        uint damage_Level;
        uint star;
        string comment;
    }
    
    mapping(address => mapping(string => Book))  resource;
    mapping(address => uint) public points;
    uint borrowedTime;
    
    
    modifier commonReturn(address payable owner, string memory book_name, uint damage_Level) {
        if (now - borrowedTime <= resource[owner][book_name].available_time) {
            uint damage = damage_Level - resource[owner][book_name].damage_Level;
            if (damage <= 0) {
                // unexpired and undamaged.
                points[resource[owner][book_name].reader] += 2;
                resource[owner][book_name].reader = address(0);
                resource[owner][book_name].is_available = true;
            } else {
                // unexpired but damaged.
                points[resource[owner][book_name].reader] -= 3;
                resource[owner][book_name].reader = address(0);
                resource[owner][book_name].is_available = true;
                resource[owner][book_name].damage_Level = damage_Level;
            }
        }
        _;
    }
    
    modifier expiredReturn(address payable owner, string memory book_name, uint damage_Level) {
        uint damage = damage_Level - resource[owner][book_name].damage_Level;
        if (damage <= 0) {
            // expired but undamaged.
            points[resource[owner][book_name].reader] -= 2;
            resource[owner][book_name].reader = address(0);
            resource[owner][book_name].is_available = true;
        } else {
            // expired and damaged.
            points[resource[owner][book_name].reader] -= 5;
            resource[owner][book_name].reader = address(0);
            resource[owner][book_name].is_available = true;
            resource[owner][book_name].damage_Level = damage_Level;
        }
        _;
    }
    
    function init_points() public returns(uint) {
        points[msg.sender] = 100;
        return points[msg.sender];
    }
    
    function init(string memory name, string memory author, address payable book_owner, uint time, bool is_available) public {
        Book storage book = resource[msg.sender][name];
        book.id += 1;
        book.book_name = name;
        book.book_author = author;
        book.book_owner = book_owner;
        book.reader = address(0);
        book.available_time = time;
        book.is_available = is_available;
        book.damage_Level = 0;
        points[msg.sender] += 2;
    }
    
    function getBook(string memory name) public view returns(string memory, address payable, address payable, bool) {
        string memory book_author = resource[msg.sender][name].book_author;
        address payable book_owner = resource[msg.sender][name].book_owner;
        address payable reader = resource[msg.sender][name].reader;
        bool is_available = resource[msg.sender][name].is_available;
        return (book_author, book_owner, reader, is_available);
    }
    
    function borrowedBook(address payable reader, string memory book_name) public returns(bool) {
        require(resource[msg.sender][book_name].is_available, 'Books cannot be borrowed!');
        resource[msg.sender][book_name].reader = reader;
        resource[msg.sender][book_name].is_available = false;
        borrowedTime = now;
        return true;
    }
    
    function returnBook(string memory book_name, uint damage) commonReturn(msg.sender, book_name, damage) expiredReturn(msg.sender, book_name, damage) public returns(string memory) {
        return "Return Book Successfully!";
    }
    
    function notReturnBook(string memory book_name) public returns(string memory) {
        points[resource[msg.sender][book_name].reader] -= 10;
        return "Processing Successfully!";
    }
    
    function CommentResource(address book_owner, string memory book_name, uint star, string memory comment) public returns(string memory) {
        resource[book_owner][book_name].star = star;
        resource[book_owner][book_name].comment = comment;
        return "Comment Successfully!";
    }
}