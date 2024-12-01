use std::{collections::HashMap, fs};

fn first_calc(vec1: &mut Vec<i32>, vec2: &mut Vec<i32>) -> i32 {
    vec1.sort();
    vec2.sort();

    let result: i32 = vec1
        .iter()
        .zip(vec2.iter())
        .map(|(x, y)| i32::abs(x - y))
        .sum();
    result
}

fn second_calc(vec1: &mut Vec<i32>, vec2: &mut Vec<i32>) -> i32 {
    let freq = vec2.iter().copied().fold(HashMap::new(), |mut map, val| {
        map.entry(val).and_modify(|frq| *frq += 1).or_insert(1);
        map
    });

    let result: i32 = vec1
        .iter()
        .map(|num| match freq.get(num) {
            Some(n) => n * num,
            None => 0,
        })
        .sum();
    result
}
fn main() {
    let contents = fs::read_to_string("../input.txt").expect("No file found");
    let mut vec1: Vec<i32> = Vec::new();
    let mut vec2: Vec<i32> = Vec::new();

    for item in contents.lines() {
        let mut num_iter = item.split_whitespace();
        let num: i32 = num_iter.next().unwrap().parse().expect("Can't parse");
        vec1.push(num);
        let num: i32 = num_iter.next().unwrap().parse().expect("Can't parse");
        vec2.push(num);
    }

    let result = first_calc(&mut vec1, &mut vec2);
    println!("{}", result);

    let result = second_calc(&mut vec1, &mut vec2);
    println!("{}", result);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_first_part() {
        let mut t_vec1: Vec<i32> = vec![3, 4, 2, 1, 3, 3];
        let mut t_vec2: Vec<i32> = vec![4, 3, 5, 3, 9, 3];
        let result = first_calc(&mut t_vec1, &mut t_vec2);
        assert_eq!(result, 11);
    }
    #[test]
    fn test_second_part() {
        let mut t_vec1: Vec<i32> = vec![3, 4, 2, 1, 3, 3];
        let mut t_vec2: Vec<i32> = vec![4, 3, 5, 3, 9, 3];
        let result = second_calc(&mut t_vec1, &mut t_vec2);
        assert_eq!(result, 31);
    }
}
