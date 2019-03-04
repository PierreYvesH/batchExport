""" 
This file finds all the recordings the recording folder and extracts the data
'"""

import os
import extract_diameter

recording_path = ['C:/User/recordings']

recording_valid = []

csv_out = []
out_dir = 'C:/User/ExportedRecordings'
annotations = False

for pa in recording_path:
    recording_dates = os.listdir(pa)
    for da in recording_dates:
        folder = os.path.join(pa, da)
    
        # Find all dates where there was a recording
        recording_sessions = os.listdir(folder)

        for se in recording_sessions:
            # Find all recordings for each day
            session = os.path.join(folder, se)

            if os.path.isdir(session):
                recording_valid.append(session)
                csv_out.append('pupil_positions_'+ da + '_' + se + '.csv')

                if annotations:
                    csv_out.append('annotations_' + da + '_' + se + '.csv') 
            
extract_diameter.main(recording_valid, csv_out, out_dir, overwrite = True, annotations = annotations)



