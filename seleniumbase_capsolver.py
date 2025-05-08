import random
import os
import time
from seleniumbase import SB


def wait_for_captcha_solution(sb, timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = sb.get_attribute("#g-recaptcha-response", "value")
            if response and len(response) > 0:
                return response
        except Exception:
            pass
        sb.sleep(1)
    raise TimeoutError("Timed out waiting for CAPTCHA to be solved by CapSolver.")


def main():
    extension_path = os.path.abspath('capsolver_extension')

    with SB(
        uc=True, 
        extension_dir=extension_path
    ) as sb:
        sb.open("https://www.google.com/recaptcha/api2/demo")

        print('\nWaiting for CAPTCHA!')
        print('--------------------')
        token = wait_for_captcha_solution(sb)
        print(token)

        sb.wait_for_element('#recaptcha-demo-submit', timeout=20)
        sb.click('#recaptcha-demo-submit')
        sb.sleep(3)

        sb.save_screenshot('seleniumbase_capsolver_google_recaptcha.png')


if __name__ == "__main__":
    main()
