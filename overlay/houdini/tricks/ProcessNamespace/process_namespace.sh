#!/bin/bash

TARGET_CMD="python3 /houdini/server.py"
PID=""

find_target_process() {
    echo "[1] Searching for process: $TARGET_CMD"
    PID=$(ps aux | grep '[p]ython3 /houdini/server.py' | awk '{print $2}' | head -n 1)
    if [[ -n "$PID" ]]; then
        echo "✅ Found: PID=$PID"
        return 0
    else
        echo "❌ Target process not found."
        return 1
    fi
}

send_signal() {
    echo "[2] Sending SIGCONT to PID $PID"
    if kill -CONT "$PID" 2>/dev/null; then
        echo "✅ Signal sent successfully"
    else
        echo "❌ Failed to send signal"
    fi
}

attach_debugger() {
    echo "[3] Attaching debugger with ptrace to PID $PID"
    if strace -p "$PID" -e trace=none -o /dev/null -t -qq &>/dev/null & sleep 1; then
        echo "✅ Able to attach (via strace)"
        pkill -P $$ strace 2>/dev/null
    else
        echo "❌ Failed to attach debugger"
    fi
}

read_memory() {
    echo "[4] Trying to read memory from /proc/$PID/mem"
    if dd if="/proc/$PID/mem" bs=1 count=4 skip=0 2>/dev/null | hexdump; then
        echo "✅ Read memory succeeded"
    else
        echo "❌ Failed to read memory"
    fi
}

main() {
    find_target_process || exit 1
    echo
    send_signal
    echo
    attach_debugger
    echo
    read_memory
}

main
