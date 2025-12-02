use std::fs::File;
use std::io::Read;

fn read_input(path: &str) -> Result<String, std::io::Error> {
    let mut file = File::open(path)?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    Ok(content)
}

fn check_invalid(val: u64) -> bool {
    let temp = val.to_string();
    temp.len() % 2 == 0 && temp[..temp.len() / 2] == temp[temp.len() / 2..]
}

fn find_invalid(input_data: &Vec<&str>) -> Result<u64, String> {
    let mut sum: u64 = 0;
    for item in input_data {
        let parts: Vec<&str> = item.split('-').collect();
        if parts.len() != 2 {
            return Err("Invalid input format".to_string());
        }
        let min = match parts[0].parse::<u64>() {
            Ok(value) => value,
            Err(_) => return Err("Invalid input format".to_string()),
        };
        let max = match parts[1].parse::<u64>() {
            Ok(value) => value,
            Err(_) => return Err("Invalid input format".to_string()),
        };
        print!("Min: {}, Max: {}\n", min, max);
        for val in min..=max {
            if check_invalid(val) {
                sum += val;
            }
        }
    }
    Ok(sum)
}

pub fn run() {
    println!("Day 2 - Solution 1");
    // let input_path = "../input_test.txt";
    let input_path = "../input.txt";
    let file_string = match read_input(input_path) {
        Ok(data) => data.trim().replace('\n', ""),
        Err(e) => {
            eprintln!("Error reading input file: {}", e);
            return;
        }
    };
    let input_data: Vec<&str> = file_string.split(",").collect();
    println!("Input Data: {:?}", input_data);
    match find_invalid(&input_data) {
        Ok(result) => println!("Result: {}", result),
        Err(e) => eprintln!("Error processing input data: {}", e),
    }
}
