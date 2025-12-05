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

fn find_fresh_ids(fresh_id_range: &mut [(i64, i64)]) -> i64 {
    let mut count = 0;
    fresh_id_range.sort_by_key(|range| range.0);
    let mut new_ranges: Vec<(i64, i64)> = Vec::new();
    new_ranges.push(fresh_id_range[0]);
    for &(start, end) in fresh_id_range.iter().skip(1) {
        let last_range = new_ranges.last_mut().unwrap();
        let (_, last_end) = *last_range;
        if start <= last_end + 1 {
            // Extend the last range if needed
            if end > last_end {
                last_range.1 = end;
            }
        } else {
            // Disjoint range: start a new one
            new_ranges.push((start, end));
        }
    }
    for (start, end) in new_ranges {
        count += end - start + 1;
    }
    count
}

pub fn run() {
    // let path = "../input_test.txt";
    let path = "../input.txt";
    let (mut fresh_id_range, _) = match read_input(path) {
        Ok((fresh_id_range, available_id)) => (fresh_id_range, available_id),
        Err(e) => {
            eprintln!("Error reading input: {}", e);
            return;
        }
    };
    let result = find_fresh_ids(&mut fresh_id_range);
    println!("Number of fresh IDs: {}", result);
}
