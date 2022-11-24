from nucypher.crypto.keystore import Keystore
keystore = Keystore.generate(password="helloWorld1") # used to encrypt nucypher
# ˓→private keys
# # Public Key
# >>> keystore.id
# e76f101f35846f18d80bfda5c61e9ec2
# # The root directory containing the private keys
# >>> keystore.keystore_dir
# '/home/user/.local/share/nucypher/keystore'