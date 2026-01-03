import mne
import os
import matplotlib.pyplot as plt


base_path = r"C:\Users\aparn\OneDrive\PROJECT_S3\IBS"


edf_file = os.path.join(base_path, "r01.edf")


raw = mne.io.read_raw_edf(edf_file, preload=True)


print("Channels:", raw.ch_names)
print("Sampling rate:", raw.info['sfreq'])


raw.plot(duration=10, scalings='auto',show=True)
plt.show()