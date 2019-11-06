pragma solidity ^0.5.0;

contract QuickSort{
    uint[] public data = [9, 4, 8, 1, 2, 10];
    function sort(uint first, uint last) public returns(uint[] memory){
        if(first >= last){
            return data;
        }
        uint low = first;
        uint high = last;
        uint mid = data[first];
        while(low < high){
            while(low < high && data[high] >= mid){
                high -= 1;
            }
            data[low] = data[high];
            while(low < high && data[low] < mid){
                low += 1;
            }
            data[high] = data[low];
        }
        data[low] = mid;
        sort(first, low-1);
        sort(low+1, last);
        return data;
    }
}