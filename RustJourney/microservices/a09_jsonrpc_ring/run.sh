#!/usr/bin/env bash
FIRST=127.0.0.1:4447
SECOND=127.0.0.1:5557
THIRD=127.0.0.1:6667

start_service() {
    RUST_LOG=jsonrpc_ring=trace RUST_BACKTRACE=1 ADDRESS=$1 NEXT=$2 target/debug/a09_jsonrpc_ring > $3 2>&1 &
}

cargo build

start_service ${FIRST} ${SECOND} first.log
start_service ${SECOND} ${THIRD} second.log
start_service ${THIRD} ${FIRST} third.log

sleep 3

curl -H "Content-Type: application/json" --data-binary '{"jsonrpc":"2.0","id":"curl","method":"start_roll_call","params":[]}' http://127.0.0.1:4447

sleep 5

pkill jsonrpc-ring

echo FIRST
cat first.log
echo SECOND
cat second.log
echo THIRD
cat third.log

rm first.log second.log third.log
