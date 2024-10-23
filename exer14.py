from contextlib import contextmanager

class MockFunction:
    def __init__(self, return_value):
        self.return_value = return_value

    def __call__(self, *args, **kwargs):
        return self.return_value

@contextmanager
def patch(target, mock):
    # Split the target to get the module and function name
    module_name, func_name = target.rsplit('.', 1)
    module = __import__(module_name, fromlist=[func_name])

    # Save the original function
    original_func = getattr(module, func_name)

    # Replace the original function with the mock
    setattr(module, func_name, mock)

    try:
        yield
    finally:
        # Restore the original function
        setattr(module, func_name, original_func)

# Define the original function
def function_to_patch():
    return "Original Function"

# Test the patch
mock = MockFunction("Mocked!")

with patch('__main__.function_to_patch', mock):
    print(function_to_patch())  # Outputs: "Mocked!"

print(function_to_patch())  # Outputs: "Original Function"