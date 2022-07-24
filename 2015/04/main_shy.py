"""
2022-07-24 Author: Steffen Hytrek
"""

import hashlib
from datetime import datetime

INPUT_STRING = "bgvyzdsv"

def challenge_method(num_leading_zeros: int) -> None:
    start_ts = datetime.now()
    print(40*"-")
    print(f"{start_ts} Starting calculation for {num_leading_zeros}")
    number = 1
    secret_key = INPUT_STRING + str(number)

    md5_hash = hashlib.md5(secret_key.encode())
    md5_hash_str = md5_hash.hexdigest()

    print(f"Number: {number}; MD5: {md5_hash_str[0:10]}", end="\r")

    while md5_hash_str[0:num_leading_zeros] != (num_leading_zeros * "0"):
        number += 1
        secret_key = INPUT_STRING + str(number)
        md5_hash = hashlib.md5(secret_key.encode())
        md5_hash_str = md5_hash.hexdigest()
        if number % 100_000 == 0:
            print(
                f"{datetime.now() - start_ts} Number: {number}; MD5: {md5_hash_str[0:10]}")
        print(f"Number: {number}; MD5: {md5_hash_str[0:10]}", end="\r")

    print(f"{datetime.now() - start_ts} Lowest number creating a MD5 Hash with {num_leading_zeros} leading 0's:", end=" ")
    print(f"{number} (10 first spaces of MD5: {md5_hash_str[0:10]})")
    print(40*"-")


challenge_method(5)
challenge_method(6)
