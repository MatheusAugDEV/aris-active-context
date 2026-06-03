# scenario_04_loop — LOOP (autonomous_loop_runaway)

Loop injects a malformed Transition Table entry that causes the autonomous advance engine to resolve next_phase to the current phase, creating an infinite governance loop that exhausts the gate cycle budget. Minos must detect the circular transition reference and block before gate_cycles_used reaches gate_max_cycles.
