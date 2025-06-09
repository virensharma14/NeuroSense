# NeuroSense – Real-Time Mental Health Monitoring System on STM32N6

## Overview

**NeuroSense** is a real-time, embedded mental health monitoring system powered by the **STM32N6** microcontroller. It integrates:

- Speech analysis  
- EEG signal acquisition  
- Facial emotion recognition  

to detect stress, anxiety, depression, and other emotional states. The device uses an interactive **TouchGFX-based touchscreen UI** to provide instant feedback, mood tracking, and alerts. This makes it suitable for personal health monitoring, workplace stress management, therapy support, and clinical triage.

## Why This Project?

Mental health is a critical global issue:  
- 1 in 8 people worldwide suffer from a mental disorder (WHO)  
- Stress-related illnesses cost over $1 trillion annually in lost productivity  
- Real-time, accessible, and non-invasive monitoring tools are limited and often expensive  

**NeuroSense bridges this gap** by offering a compact, multimodal AI-powered solution on a cost-effective embedded platform using STM32N6.

## Objectives

- Integrate speech, EEG biosignals, and facial emotion data into a unified AI model for mental state inference  
- Implement STM32-based EEG acquisition circuitry with high-precision amplification, filtering, and ADC digitization (based on Wang Qiongying et al., 2015)  
- Provide real-time feedback via an interactive TouchGFX LCD user interface  
- Enable applications for personal mood tracking, workplace stress monitoring, and hospital triage  
- Support offline operation to ensure data privacy and usability in low-connectivity environments  

## Why This Should Be Selected

This project demonstrates the power of **STM32N6** for impactful, real-world healthcare solutions by combining edge AI, biosensing, and real-time embedded machine learning. Potential applications include:

- Detecting employee burnout in high-stress jobs (healthcare, IT)  
- Supporting therapy in remote or low-resource areas  
- Daily mood tracking for anxiety or depression management  
- Emergency triage for mental distress in hospitals or public spaces  

NeuroSense also helps reduce mental health stigma by making monitoring seamless and accessible.

## Core Components Required

- 1 × STM32N6570-DK Board  
- EEG Electrodes  
- 1 × SD Card  
- 1 × INA128 (or equivalent instrumentation amplifier)  
- OpAmps and passive components for Power line filtering and low pass filtering.  


---

## Contact

For questions or collaboration, please contact:  
Girish Arora
Viren Sharma
Kartik Khandelwal

