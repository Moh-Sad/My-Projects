# ASTU View From The Main Gate

This repository contains a Python script that uses the `cs1graphics` library to render a graphical representation of the main gate view of Addis Ababa Science and Technology University (ASTU). The visualization includes a road, gate, ASTU logo, surrounding greenery, and fences.

## Features

- **Custom Background:**  
  A green background simulates a natural environment.

- **Road Representation:**  
  Includes a detailed two-part road structure leading to the main gate.

- **Gate Design:**  
  A layered elliptical gate structure with text ("ASTU") and decorative elements.

- **Logo:**  
  A custom ASTU logo constructed from multiple geometric shapes, scaled and positioned for visual appeal.

- **Greenery:**  
  Black polygons represent areas of greenery and landscaping.

- **Fence Design:**  
  Multi-layered fencing is added using paths, rectangles, and polygons for a realistic touch.

## Prerequisites

- Python 3.x
- `cs1graphics` library

## Installation

To install the required library:

```bash
pip install cs1graphics
```

Ensure Python and the library are installed before running the script.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Moh-Sad/My-Projects
   ```
2. Navigate to the folder:
   ```bash
   cd My-Projects/Python Graphics
   ```
3. Run the script:
   ```bash
   python Astu_Main_Gate.py
   ```

The script will open a graphical window rendering the ASTU main gate view.

## Code Overview

### Main Sections:

1. **Canvas Setup:**  
   Initializes the canvas with a dark green background and dimensions of `1300x800` pixels.

2. **Road Construction:**  
   Adds two black rectangles to represent the road.

3. **Gate Design:**  
   A series of ellipses and text objects form the gate, with layering for depth.

4. **Logo Design:**  
   The ASTU logo is composed of circles, ellipses, and a polygon.

5. **Greenery:**  
   Polygons are added to simulate greenery near the gate.

6. **Fence Design:**  
   Includes detailed path and rectangle objects to form a fence on both sides of the gate.

### Added Elements:

- **Greenery Expansion:**  
  Additional polygons (`green1`, `green2`, `green3`, `green4`) enhance the greenery around the gate.
- **Fence Expansion:**  
  Paths, rectangles, and polygons form an extended fence design.

## File Structure

- `Astu_Main_Gate.py`: Main Python script for rendering the ASTU gate view.
- `README.md`: Documentation for the repository.

## Preview

The script generates the following elements:
- Green background
- Black road
- ASTU gate with layered design
- ASTU logo
- Decorative greenery
- Detailed fences

## Contributing

Contributions are welcome! If you have ideas for improvements or additional features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
```
