"""
File ini dibuat khusus untuk KEGIATAN TESTING.
Berisi kata kunci yang sering terdeteksi sebagai sensitive information.
TIDAK berisi secret asli.
"""

# Dummy variables for testing purpose only
PRIVATE_KEY = "PRIVATE KEY"
private_key_id = "private_key_id"
private_key = "private_key"
api_key = "api-key"
x_api_key = "x-api-key"

def print_test_keywords():
    print("Testing sensitive keyword detection:")
    print(PRIVATE_KEY)
    print(private_key_id)
    print(private_key)
    print(api_key)
    print(x_api_key)

if __name__ == "__main__":
    print_test_keywords()
