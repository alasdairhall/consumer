import argparse
import subprocess
import os

def write_properties(username, service):
    with open(f"{os.path.expanduser('~')}/.gradle/dice_keystore.properties", "w+") as file:
        lines = [
            f"gpr.user={username}",
            f"gpr.service={service}"
        ]
        file.write("\n".join(lines))
        file.write("\n")


parser = argparse.ArgumentParser(description="Set credentials in Keychain and ~/.gradle/dice_keystore.properties")
parser.add_argument("username", help="Your GitHub username")
parser.add_argument("token", help="Your GitHub access token (must have `read:packages` scope)")
args = parser.parse_args()

username = args.username
token = args.token
service = "dice-github"

# add token to Keychain, so it can be read using `security find-generic-password ...` in `settings.gradle`
subprocess.run(["security", "add-generic-password", "-a", username, "-s", service, "-w", token, "-U"], capture_output=True)

# write properties to `~/.gradle/dice_keystore.properties`
write_properties(username, service)