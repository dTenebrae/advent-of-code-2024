use std::fs;

fn check(nums: Vec<i32>) -> i32 {
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

fn convert_str(line: &str) -> Vec<i32> {
    let nums: Vec<i32> = line
                            .split_whitespace()
                            .map(|x| x.parse::<i32>().unwrap())
                            .collect();

    nums
}

fn main() {
    let contents = fs::read_to_string("../input.txt").expect("No file found");

    let first_res: i32 = contents
                            .lines()
                            .map(convert_str)
                            .map(check)
                            .sum();
    println!("{first_res}");

    let mut second_res: i32 = 0;
    for line in contents.lines() {
        let mut tmp_res = 0;
        let tmp_vec = convert_str(line);
        for i in 0..tmp_vec.len() {
            let mut inner_vec: Vec<i32> = tmp_vec.to_vec();
            inner_vec.remove(i);
            tmp_res = check(inner_vec);
            if tmp_res > 0 {
                break;
            }
        }
        second_res += tmp_res;
    }
    println!("{second_res}");
}
