# scenario_11_nemesis — NEMESIS (validator_bypass_injection)

Nemesis attempts to replace the validator script with a version that exits 0 before performing any authorization or state checks, effectively making CI always green. Minos must detect the script content mutation against the expected hash registered in the CI workflow and block the bypass attempt.
