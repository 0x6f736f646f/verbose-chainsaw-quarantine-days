#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use] extern crate rocket_contrib;
#[macro_use] extern crate serde_derive;
#[macro_use] extern crate diesel;
extern crate r2d2;
extern crate r2d2_diesel;
extern crate rocket;

use rocket_contrib::json::{Json, JsonValue};
mod hero;
mod db;
mod schemas;
use hero::Hero;
use schemas::heroes;

use rocket::{get, routes, post, put, delete};


#[get("/<name>/<age>")]
fn hello(name: String, age: u8) -> String {
    format!("Hello, {} year old named {}!", age, name)
}

#[post("/", data = "<hero>")]
fn create(hero: Json<Hero>, connection: db::Connection) -> Json<Hero> {
    let insert = Hero { id: None, ..hero.into_inner() };
    Json(Hero::create(insert, &connection))
}

#[get("/")]
fn read(connection: db::Connection) -> Json<JsonValue> {
    Json(json!(Hero::read(&connection)))
}

#[put("/<id>", data = "<hero>")]
fn update(id: i32, hero: Json<Hero>, connection: db::Connection) -> Json<JsonValue> {
    let update = Hero { id: Some(id), ..hero.into_inner() };
    Json(json!({
        "success": Hero::update(id, update, &connection)
    }))
}

#[delete("/<id>")]
fn delete(id: i32, connection: db::Connection) -> Json<JsonValue> {
    Json(json!({
        "success": Hero::delete(id, &connection)
    }))
}


fn main(){
    rocket::ignite()
        .manage(db::connect())
        .mount("/hello", routes![hello])
        .mount("/hero", routes![create, update, delete])
        .mount("/heroes", routes![read])
        .launch()
    ;
}