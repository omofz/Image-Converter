"""
This program converts png format to ico format
"""
from PIL import Image


def to_ico(filepath: str, filename: str = "icon") -> bool:
    """converts jpg file to ico file

    Args:
        filepath (str): file path or relative path
        filename (str, optional): name of ico file to be saved.
            Defaults to "icon".

    Returns:
        bool: Saved or not
    """
    try:
        img = Image.open(filepath)
    except Exception as e:
        print("Error:", e)
        return False

    try:
        img.save(f"{filename}.ico", format="ICO")
    except Exception as e:
        print(e)
        return False
    else:
        print("Try again.")
    return True


def main():
    """
    main function for user prompt
    """
    print("This program converts a png image to ico format.")
    print("No quotation input such as '', \"\", ``")
    path = input("Enter the image path: ")
    name = input("Enter the name you want it to be saved as: ")

    task = to_ico(path, name)
    if task:
        print(f"Successfully created: {name}.ico")
    else:
        print("Unsuccessful attempt")


main()
