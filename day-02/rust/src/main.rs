use std::fs;

fn check(line: &str) -> i32 {
    let nums: Vec<i32> = line
                            .split_whitespace()
                            .map(|x| x.parse::<i32>().unwrap())
                            .collect();
    
    let mut diff: Vec<i32> = Vec::new();
    let num_len = nums.len() - 1;
    let dist_range = 1..4;

    for i in 0..num_len {
        diff.push(nums[i] - nums[i + 1]);
    }
    let monotonic = diff.iter().all(|&x|x > 0) || diff.iter().all(|&x| x < 0); 
    let mut abs_diff = diff.iter().map(|x| x.abs());
    let dist = abs_diff.all(|x| dist_range.contains(&x));
    (monotonic && dist) as i32
}

fn main() {
    let contents = fs::read_to_string("../input.txt").expect("No file found");

    let res: i32 = contents.lines().map(check).sum();
    println!("{res}");
}
