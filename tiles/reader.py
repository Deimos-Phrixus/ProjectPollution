import pandas as pd

class Reader():
    """
    Initialises reader by setting data (pandas table representing the excel sheet)

    @param sheet_name : Sheet name to read for data
    """
    def __init__(self, sheet_name):
        self.data = pd.read_excel("pollution-data.xlsx", sheet_name=sheet_name)
    
    """
    Returns a json (dictionary) containing the data for tiles

    @return A dictionary contianing tile's data (name, percentage, image_url, clickable)
    """
    def get_tiles_data(self):
        records = []
        for each_type in self.data['Name']:
            record = {}
            record['name'] = each_type
            record['percentage'] = list(self.data[self.data['Name'] == each_type]['Percentage'])[0]
            record['image_url'] = list(self.data[self.data['Name'] == each_type]['Image'])[0]
            try:
                pd.read_excel("pollution-data.xlsx", sheet_name=each_type)
                record['clickable'] = True
            except:
                record['clickable'] = False
            records.append(record)
        records = sorted(records, key=lambda x: -x['percentage'])
        return records
    
    def get_parent(self):
        return str(self.data['Parent'][0])