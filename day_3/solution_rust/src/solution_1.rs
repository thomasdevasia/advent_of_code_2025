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

fn find_largest_joltage(input_data: &Vec<String>, battery_size: i32) -> Result<Vec<i64>, &str> {
    let mut results: Vec<i64> = Vec::new();
    for line in input_data {
        let mut largest_loc: i32 = -1;
        let mut temp_result = String::new();
        let mut battery_len = battery_size;
        // print!("\nProcessing line: {} -> ", line);
        while battery_len > 0 {
            // print!("Battery Length: {} -> ", battery_len);
            let mut largest = 0;
            for i in largest_loc + 1..line.len() as i32 - battery_len + 1 {
                let current_char = line.chars().nth(i as usize).ok_or("Index out of bounds")?;
                let current_value = current_char
                    .to_string()
                    .parse::<i32>()
                    .map_err(|_| "Failed to parse integer")?;
                if largest < current_value {
                    largest = current_value;
                    largest_loc = i;
                }
            }
            battery_len -= 1;
            temp_result.push_str(&largest.to_string());
            // print!("{} \n", largest);
        }
        // print!("Temp Result: {} \n", temp_result);
        results.push(
            temp_result
                .parse::<i64>()
                .map_err(|_| "Failed to parse integer result")?,
        );
    }
    Ok(results)
}

fn sum_list(list_values: Vec<i64>) -> i64 {
    let mut total: i64 = 0;
    for value in list_values {
        total += value;
    }
    total
}

pub fn run(battery_size: i32) {
    // let file_path = "../input_test.txt";
    let file_path = "../input.txt";
    let input_data = match read_input(file_path) {
        Ok(data) => data,
        Err(e) => {
            eprintln!("Error reading input file: {}", e);
            return;
        }
    };
    // println!("Input Data: {:?}", input_data);

    let largest_joltages = match find_largest_joltage(&input_data, battery_size) {
        Ok(value) => value,
        Err(e) => {
            eprintln!("Error processing input data: {}", e);
            return;
        }
    };
    // println!("\nResult: {:?}", largest_joltages);

    let total = sum_list(largest_joltages);
    println!("Total Sum: {}", total);
}
