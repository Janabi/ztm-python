is_magician = True
is_expert = False

# check if magician and expert: "You are a master magician"
if is_magician and is_expert:
    print("You are a master magician")
# check if magician but not expert: "At least you are getting there"
elif is_magician and not(is_expert):
    print("At least you are getting there")

# if you are not magician: "You need a magic power"
elif not(is_magician):
    print("You need a magic power")