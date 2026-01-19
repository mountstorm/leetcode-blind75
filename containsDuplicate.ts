function containsDuplicate(nums: number[]): boolean {
    // Set holds unique items of the nums.
    // comparing set's size and original array's size helps to solve this problem
    return !(new Set(nums).size === nums.length);
};
