if __name__ == "__main__":
    start = time.time()
    print(f"Start time: {start: .2f} seconds")

    passFile = open("MostCommonPWs", "r")

    for password in passFile:
        print(password.strip())

        # .strip() removes any whitespace or newline characters
        process = subprocess.run(["python3", "Login.pyc", "Adam", password.strip()], capture_output = True)

        if process.stdout.decode() != "Login failed: incorrect password. Try again please.\n":
            print(process.stdout.decode())
            print(f"Adam's password: ", password.strip())
            break

        end = time.time()
        print(f"End time: {end:.2f} seconds")

        passFile.close()
