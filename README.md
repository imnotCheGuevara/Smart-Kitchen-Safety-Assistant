# Smart Kitchen Safety Assistant  
**智能厨房安全助手：基于CV与多模态LLM的早期火情检测与风险预警系统**

![Kitchen Fire Detection Demo](https://via.placeholder.com/800x400?text=Demo+Video+Coming+Soon)  
*(演示视频即将上传)*

## 项目简介
我的第一个完整AI项目，目标是利用计算机视觉（YOLOv11）和多模态大模型（Qwen2-VL）实现厨房实时火情/烟雾检测，并在火势扩大前生成自然语言警报（中文），通过Telegram推送提醒用户。  
项目针对澳门家庭/学生宿舍场景，强调**本地运行 + 隐私保护 + 低成本**。

- **核心功能**：摄像头视频流 → 火/烟检测 → 风险评估 → 中文警报建议  
- **技术栈**：YOLOv11 + Qwen2-VL + OpenCV + Streamlit + Raspberry Pi  
- **数据集**：DetectiumFire (Kaggle) + 自采集澳门厨房视频  
- **当前阶段**：Week 1 - 项目规划与文档启动

## 项目书（Proposal）摘要
**目标**：mAP ≥ 0.80，假阳性 < 5%，RPi实时FPS ≥ 8  
**意义**：厨房火灾占住宅火灾50%以上，本系统比传统烟感更早预警  
**学习收获**：目标检测、多模态LLM、prompt工程、边缘部署  
详情见：[PROJECT_PROPOSAL.md](./Project proposal.md)

## 进度路线（14周计划）
- Week 1–2：规划、调研、环境  
- Week 3–6：数据 + CV训练  
- Week 7–8：LLM集成  
- Week 9–10：部署 + 警报  
- Week 11–14：测试、文档、展示

## 如何运行（Coming Soon）
安装依赖 → python main.py → 打开浏览器看demo

欢迎star/fork！这是我大二的第一个项目，持续更新中～  
William | Macau Polytechnic University | 2026.3
