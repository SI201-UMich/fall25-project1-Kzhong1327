# Name: Ke Zhpng
# Student ID: 49628069
# Email: kzhong@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): Chatgpt
# If you worked with generative AI also add a statement for how you used it.  
# Asked ChatGPT hints for debugging

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
            try:
                row['flipper_length_mm'] = float(row['flipper_length_mm'])
            except:
                row['flipper_length_mm'] = None
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



def calculate_flipper_percentage(data, threshold=200):

    result2 = {}

    for penguin in data:
        species = penguin['species']
        sex = penguin['sex']
        flipper = penguin['flipper_length_mm']

        if not species or not sex or flipper is None:
            continue

        key = (species, sex)
        if key not in result2:
            result2[key] = {'total': 0, 'above': 0}

        result2[key]['total'] += 1
        if flipper > threshold:
            result2[key]['above'] += 1

    for key, counts in result2.items():
        total = counts['total']
        above = counts['above']
        percentage = round((above / total) * 100, 2)
        result2[key]['percentage_above'] = percentage

    return result2


def write_results_to_txt(results, filename, threshold=200):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Percentage of Penguins Above {threshold} mm Flipper Length\n")
        file.write("=" * 60 + "\n\n")

        for (species, sex), stats in results.items():
            file.write(f"Species: {species}\n")
            file.write(f"Sex: {sex}\n")
            file.write(f"Percentage above {threshold} mm: {stats['percentage_above']}%\n")
            file.write(f"Total penguins in group: {stats['total']}\n")
            file.write(f"Above threshold: {stats['above']}\n")
            file.write("-" * 40 + "\n")

    print(f"Results saved to {filename}")




def main():
    filename = 'penguins.csv' 
    data = read_csv_file(filename)
    results = calculate_species_averages(data)
    write_results_to_csv(results, 'penguin_species_summary.csv')
    results2 = calculate_flipper_percentage(data, threshold=200)
    write_results_to_txt(results2, 'penguin_flipper_percentage.txt', threshold=200)



if __name__ == '__main__':
    main()
