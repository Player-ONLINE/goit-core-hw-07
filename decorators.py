def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Not enough arguments."
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    return inner