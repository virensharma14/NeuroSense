NeuroSense – Real-Time Mental Health Monitoring System on STM32N6
NeuroSense is a real-time, embedded mental health monitoring device powered by STM32N6. It uses speech analysis, EEG signals, and facial emotion recognition to detect stress, anxiety, depression, and other emotional states. With the use of interactive TouchGFX-based touchscreen UI, users can receive instant feedback, mood tracking, and alerts, enabling applications in personal health, workplaces, therapy, and clinical environments. Our proposed system aims to be an optimized, lightweight and efficient embedded health solution to neurological medical issues.
Why This Project?
Mental health issues are a global crisis. According to WHO, 1 in 8 people globally live with a mental disorder, with depression and anxiety leading the burden. Stress-related illnesses cost $1 trillion annually in lost productivity. Despite this, real-time, accessible, and non-invasive monitoring tools are limited in number and are often expensive.
NeuroSense bridges this gap by delivering a compact, multimodal (YoloV8, miniresnetV2, LSTM) AI solution for early detection and continuous mental state monitoring. We want to harness the AI and DSP capabilities on this MCU discovery kit as this would allow us to develop the proposed system efficiently in the future.  
Objectives
Integrate speech, bio-signals (EEG), and facial data into a single AI-based model for mental state inference.
For EEG signal acquisition, we will implement a proven STM32-based circuitry similar to the design presented by WANG Qiongying, ZHANG Hongmin, LI Zhuqin, et al. Design of Electroencephalogram Acquisition System Based on STM32[J]. Journal of Integration Technology,2015,4(5):54-62. This includes high-precision signal amplification, filtering, and ADC-based digitization to ensure reliable EEG data collection for mental state analysis.
Provide real-time feedback via an interactive TouchGFX LCD UI.
Serve multiple use cases: personal tracking, workplace stress monitoring, and hospital triage.
Enable offline operation, ensuring data privacy and accessibility anywhere.
Why This Should Be Selected
This project showcases the power of STM32N6 for real-world societal impact, pushing the limits of Edge AI for healthcare. It tackles a critical and growing global issue with practical applications across sectors. By combining machine learning, bio-sensing, and real-time AI deployed on microcontrollers, we aim to provide an efficient humane solution. The problem is a global concern in the corporate setup worldwide and solutions such as ours could help eradicate this issue.
Real-life examples of relevance:
Employee burnout detection in high-stress jobs (e.g., healthcare, IT).
Therapy support for patients in remote or low-resource areas.
Daily mood tracking for individuals with anxiety or depression.
Emergency triage for mental distress in hospitals or public spaces.
This system could reduce mental health stigma by making monitoring seamless and accessible.
Core Components Required
1 x STM32N6570-DK Board
EEG Electrodes 
1 x SD Card 
1 x INA128 or some other instrumentation amplifier 
OpAmps to build Band-Pass Filte
