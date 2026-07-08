#!/usr/bin/env python3
def secure_archive(name: str, action: str = "r", content: str = "") -> tuple:
    if action == "r":
        try:
            with open(name) as file:
                text = file.read()
                return (True, text)
        except Exception as e:
            return (False, str(e))
    if action == 'w':
        try:
            with open(name, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        except Exception as e:
            return (False, str(e))
    return (False, "Invalid action")


print("=== Cyber Archives Security ===")
print("Using 'secure_archive' to read from a nonexistent file:")
text = secure_archive("a.txt")
print(text)
print("Using 'secure_archive' to read from an inaccessible file:")
text = secure_archive("/etc/passwd")
print(text)
print("Using 'secure_archive' to read from a regular file:")
text = secure_archive("hello.txt")
print(text)
print("Using 'secure_archive' to write previous content to a new file:")
text = secure_archive("hello.txt", "w", "aaa")
print(text)
