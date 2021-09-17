use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        thread::sleep(Duration::from_millis(1));
        println!("（っ'-')╮  Hello from spawned thread");
    });


    handle.join().unwrap();

    println!("∠( ﾟдﾟ)／ Hello from Main Thread");
    println!("Main done")
}