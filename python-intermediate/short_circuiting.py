# Short circuiting
# when we use "or" operator little bet more efficient (whenever finds true, it will execute the following code immediately)
is_friend = True
is_user = True

if is_friend and is_user:
    print("best friends forever")

if is_friend or is_user:
    print("best friends forever")