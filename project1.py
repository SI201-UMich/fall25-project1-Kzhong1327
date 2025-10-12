import csv


def read_csv_file(filename):
    """Read a CSV file into a list of dictionaries"""
    data = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                row['body_mass_g'] = float(row['body_mass_g'])
            except:
                row['body_mass_g'] = None
            try:
                row['bill_length_mm'] = float(row['bill_length_mm'])
            except:
                row['bill_length_mm'] = None
            data.append(row)
    return data


def calculate_species_averages(data):
    """Return a dictionary with average mass and bill length per species"""
    result = {}
    species_data = {}

    for penguin in data:
        species = penguin['species']
        body_mass = penguin['body_mass_g']
        bill_length = penguin['bill_length_mm']

        if body_mass is None or bill_length is None:
            continue

        if species not in species_data:
            species_data[species] = {
                'mass_sum': 0.0,
                'bill_sum': 0.0,
                'count': 0
            }
        species_data[species]['mass_sum'] += body_mass
        species_data[species]['bill_sum'] += bill_length
        species_data[species]['count'] += 1

    for species, stats in species_data.items():
        avg_mass = stats['mass_sum'] / stats['count']
        avg_bill = stats['bill_sum'] / stats['count']
        result[species] = {
            'avg_body_mass_g': round(avg_mass, 2),
            'avg_bill_length_mm': round(avg_bill, 2)
        }
    return result



def write_results_to_csv(results, filename):
    """Write the results dictionary to a CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['species', 'avg_body_mass_g', 'avg_bill_length_mm']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for species, stats in results.items():
            writer.writerow({
                'species': species,
                'avg_body_mass_g': stats['avg_body_mass_g'],
                'avg_bill_length_mm': stats['avg_bill_length_mm']
            })
    print(f"Results written to {filename}")



def main():
    filename = 'penguins.csv' 
    data = read_csv_file(filename)
    results = calculate_species_averages(data)
    write_results_to_csv(results, 'penguin_species_summary.csv')



if __name__ == '__main__':
    main()
