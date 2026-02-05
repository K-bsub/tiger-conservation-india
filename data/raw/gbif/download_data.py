# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#!/usr/bin/env python3
"""
GBIF Tiger Downloader - Using Scientific Name
Downloads Panthera tigris occurrences from India using scientific name instead of taxon key

Usage:
    python download_tigers_by_name.py
"""

import requests
import pandas as pd
import json
from datetime import datetime
import time
import os
output_dir = os.getcwd()


def download_tigers_india():
    """Download tiger occurrences from India using scientific name"""

    print("="*80)
    print("GBIF TIGER DOWNLOAD - INDIA (Using Scientific Name)")
    print("="*80)
    print("Scientific Name: Panthera tigris")
    print("Country: India (IN)")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-"*80)

    # GBIF API endpoint
    api_url = "https://api.gbif.org/v1/occurrence/search"

    # Use scientific name instead of taxon key
    params = {
        'scientificName': 'Panthera tigris',
        'country': 'IN',
        'limit': 300,
        'offset': 0
    }

    all_records = []
    batch = 1

    try:
        # First request to get total count
        print("Getting total count...", end=' ')
        response = requests.get(api_url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        total_count = data.get('count', 0)

        # Show first result to verify species
        if data.get('results'):
            first_result = data['results'][0]
            print(f"\n✓ Found {total_count:,} records")
            print(f"Verified species: {first_result.get('species', 'N/A')}")
            print(f"Scientific name: {
                  first_result.get('scientificName', 'N/A')}")
        else:
            print(f"Found {total_count:,} records")

        print("-"*80)

        # Download all records
        while params['offset'] < total_count:
            print(f"Batch {batch}: Offset {params['offset']:,}...", end=' ')

            response = requests.get(api_url, params=params, timeout=30)
            response.raise_for_status()

            data = response.json()
            records = data.get('results', [])

            if not records:
                print("No more records")
                break

            all_records.extend(records)
            print(f"Got {len(records)} records. Total: {len(all_records):,}/{total_count:,} "
                  f"({100*len(all_records)/total_count:.1f}%)")

            # Next batch
            params['offset'] += 300
            batch += 1

            # Small delay to be nice to the API
            time.sleep(0.2)

        print("-"*80)
        print(f"✓ Downloaded {len(all_records):,} records")
        return all_records, total_count

    except requests.exceptions.RequestException as e:
        print(f"\n✗ Error: {e}")
        print(f"Partial download: {len(all_records):,} records")
        return all_records, len(all_records)
    except KeyboardInterrupt:
        print(f"\n⚠ Interrupted. Partial download: {
              len(all_records):,} records")
        return all_records, len(all_records)


def process_and_save(records, total_count):
    """Process and save records"""

    if not records:
        print("No records to process")
        return None

    print(f"\nProcessing {len(records):,} records...")

    # Convert to DataFrame
    processed = []
    for rec in records:
        processed.append({
            'gbifID': rec.get('gbifID'),
            # Include actual taxon key for reference
            'taxonKey': rec.get('taxonKey'),
            'species': rec.get('species'),
            'scientificName': rec.get('scientificName'),
            'subspecies': rec.get('infraspecificEpithet'),
            'decimalLatitude': rec.get('decimalLatitude'),
            'decimalLongitude': rec.get('decimalLongitude'),
            'coordinateUncertaintyInMeters': rec.get('coordinateUncertaintyInMeters'),
            'country': rec.get('country'),
            'countryCode': rec.get('countryCode'),
            'stateProvince': rec.get('stateProvince'),
            'locality': rec.get('locality'),
            'eventDate': rec.get('eventDate'),
            'year': rec.get('year'),
            'month': rec.get('month'),
            'day': rec.get('day'),
            'basisOfRecord': rec.get('basisOfRecord'),
            'institutionCode': rec.get('institutionCode'),
            'catalogNumber': rec.get('catalogNumber'),
            'recordedBy': rec.get('recordedBy'),
            'occurrenceStatus': rec.get('occurrenceStatus'),
            'individualCount': rec.get('individualCount'),
            'datasetName': rec.get('datasetName'),
            'publisher': rec.get('publisher'),
            'license': rec.get('license'),
        })

    df_all = pd.DataFrame(processed)
    print(f"Created DataFrame: {len(df_all):,} rows × {
          len(df_all.columns)} columns")

    # Show what taxon keys were found
    print(f"\nTaxon keys in results: {df_all['taxonKey'].unique()}")

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save ALL records (all years)
    csv_all = f'{output_dir}/tiger_india_ALL_YEARS_{timestamp}.csv'
    df_all.to_csv(csv_all, index=False)
    print(f"\n✓ Saved ALL records: {csv_all}")

    # Filter for 2006-2022
    df_filtered = df_all[(df_all['year'] >= 2006) &
                         (df_all['year'] <= 2022)].copy()
    csv_filtered = f'{output_dir}/tiger_india_2006_2022_{timestamp}.csv'
    df_filtered.to_csv(csv_filtered, index=False)
    print(f"✓ Saved 2006-2022 filtered: {csv_filtered}")
    print(f"  Filtered records: {len(df_filtered):,} (removed {
          len(df_all)-len(df_filtered):,} outside range)")

    # Save raw JSON
    json_file = f'{output_dir}/tiger_india_raw_{timestamp}.json'
    with open(json_file, 'w') as f:
        json.dump(records, f, indent=2)
    print(f"✓ Saved raw JSON: {json_file}")

    # Create summary
    summary = {
        'download_timestamp': datetime.now().isoformat(),
        'scientific_name': 'Panthera tigris',
        'country': 'India',
        'total_available': total_count,
        'total_downloaded': len(df_all),
        'filtered_2006_2022': len(df_filtered),
        'taxon_keys_found': df_all['taxonKey'].unique().tolist(),
        'records_with_coordinates': int(df_all['decimalLatitude'].notna().sum()),
        'states': int(df_all['stateProvince'].nunique()),
        'years_range': f"{df_all['year'].min():.0f} - {df_all['year'].max():.0f}"
    }

    summary_file = f'{output_dir}/download_summary_{timestamp}.json'
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"✓ Saved summary: {summary_file}")

    # Print summary
    print("\n" + "="*80)
    print("DOWNLOAD COMPLETE - SUMMARY")
    print("="*80)
    print("Scientific Name: Panthera tigris")
    print(f"Total GBIF records for India: {total_count:,}")
    print(f"Downloaded: {len(df_all):,} records")
    print(f"After 2006-2022 filter: {len(df_filtered):,} records")
    print(f"Date range (all data): {
          df_all['year'].min():.0f} - {df_all['year'].max():.0f}")
    print(f"Records with coordinates: {
          df_all['decimalLatitude'].notna().sum():,}")
    print(f"Indian states/regions: {df_all['stateProvince'].nunique()}")

    print("\nSpecies Verification:")
    print(f"  Unique species: {df_all['species'].unique()}")
    print(f"  Taxon keys found: {df_all['taxonKey'].unique()}")

    print("\nTop 10 States (all years):")
    for state, count in df_all['stateProvince'].value_counts().head(10).items():
        state_name = state if state else 'Unknown'
        print(f"  {state_name:30s}: {count:5,} records")

    print("\nBasis of Record:")
    for basis, count in df_all['basisOfRecord'].value_counts().head(10).items():
        print(f"  {basis:30s}: {count:5,} records")

    print("\nYear Distribution (2006-2022):")
    yearly = df_filtered.groupby('year').size()
    for year in range(2006, 2022):
        count = yearly.get(year, 0)
        if count > 0:
            print(f"  {year}: {count:4,} records")

    print("\n" + "="*80)
    print(f"Files saved in: {output_dir}/")
    print("="*80)

    return df_all, df_filtered


def main():
    """Main execution"""

    print("\nNOTE: Using scientific name 'Panthera tigris' instead of taxon key")
    print("This ensures we get the correct species!\n")

    # Download
    records, total_count = download_tigers_india()

    if not records:
        print("\n⚠ No data downloaded. Check your internet connection.")
        return

    # Process and save
    result = process_and_save(records, total_count)

    if result is not None:
        df_all, df_filtered = result
        print("\n✓ Success! Data ready for analysis.")
        print("\nTo load the data in Python:")
        print("  import pandas as pd")
        print("  df = pd.read_csv('tiger_india_gbif_data/tiger_india_2006_2022_*.csv')")
        print("\nTo verify species:")
        print("  print(df['species'].value_counts())")
        print("  print(df['scientificName'].value_counts())")


if __name__ == "__main__":
    main()
