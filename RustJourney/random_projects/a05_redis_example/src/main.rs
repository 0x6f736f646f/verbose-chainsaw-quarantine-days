use redis::Commands;

fn main() -> redis::RedisResult<()> {
    let conn = redis::Client::open("redis://localhost:6379")?.get_connection()?;
    conn.set("aKey", "a string".to_string())?;
    conn.set("anotherKey", 4567)?;
    conn.set(45, 12345)?;

    println!(
        "{:?}, {:#?}, {:#?}, {:#?}.",
        conn.get("aKey")?,
        conn.get("anotherKey")?,
        conn.get(45)?,
        conn.exists(40)?
    );

    Ok(())
}