Smart Kitchen Safety Assistant: Early Fire Detection and Risk Alert System Based on CV and Multimodal LLM
Project Proposer: William Yang
Project Launch Date: March 2026
Estimated Completion Cycle: 14 weeks (March – June 2026)
Guiding Objectives: Through this project, systematically master core AI skills including Computer Vision (CV), multimodal integration of Large Language Models (LLM), and edge deployment, and deliver a demonstrable and open-source practical prototype to enhance personal project experience and resume competitiveness.
I. Background & Significance
Kitchen fires are one of the primary causes of residential fires. According to global fire statistics, cooking-related fires account for more than 50% of household fires, and they often start in the early stage such as overheated oil pans and ignited food. Traditional smoke/temperature detectors are prone to high false alarm rates due to steam and oil fumes, failing to nip fires in the bud.
With the maturity of AI vision technology, flame/smoke detection based on real-time video streams has become feasible. Furthermore, combined with multimodal large models (Vision-Language Models), the system can not only detect fire but also understand the scene, evaluate risk levels, and generate Chinese natural language alerts and handling suggestions (e.g., "High Risk: Oil Pan Fire! Please close the gas valve immediately and smother the fire with a pot lid").
This project targets kitchen scenarios of local families and student dormitories in Macao, and constructs a privacy-preserving, low-cost and implementable smart kitchen safety assistant, which has both technical learning value and practical application potential.
II. Objectives
Core Objectives
Develop an end-to-end kitchen fire early warning system to realize the following functional chain:
Real-time camera video stream → CV model for flame/smoke detection → Multimodal LLM for risk analysis and alert generation → Local/Telegram push of Chinese alerts
Quantitative Indicators (Expected)
Mean Average Precision (mAP@0.5) of object detection ≥ 0.80 (based on fine-tuned YOLOv11)
False positive rate (false alarms from steam/lighting) < 5% (one-week test in real fire-free kitchen scenarios)
Accuracy of LLM alert generation > 85% (manual evaluation of 10 typical scenarios)
Real-time inference FPS ≥ 8 on edge device (Raspberry Pi 5)
Fully local system operation (no cloud upload, privacy protection)
Learning Objectives
Master the full workflow of YOLOv11 object detection (dataset preparation, training, optimization, HSV color space experiments)
Learn image+text inference and prompt engineering of multimodal LLMs (Qwen2-VL / LLaVA)
Practice edge deployment (RPi + OpenCV + quantized models) and real-time alert system (Telegram Bot)
Complete a full project cycle from 0 to 1 (code, documentation, demo video, report)
III. Technical Approach
Overall Architecture
Data Collection and Preparation
Main dataset: DetectiumFire (released on Kaggle in 2025, a large-scale multimodal fire dataset containing 212 images of uncontrolled kitchen fires, 54 images of controlled cooking fires, with bounding boxes and text descriptions)
Self-collected data: 30–50 local kitchen videos in Macao (simulating safe scenarios such as early smoke emission and hot oil ignition)
Tools: Roboflow (annotation, augmentation, export in YOLO format)
Computer Vision Module (Fire/Smoke Detection)
Model: Ultralytics YOLOv11m (or s/n versions for edge deployment)
Optimization directions: HSV color space preprocessing, continuous frame confirmation mechanism to reduce false alarms
Output: bounding box + confidence score + category (fire / smoke)
Multimodal Risk Reasoning Module
Model: Qwen2-VL-7B-Instruct (open-sourced by Alibaba, with strong Chinese language capability) or quantized version
Input: Cropped fire image + prompt (including scene description, DetectiumFire captions as RAG knowledge)
Output: Risk level (low/medium/high) + Chinese alert suggestions
System Integration and Deployment
Real-time stream processing: OpenCV video capture
Web Demo: Streamlit (view video feeds and historical alerts via local browser)
Alert channel: Telegram Bot push (supports real-time notifications in Macao)
Edge platform: Raspberry Pi 5 + USB/Pi Camera (final deployment)
IV. Deliverables
GitHub open-source repository (complete code, dataset links, training logs, README)
Runnable demos: Web version + RPi version + Telegram alert system
2–3 minute demonstration video (uploaded to Bilibili/YouTube)
Project report (4–6 pages): Problem analysis, technical route, experimental results, challenges and prospects
Sample resume highlight: "Independently developed a multimodal AI kitchen safety system, fine-tuned YOLOv11 based on the DetectiumFire dataset and integrated Qwen2-VL, realizing real-time fire detection and natural language risk early warning with mAP of 0.82 and deployment on Raspberry Pi."
V. Risks and Mitigation Strategies
Data scarcity / time-consuming annotation → Prioritize high-quality subsets of DetectiumFire, with self-collected data only as supplementation
High model false alarm rate → Add non-fire negative samples, time-series filtering and threshold tuning
Insufficient hardware/computing power → Use Colab free GPU in the early stage, and deploy quantized models on RPi later
Tight schedule → Adopt phased milestones: first implement and verify the pure CV version, then integrate LLM
VI. Timeline Summary
Week 1–2: Planning, research and environment setup
Week 3–6: Data preparation and CV model training & optimization
Week 7–8: LLM integration and pipeline construction
Week 9–10: System deployment and alert system development
Week 11–12: Real-world testing and iteration
Week 13–14: Documentation, video production and presentation preparation
Project Proposer's Signature: William Yang
Date: March 19, 2026