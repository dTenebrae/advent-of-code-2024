use std::{collections::HashMap, fs};

fn main() {
    let contents = fs::read_to_string("../test.txt").expect("No file found");
    let vector: Vec<i32> = contents
                            .split_whitespace()
                            .map(|x| x.parse::<i32>().unwrap())
                            .collect();
    let mut cache: HashMap<i32, usize> = HashMap::new();
    for num in vector {
        *cache.entry(num).or_default() += 1;
    }
    
    for _ in 0..1 {
        let mut tmp_freq: HashMap<i32, usize> = HashMap::new();
        for (num, count) in cache.into_iter() {
            let (n1, n2) = process_stone(num);

                if n2 != -1 {
                    *tmp_freq.entry(n2).or_insert(count) += count;
                }
            *tmp_freq.entry(n1).or_insert(count) += count;
        }
        cache = tmp_freq.clone();
    }
    println!("{:?}", cache.into_values().sum::<usize>());
}

fn num_len(num: i32) -> u16 {
    1 + num.ilog10() as u16
}

fn num_split(num: i32) -> (i32, i32) {
    let n0 = num_len(num) as u32;
    let div: i32 = 10_i32.pow(n0 / 2);
    let left = (num / div) as i32;
    let right = (num % div) as i32;
    (left, right)
}

fn process_stone(stone: i32) -> (i32, i32) {
    return if stone == 0 {
        (1, -1)
    } else if num_len(stone) % 2 == 0 {
        num_split(stone)
    } else {
        (stone * 2024, -1)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_first_part() {
        let mut t_vec1: Vec<i32> = vec![125, 17];
        // let result = first_calc(&mut t_vec1, &mut t_vec2);
        // assert_eq!(result, 11);
    }
}