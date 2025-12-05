use std::fs::File;
use std::io::{BufRead, BufReader};

type Pair = (i64, i64);
type PairList = Vec<Pair>;
type ValueList = Vec<i64>;
type IoResult<T> = Result<T, std::io::Error>;

fn read_input(file_path: &str) -> IoResult<(PairList, ValueList)> {
    let file = File::open(file_path)?;
    let reader = BufReader::new(file);
    let mut fresh_id_range: Vec<(i64, i64)> = Vec::new();
    let mut available_id: Vec<i64> = Vec::new();
    let mut flag = false;
    for line in reader.lines() {
        let temp = line?.trim().to_string();
        if temp.is_empty() {
            flag = true;
            continue;
        }
        if !flag {
            fresh_id_range.push((
                temp.split('-').next().unwrap().parse::<i64>().unwrap(),
                temp.split('-').nth(1).unwrap().parse::<i64>().unwrap(),
            ));
        } else {
            available_id.push(temp.parse::<i64>().unwrap());
        }
    }
    Ok((fresh_id_range, available_id))
}

fn check_in_range(id: i64, range: &Vec<(i64, i64)>) -> bool {
    for r in range {
        if id >= r.0 && id <= r.1 {
            return true;
        }
    }
    false
}

fn find_fresh_ids(fresh_id_range: &Vec<(i64, i64)>, available_id: &Vec<i64>) -> i64 {
    let mut count = 0;
    for id in available_id {
        // println!("Checking ID: {}", id);
        if !check_in_range(*id, fresh_id_range) {
            count += 1;
        }
    }
    count
}

pub fn run() {
    // let path = "../input_test.txt";
    let path = "../input.txt";
    let (fresh_id_range, available_id) = match read_input(path) {
        Ok((fresh_id_range, available_id)) => (fresh_id_range, available_id),
        Err(e) => {
            eprintln!("Error reading input: {}", e);
            return;
        }
    };
    let result = find_fresh_ids(&fresh_id_range, &available_id);
    println!("Number of fresh IDs: {}", result);
}
