use std::fs::File;
use std::io::{BufRead, BufReader};

fn read_input(path: &str) -> Result<Vec<Vec<char>>, std::io::Error> {
    let file = File::open(path)?;
    let reader = BufReader::new(file);
    let mut input: Vec<Vec<char>> = Vec::new();
    for line in reader.lines() {
        let chars: Vec<char> = line?.chars().collect();
        input.push(chars);
    }
    Ok(input)
}

fn check_valid(input: &[Vec<char>], x: usize, y: usize) -> bool {
    let directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ];
    let mut count = 0;
    let len_x = input.len() as isize;
    let len_y = input[0].len() as isize;
    for direction in directions {
        let new_x = x as isize + direction.0;
        let new_y = y as isize + direction.1;
        if new_x < 0 || new_x >= len_x || new_y < 0 || new_y >= len_y {
            continue;
        }
        if input[new_x as usize][new_y as usize] != '.' {
            count += 1;
        }
        if count >= 4 {
            return false;
        }
    }
    true
}

fn solve(input: &mut [Vec<char>]) -> usize {
    let mut total = 0;
    let mut prev_total = 1;
    while total != prev_total {
        prev_total = total;
        // println!("Total: {}", total);
        for i in 0..input.len() {
            for j in 0..input[i].len() {
                if input[i][j] == '@' && check_valid(input, i, j) {
                    input[i][j] = '.';
                    total += 1;
                }
            }
        }
    }
    total
}

pub fn run() {
    let path = "../input.txt";
    // let path = "../input_test.txt";

    let mut input_data = match read_input(path) {
        Ok(data) => data,
        Err(e) => {
            eprintln!("Error reading input file: {}", e);
            return;
        }
    };
    // println!("Input Data: {:?}", input_data);

    let result = solve(&mut input_data);
    println!("Result: {}", result);
}
