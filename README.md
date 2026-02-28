
# ComfyUI-DNode: Lissajous Camera Shake (V1) 🎥
---

## 🎬 效果对比 (Comparison)

| 优化前 (Before) | 优化后 (After) |
| :---: | :---: |
| <video src="https://github.com/user-attachments/assets/a5748d7d-e4ca-4ac6-a496-3714c980b498" height="400px" controls></video> | <video src="https://github.com/user-attachments/assets/6b77a542-b380-4977-952f-03c6e2689de6" height="400px" controls></video> |

---
## 🇨🇳 中文说明

### 💡 开发背景
目前的数字人（Digital Human）和 AI 生成视频技术在生成人物时非常逼真，但由于镜头轨迹往往过于死板、完美，容易产生一种“电子僵硬感”，缺乏真实拍摄的生命力。

本节点 **Lissajous Camera Shake** 专门用于解决这一痛点。通过模拟真实手持镜头的微小肌肉晃动，为数字人视频注入逼然的“临场感”，显著提升视频的真实性和沉浸感。

### 🌟 核心特性
*   **平滑运镜**：基于利萨茹曲线 (Lissajous) 算法，通过叠加多组低频正弦波生成轨迹，而非简单的随机乱抖。
*   **中心对齐**：算法确保镜头始终围绕画面绝对中心点进行往复漂移，从根本上解决画面偏离、越飘越远的问题。
*   **高保真度**：提供平滑、无锐角的呼吸感运镜，模拟真实的人体肌肉控制感。

### ⚙️ 参数说明
*   **intensity (强度)**：默认 **0.40**，控制晃动剧烈程度。
*   **zoom_factor (缩放)**：默认 **1.05**，位移后的边缘保护。
*   **fps (帧速率)**：视频的帧率，用于辅助计算运动周期。
*   **seed (随机种子)**：决定运动轨迹的初始形态。

### 📥 安装方法
1.  **Git Clone (推荐)**：
    进入 ComfyUI 的 `custom_nodes` 文件夹运行：
    `git clone https://github.com/Derryyyyyy/ComfyUI-DNode.git`
2.  **手动安装**：
    在 `custom_nodes` 下新建名为 `ComfyUI-DNode` 的文件夹，将 `__init__.py` 放入其中。

### 💡 使用方法
*   在 ComfyUI 中右键选择：`DNode` -> `🎥 Lissajous Camera Shake (V1)`。
*   将视频帧序列连接至 `images` 输入端即可。

<br>

---

## 🇬🇧 English Documentation

### 💡 Background
Current Digital Human and AI video technologies produce realistic characters, but the outputs often feel "stiff" due to overly static or perfect camera movements.

**Lissajous Camera Shake** is designed to solve this problem. By simulating the subtle muscle tremors of a real handheld camera, it injects "presence" into virtual videos, significantly enhancing realism.

### 🌟 Core Features
*   **Smooth Motion**: Based on the Lissajous algorithm, generating organic trajectories via superimposed low-frequency sine waves.
*   **Center Aligned**: Ensures the camera always drifts around the absolute center, preventing frame deviation.
*   **High Fidelity**: Provides smooth, organic camera movement simulating natural human muscle control.

### ⚙️ Parameters
*   **intensity**: Default **0.40**. Controls the magnitude of the shake.
*   **zoom_factor**: Default **1.05**. Edge protection for frame shifting.
*   **fps**: Frame rate used for calculating physical motion cycles.
*   **seed**: Determines the unique initial state of the trajectory.

### 📥 Installation
1.  **Git Clone (Recommended)**:
    Run in your ComfyUI `custom_nodes` folder:
    `git clone https://github.com/Derryyyyyy/ComfyUI-DNode.git`
2.  **Manual Installation**:
    Create a folder named `ComfyUI-DNode` in `custom_nodes` and place `__init__.py` inside.

### 💡 Usage
*   Find the node in the menu: `DNode` -> `🎥 Lissajous Camera Shake (V1)`.
*   Connect your video frame sequence to the `images` input.
---

### 📥 安装方法 (Installation)
1. **Git Clone**: `git clone https://github.com/Derryyyyyy/ComfyUI-DNode.git`
2. **Manual**: Create `ComfyUI-DNode` in `custom_nodes`.
