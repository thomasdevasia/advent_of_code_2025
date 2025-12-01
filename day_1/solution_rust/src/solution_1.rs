use std::fs::File;
use std::io::{BufRead, BufReader};

fn read_input(path: &str) -> Result<Vec<String>, std::io::Error> {
    let file = File::open(path)?;
    let reader = BufReader::new(file);
    let mut lines = Vec::new();
    for line in reader.lines() {
        lines.push(line?);
    }
    Ok(lines)
}

fn move_dial(input_lines: &[String], start_pos: usize) -> Result<usize, String> {
    let mut pos: i32 = start_pos as i32;
    print!("Starting position: {}\n", pos);
    let mut count_zeros: usize = 0;

    for item in input_lines {
        if item.len() < 2 {
            return Err(format!("Invalid input line: '{}'", item));
        }
        let dir = &item[0..1];
        let steps_str = item[1..].trim();
        let steps: i32 = match steps_str.parse::<i32>() {
            Ok(n) => n,
            Err(_) => {
                return Err(format!(
                    "Invalid number of steps '{}' in line '{}'",
                    steps_str, item
                ));
            }
        };
        print!("Direction: {}, Steps: {}\n", dir, steps);

        for _ in 0..steps {
            if dir == "R" {
                pos += 1;
            } else if dir == "L" {
                pos -= 1;
            } else {
                return Err(format!("Invalid direction '{}' in line '{}'", dir, item));
            }
            if pos > 99 {
                pos = 0;
            } else if pos < 0 {
                pos = 99;
            }
        }

        print!("New position: {}\n", pos);

        if pos == 0 {
            count_zeros += 1;
        }
    }

    return Ok(count_zeros);
}

pub fn run() {
    let file_path = "../input.txt";
    let start_pos = 50;
    let input_lines = match read_input(file_path) {
        Ok(lines) => {
            print!("Read {} lines from {}\n", lines.len(), file_path);
            print!("values: {:?}\n", lines);
            lines
        }
        Err(e) => {
            eprintln!("Error reading file: {}", e);
            return;
        }
    };
    match move_dial(&input_lines, start_pos) {
        Ok(result) => println!("Result: {}", result),
        Err(e) => eprintln!("Error processing input: {}", e),
    }
}
