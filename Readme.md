# Image to ASCII Art Converter  

A Python script that converts an image into ASCII art and allows saving it as either a text file (.txt) or an image (.jpg).  

## Features  
- Converts an image to ASCII art.  
- Allows saving the output in JPG or TXT format.  
- Automatically resizes the image while maintaining proportions.  
- Uses an ASCII character palette to represent grayscale levels.  

## Prerequisites  
Make sure you have Python 3 installed along with the following dependencies:  

pip install pillow numpy  

## Usage  
1. Run the script:  
   python ascii_converter.py  
2. Follow the instructions:  
   - Enter the path to the image you want to convert.  
   - Choose the output format (JPG or TXT).  
   - Enter the name of the output file.  

## Example  
Input:  
[![image](https://github.com/user-attachments/assets/f7bd57d2-08bb-4b56-a482-2621c76f7159)
]  

Output (ASCII):  

@@@@@@####****++++====----::::..  
@@@@@###****++++====----::::..  
@@@@###****++++====----::::..  
@@@##***++++====----::::..  
@@##***+++====----::::..  

## Project Structure  
- ascii_converter.py   (Main script)  
- example.jpg          (Example image)  
- README.md            (Documentation)  

## Customization  
- Modify ASCII_CHARS in the script to change the character palette.  
- Adjust new_width=100 to change the ASCII art size.  

## Future Improvements  
- Support for color ASCII art.  
- GUI for easier use.  

## License  
This project is licensed under the MIT License.  
