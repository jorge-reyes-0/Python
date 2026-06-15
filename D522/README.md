# D522 — Scripting and Programming Foundations (WGU)

This repository contains code and notes for the **D522 Scripting and Programming Foundations** course at Western Governors University. The examples focus on Python fundamentals with a network automation theme — most code uses routers, switches, IP addresses, and device inventories as real-world context.

---

## Repository Structure

```
D522/
├── 01_basics/
│   ├── if_else.py              — Conditional statements and ternary expressions
│   └── string_formatting.py    — .format(), index args, numbers, padding/alignment
│
├── 02_data_structures/
│   ├── lists.py                — Access, concatenate, copy, sort, list constructor
│   ├── dictionaries.py         — Create, read, nested dicts, update, add, remove, clear
│   ├── tuples.py               — Index, slice, unpack, tuple(), and modifying via list
│   └── sets.py                 — Union, add, update, remove, discard, clear, del
│
├── 03_control_flow/
│   ├── loops.py                — for, while, break, continue, while/else
│   └── functions.py            — Args, kwargs, *args, **kwargs, defaults, recursion
│
├── 04_file_io/
│   ├── file_basics.py          — open modes, built-in file functions, delete files/folders
│   ├── reading_files.py        — Read plain-text and CSV files
│   ├── writing_files.py        — Append, overwrite, and exclusive-create modes
│   └── ssh_automation.py       — SSH to network devices using Paramiko
│
├── 05_modules_packages_libraries/
│   ├── modules.py              — Import, rename, built-in modules, ipaddress module
│   ├── libraries.py            — Standard library, socket example
│   └── packages.py             — pip commands, netmiko ConnectHandler example
│
└── 06_reference/
    ├── debugging_and_errors.py — Syntax/runtime/semantic errors, debugging techniques
    └── comparing_files.py      — filecmp module for comparing configuration files
```

---

## Topics Covered

| Topic | File |
|---|---|
| If / else, ternary expressions | `01_basics/if_else.py` |
| String formatting | `01_basics/string_formatting.py` |
| Lists | `02_data_structures/lists.py` |
| Dictionaries | `02_data_structures/dictionaries.py` |
| Tuples | `02_data_structures/tuples.py` |
| Sets | `02_data_structures/sets.py` |
| For / while loops | `03_control_flow/loops.py` |
| Functions | `03_control_flow/functions.py` |
| File I/O basics | `04_file_io/file_basics.py` |
| Reading files and CSV | `04_file_io/reading_files.py` |
| Writing files | `04_file_io/writing_files.py` |
| SSH with Paramiko | `04_file_io/ssh_automation.py` |
| Modules | `05_modules_packages_libraries/modules.py` |
| Libraries (socket) | `05_modules_packages_libraries/libraries.py` |
| Packages (pip / netmiko) | `05_modules_packages_libraries/packages.py` |
| Debugging and error types | `06_reference/debugging_and_errors.py` |
| Comparing files | `06_reference/comparing_files.py` |

---

## Prerequisites

- Python 3.x
- Optional (only needed for SSH examples): `pip install paramiko`
- Optional (only needed for netmiko examples): `pip install netmiko`
