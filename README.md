# Enhancing Accessibility and Engagement Through Real-Time Data Integration

This project aims to integrate public transportation accessibility data with contact information of social entities in Abu Dhabi to create a comprehensive platform that enhances accessibility and community engagement.

## Features
- **Real-Time Data**: Provides up-to-date transportation routes, schedules, and accessibility features.
- **Social Entity Contacts**: Offers direct contact information for governmental social entities.
- **User-Friendly Interface**: Allows users to filter and search for specific transportation options and contact information.
- **Multi-Format Outputs**: Supports data export in XLSX, CSV, and PDF formats.

## Installation
1. Clone the repository:
   bash
   git clone https://github.com/your-repo/abu-dhabi-accessibility.git
   cd abu-dhabi-accessibility
   
2. Install dependencies:
   bash
   pip install pandas requests
   

## Usage
1. Run the Python script to load and process the data:
   bash
   python integrate_data.py
   
2. Use the `get_accessible_transport_options` function to filter data:
   python
   from integrate_data import get_accessible_transport_options
   region = 'Downtown'
   accessibility_needs = 'Wheelchair'
   options = get_accessible_transport_options(region, accessibility_needs)
   print(options)
   

## Contributing
We welcome contributions from the community. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License.
