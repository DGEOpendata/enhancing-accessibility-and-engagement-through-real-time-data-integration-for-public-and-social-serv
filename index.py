python
import pandas as pd
import requests

# Load transportation data
transport_data_url = 'https://example.com/abu_dhabi_transport_data.xlsx'
transport_data = pd.read_excel(transport_data_url)

# Load social entities contact data
contact_data_url = 'https://example.com/abu_dhabi_social_contacts.xlsx'
contact_data = pd.read_excel(contact_data_url)

# Merge datasets on relevant fields
merged_data = pd.merge(transport_data, contact_data, how='left', on='Region')

# Example function to filter data based on user input
def get_accessible_transport_options(region, accessibility_needs):
    filtered_data = merged_data[(merged_data['Region'] == region) &
                                (merged_data['AccessibilityFeatures'].str.contains(accessibility_needs))]
    return filtered_data[['Route', 'Stop', 'AccessibilityFeatures', 'ContactName', 'ContactEmail']]

# Example usage
region = 'Downtown'
accessibility_needs = 'Wheelchair'
accessible_options = get_accessible_transport_options(region, accessibility_needs)

print(accessible_options)
