from random import randint
from time import sleep

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter



# Setup a provider for our service
provider = TracerProvider(resource=Resource({"service.name": "secure-password-services-inc"}))


# Enable this processor if you want output to console
#processor = BatchSpanProcessor(ConsoleSpanExporter())
processor = BatchSpanProcessor(JaegerExporter(agent_host_name="localhost", agent_port=6831))

provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)


class UserDetails():

    def __init__(self):
        self.name = ""
        self.email = "hacker-for-hire@jail.com"
        self.location = "Federal Penitentiary"
        self.occupation = "Hacker"
        self.password = "GH^&%E%JHY*(YKLI&IUKJO(&&IIH&%Rjhu675rflfsadgf;dhng"


def save_details(details):

    with open("all-users.txt", 'w') as file:
        file.write(details.name)

    print("Details saved to super secure storage")


def super_secure_password_changing_service(username):

    with tracer.start_as_current_span("changePasswordRequest"):

        # Step One. Authenticate the user
        is_valid = authenticate_user(username)

        if is_valid:

            # Step 2. Fetch the users details from storage
            details = fetch_user_details(username)

            print(f"Welcome back [{username}]. We currently hold the following details for you:")
            print(f"Name {details.name}")
            print(f"Email {details.email}")
            print(f"Password {details.password}")
            print(f"Occupation {details.occupation}")
            print(f"Location {details.location}")

            print()
            print()

            # Step 3. Change the users password
            details.password = change_password(details)
            print(f"Your new security compliant password is [{details.password}]")

            # Step 4. Save the new details to storage
            save_details(details)

            print("Password changed and the internet is now a safer place ")


def authenticate_user(username):
    with tracer.start_as_current_span("authenticateUser"):
        print(f"Performing checks to verify your credentials [{username}]")
        sleep(randint(2, 5))
        print("After considerable thought I believe you must be you because no one on the internet lies")
        return True


def fetch_user_details(username):
    with tracer.start_as_current_span("fetchUserDetails") as span:
        # track the user the request was made for
        span.set_attribute("name", username)
        print("The database is really slow today. Please wait")
        sleep(randint(3, 6))
        user_details = UserDetails()
        user_details.name = username
        return user_details


def generate_uncrackable_password():
    with tracer.start_as_current_span("generateUncrackablePassword"):
        print()
        print("Generating uncrackable password, this is complex and will take time")
        sleep(randint(2, 5))

        return "password"


def change_password(details):
    with tracer.start_as_current_span("changePassword"):
        print(f"Your password [{details.password}] does not meet out security standards."
              f" Changing to something more secure")
        new_password = generate_uncrackable_password()

        return new_password



super_secure_password_changing_service("definitely not a hacker")
super_secure_password_changing_service("probably not a hacker")
super_secure_password_changing_service("occasionally a hacker")