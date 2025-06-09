import numpy as np
import os
from scipy.signal import butter, filtfilt

# --- Configuration Parameters ---
fs = 250                 # Sampling rate in Hz
duration = 2.048              # Duration in seconds (2.048 s * 250 Hz = 512 samples)
num_samples = int(fs * duration) # Calculate exact number of samples
num_lines_per_class = 200     # Number of signal instances per CSV file (class)
output_dir = "generated_eeg_signals" # Directory to save CSVs

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Time vector for signal generation
t = np.linspace(0, duration, num_samples, endpoint=False)


eeg_bands_params = {
    "delta": {
        "freq_range": [0.5, 4],  # Hz
        "amp_range": [10, 50],   # µV
        "noise_scale": 0.5       # Multiplier for raw noise before filtering
    },
    "theta": {
        "freq_range": [4, 8],    # Hz
        "amp_range": [8, 30],    # µV
        "noise_scale": 0.7
    },
    "alpha": {
        "freq_range": [8, 13],   # Hz
        "amp_range": [5, 20],    # µV
        "noise_scale": 1.0
    },
    "beta": {
        "freq_range": [13, 30],  # Hz
        "amp_range": [2, 15],    # µV
        "noise_scale": 1.5
    },
    "gamma": {
        "freq_range": [30, 100], # Hz (up to Nyquist for 250Hz fs is 125Hz)
        "amp_range": [0.5, 8],   # µV
        "noise_scale": 2.0       # More "noisy" appearance for higher frequencies
    }
}

# --- Signal Generator Function (Band-pass Filtered Noise) ---
def generate_eeg_band_signal(band_params, sampling_rate, num_samples):
    """
    Generates an EEG-like signal for a specific band using band-pass filtered white noise.
    """
    freq_low, freq_high = band_params["freq_range"]
    amp_min, amp_max = band_params["amp_range"]
    noise_scale = band_params["noise_scale"]

    # Generate raw white noise. Scale by a random amplitude within the desired range.
    # We multiply by noise_scale to ensure there's enough raw amplitude for filtering
    # and then normalize later if needed.
    raw_noise = np.random.randn(num_samples) * np.random.uniform(amp_min, amp_max) * noise_scale

    # Design Butterworth band-pass filter
    nyquist = 0.5 * sampling_rate
    low_cutoff_norm = freq_low / nyquist
    high_cutoff_norm = freq_high / nyquist
    order = 4 # Filter order, a good balance between sharpness and ringing

    # Basic validation for filter frequencies
    if low_cutoff_norm >= 1.0 or high_cutoff_norm >= 1.0 or low_cutoff_norm >= high_cutoff_norm:
        # Fallback for invalid filter ranges (e.g., if freq_high > Nyquist)
        # This can happen if params are too high for the sampling rate.
        print(f"Warning: Invalid filter parameters for range [{freq_low}, {freq_high}] Hz. "
              f"Nyquist is {nyquist} Hz. Returning raw noise instead.")
        return raw_noise

    # Apply the filter (filtfilt for zero phase distortion)
    b, a = butter(order, [low_cutoff_norm, high_cutoff_norm], btype='band')
    filtered_signal = filtfilt(b, a, raw_noise)

    # Optional: Normalize amplitude of the filtered signal to roughly fit the desired range
    # This helps in controlling the output amplitude more consistently.
    # Note: This is an approximation and might not perfectly match amp_range min/max.
    current_amp = np.max(np.abs(filtered_signal))
    if current_amp > 0:
        scaling_factor = np.random.uniform(amp_min, amp_max) / current_amp
        filtered_signal = filtered_signal * scaling_factor

    return filtered_signal

# --- Generate and Save Signals ---
print(f"Generating EEG-like signals for {len(eeg_bands_params)} bands...")

for band_name, params in eeg_bands_params.items():
    file_path = os.path.join(output_dir, f"{band_name}.csv")
    print(f"  Generating {num_lines_per_class} '{band_name}' signals to {file_path}...")

    with open(file_path, 'w') as f:
        for i in range(num_lines_per_class):
            # Generate the signal for the current band
            signal = generate_eeg_band_signal(params, fs, num_samples)

            # Ensure the signal has exactly num_samples (should be by design, but good check)
            if len(signal) != num_samples:
                raise ValueError(f"Generated signal for {band_name} has {len(signal)} samples, expected {num_samples}")

            # Format the signal as a space-separated string with 3 decimal places
            line = " ".join(f"{x:.3f}" for x in signal)
            f.write(line + "\n")

print(f"\nAll EEG signal files generated successfully in '{output_dir}'.")
print(f"Each CSV contains {num_lines_per_class} lines, with {num_samples} space-separated values per line.")
print("The values represent amplitude in microvolts (µV).")

# --- Optional: Visualize one of the generated signals and its FFT ---
# This part is just for verification and not part of the CSV generation loop.
import matplotlib.pyplot as plt

def plot_signal_and_fft(signal, sampling_rate, title, xlim_time=0.5, xlim_freq=120):
    """Plots a signal in time domain and its FFT in frequency domain."""
    N = len(signal)
    time = np.linspace(0, N/sampling_rate, N, endpoint=False)
    yf = np.fft.fft(signal)
    xf = np.fft.fftfreq(N, 1 / sampling_rate)

    plt.figure(figsize=(14, 5))

    plt.subplot(1, 2, 1)
    plt.plot(time, signal)
    plt.title(f'Time Domain: {title}')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (µV)')
    plt.xlim(0, xlim_time) # Zoom in for clarity
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(xf[:N//2], 2/N * np.abs(yf[:N//2])) # Plot only positive frequencies, normalize amplitude
    plt.title(f'Frequency Domain (FFT): {title}')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power/Amplitude')
    plt.xlim(0, xlim_freq) # Show relevant frequency range up to Nyquist
    plt.grid(True)
    plt.tight_layout()
    plt.show()

print("\n--- Visualizing a sample signal and its FFT from each band ---")
for band_name in eeg_bands_params.keys():
    # Read the first line of the generated CSV for visualization
    file_path = os.path.join(output_dir, f"{band_name}.csv")
    with open(file_path, 'r') as f:
        sample_line_str = f.readline()
    sample_signal = np.array([float(x) for x in sample_line_str.split()])
    plot_signal_and_fft(sample_signal, fs, f'{band_name} Signal Sample')