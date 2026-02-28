# ComfyUI-DNode: Lissajous Camera Shake (V1) 🎥

**开发者 (Author):** 心寸

---

## 🎬 效果对比 (Comparison)

| 优化前 (Before / AI Stiff) | 优化后 (After / DNode Shake) |
| :---: | :---: |
| https://github.com/user-attachments/assets/aca1c343-18ca-4285-95a1-a3a9d7b3202b | https://github.com/user-attachments/assets/f6f4f3b8-1346-4003-a07a-82f3ce59eac1 |




---

## 🇨🇳 中文说明 (Chinese)

### 💡 开发背景
目前的数字人（Digital Human）和 AI 生成视频技术在生成人物时非常逼真，但由于镜头轨迹往往过于死板、完美，容易产生一种“电子僵硬感”，缺乏真实拍摄的生命力。

本节点 **Lissajous Camera Shake** 专门用于解决这一痛点。通过模拟真实手持镜头的微小肌肉晃动，为数字人视频注入逼然的“临场感”，显著提升视频的真实性和沉浸感。

### 🌟 核心特性
*   **平滑运镜**：基于利萨茹曲线 (Lissajous) 算法，通过叠加多组低频正弦波生成轨迹，而非简单的随机乱抖。
*   **中心对齐**：算法确保镜头始终围绕画面绝对中心点进行往复漂移，从根本上解决画面偏离、越飘越远的问题。
*   **高保真度**：提供平滑、无锐角的呼吸感运镜，模拟真实的人体肌肉控制感。

### ⚙️ 参数说明
*   **intensity (强度)**：默认 **0.40**。
*   **zoom_factor (缩放)**：默认 **1.05**。
*   **fps (帧速率)**：视频的帧率。
*   **seed (随机种子)**：轨迹随机种子。

---

## 🇬🇧 English Documentation

### 💡 Background
Current Digital Human and AI video generation technologies produce realistic characters, but outputs often feel "stiff" due to static camera movements. **Lissajous Camera Shake** injects authenticity into virtual videos by simulating subtle handheld tremors.

### 🌟 Core Features
*   **Smooth Motion**: Uses Lissajous algorithm to generate organic trajectories.
*   **Center Aligned**: Ensures the camera drifts around the absolute center.

---

### 📥 安装方法 (Installation)
1. **Git Clone**: `git clone https://github.com/Derryyyyyy/ComfyUI-DNode.git`
2. **Manual**: Create `ComfyUI-DNode` in `custom_nodes`.
