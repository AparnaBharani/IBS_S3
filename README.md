# IBS_S3
# Non-Invasive Fetal ECG Extraction using Independent Component Analysis (ICA)

##  Project Overview
This project focuses on the **Biomedical Signal Analysis** of fetal electrocardiograms (fECG). The primary objective is to non-invasively extract the fetal ECG signal from abdominal maternal recordings where maternal and fetal heart activities are mixed with noise.

Using **Independent Component Analysis (ICA)**, this project isolates the fetal ECG component from multichannel abdominal signals and validates the extraction by comparing it against a direct fetal scalp electrode recording (ground truth).

---

##  Problem Statement & Objectives
**Problem:** Fetal ECG signals acquired from the maternal abdomen are significantly weaker (~10× smaller) than maternal ECG signals and often overlap in frequency, making extraction difficult due to noise and maternal dominance.

**Objective:**
1.  To non-invasively isolate the fetal ECG using **Independent Component Analysis (ICA)**.
2.  To validate the extracted signal by comparing it with the direct fetal reference signal.
3.  To compute the Heart Rate (BPM) and detect R-peaks.

---

##  Dataset
The project utilizes the **Abdominal and Direct Fetal ECG Database (ADFECGDB)** from PhysioNet.

* **Records:** 5 records (`r01.edf` to `r05.edf`).
* **Duration:** 5 minutes per record.
* **Sampling Rate:** 1000 Hz.
* **Channels:**
    * **4 Abdominal Channels:** Mixed maternal and fetal signals.
    * **1 Direct Fetal Channel:** Scalp electrode signal (Ground Truth).

---

##  Methodology

The project pipeline follows these distinct stages:

### 1. Data Loading
* EDF (European Data Format) files are loaded using the `mne` or `pyEDFlib` library.
* Channel information and sampling frequencies are extracted.

### 2. Signal Preprocessing
To ensure stability for the ICA algorithm, the raw signals undergo:
* **Bandpass Filtering:** Applied between **0.5 Hz – 45 Hz** to remove baseline drift (low freq) and power line interference/muscle noise (high freq).
* **Normalization:** Signals are standardized to have zero mean and unit variance.

### 3. Independent Component Analysis (ICA)
* **Concept:** ICA is a blind source separation technique. It assumes the abdominal signal is a linear mixture of statistically independent sources (Maternal Heart, Fetal Heart, Noise).
* **Process:** The algorithm decomposes the 4 input abdominal channels into 4 independent components.

### 4. Component Identification & Validation
* Each independent component is compared with the **Direct Fetal ECG** (reference channel).
* **Correlation Analysis:** The component with the highest correlation coefficient relative to the direct fECG is identified as the extracted fetal signal.

### 5. Post-Processing
* **R-Peak Detection:** Locating the peaks of the QRS complex in the extracted signal.
* **Heart Rate Calculation:** Computing Beats Per Minute (BPM).

---

ing raw EDF data
└── README.md           # Project documentation
