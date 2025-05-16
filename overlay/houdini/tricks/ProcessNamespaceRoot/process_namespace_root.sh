# cat process_namespace.sh
#!/bin/bash

# TARGET_CMD="sh -c while"
TARGET_CMD="/usr/bin/python3 /houdini/server.py"
PID=""

find_target_process() {
    echo "[1] Searching for process: $TARGET_CMD"
    PID=$(ps aux | grep "[/]usr/bin/python3" | awk '{print $2}' | head -n 1)
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

    # Attempt to attach strace in the background
    strace -p "$PID" -e trace=none -o /dev/null -t -qq &
    STRACE_PID=$!

    # Give it a moment to try attaching
    sleep 0.2

    # Check if strace is still running (i.e., it successfully attached)
    if kill -0 "$STRACE_PID" 2>/dev/null; then
        kill "$STRACE_PID"       # Cleanly stop strace
        wait "$STRACE_PID" 2>/dev/null
        echo "✅ Able to attach (via strace)"
    else
        echo "❌ Failed to attach debugger"
    fi
}

main() {
    find_target_process || exit 1
    echo
    send_signal
    echo
    attach_debugger
}

main
