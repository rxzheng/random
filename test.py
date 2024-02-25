import instagram  # importing file

insta = instagram.Instagram()  # create an instance
res = insta.login(
    username="h2wb5nf4ivqqbamucqjovmentfxajm", password="Linux#1234"
)  # perform login. it will give out login info of user logged in like userID and auth.

## if above operation yields auth != True then you can read res in order to understand errors

if (
    not insta.isAuth
):  ## checks if above login was successful or not same as res.text['Authentication']
    print("Failed to login in")
else:
    print("login successful")
