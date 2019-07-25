#!/usr/bin/env python3
import uuid

howmany = int(input("How many uuids?"))
print("Generating UUIDs...")

for uuid in range(howmany):
    print(uuid.uuid4())
