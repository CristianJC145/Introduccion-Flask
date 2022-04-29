import hashlib

message = hashlib.sha256()
message.update(b"CristianJamioy.145@991618")

print(message.hexdigest())