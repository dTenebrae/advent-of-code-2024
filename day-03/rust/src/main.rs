use std::fs;
use regex::Regex;

fn main() {
    let re = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();
    let contents = fs::read_to_string("../input.txt").expect("No file found");
    let vec_match: Vec<Vec<&str>> = re
                                    .captures_iter(&contents)
                                    .map(|c| c
                                                            .iter()
                                                            .map(|m| m
                                                                                        .unwrap()
                                                                                        .as_str())
                                                                                        .collect())
                                    .collect();
}
