from pydantic import BaseModel, EmailStr
from typing import Optional

# Step 1: Define the 'student' class, which is a Pydantic model
class Student(BaseModel):
    name: str = "Jit"  # Default value for name
    age: Optional[int] = None  # Optional field, it can be None
    email: EmailStr  # Field that must be a valid email

    # Adding an example method to display info
    def display_info(self):
        print(f"Student Info:\n Name: {self.name}\n Age: {self.age}\n Email: {self.email}")

# Step 2: Example of creating a student dictionary (This is how data might come from an API or a form)
student_data = {
    "name": "John Doe",  # Optional: can be omitted if using default
    "age": 21,  # Optional: can be omitted as well
    "email": "john.doe@example.com"  # This is a required field
}

# Step 3: Create an instance of the Student model by passing the dictionary
student_instance = Student(**student_data)

# Step 4: Display the student info using the method
student_instance.display_info()

# Step 5: Convert the Pydantic model instance to a dictionary
student_dict = student_instance.model_dump()
print("\nConverted to Dictionary:")
print(student_dict)

# Step 6: Convert the Pydantic model instance to a JSON string
student_json = student_instance.model_dump_json()
print("\nConverted to JSON:")
print(student_json)

# Step 7: Handling Validation (What happens if the data doesn't match the model?)
try:
    # Trying to create an invalid email
    invalid_student = Student(name="Invalid", age=22, email="invalid-email")
except ValueError as e:
    print("\nError during validation:", e)
