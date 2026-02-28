# ComfyUI-DNode: Lissajous Camera Shake (V1) 🎥

**开发者 (Author):** 心寸

---

## 🇨🇳 中文说明 (Chinese)

### 💡 开发背景
目前的数字人（Digital Human）和 AI 生成视频技术在生成人物时非常逼真，但由于镜头轨迹往往过于死板、完美，容易产生一种“电子僵硬感”，缺乏真实拍摄的生命力。

本节点 **Lissajous Camera Shake** 专门用于解决这一痛点。通过模拟真实手持镜头的微小肌肉晃动，为数字人视频注入逼然的“临场感”，显著提升视频的真实性和沉浸感。

### 🌟 核心特性
*   **平滑运镜**：基于利萨茹曲线 (Lissajous) 算法，通过叠加多组低频正弦波生成轨迹，而非简单的随机乱抖。
*   **中心对齐**：算法确保镜头始终围绕画面绝对中心点进行往复漂移，从根本上解决画面偏离、越飘越远的问题。
*   **高保真度**：提供平滑、无锐角的呼吸感运镜，模拟真实的人体肌肉控制感，完美适配手持拍摄模拟。

### ⚙️ 参数说明
*   **intensity (强度)**：控制晃动的剧烈程度。默认 **0.40** 是经过测试的最佳平衡点。
*   **zoom_factor (缩放)**：位移后的边缘保护机制。默认 **1.05** (放大5%) 配合 0.4 强度可完美防止黑边。
*   **fps (帧速率)**：视频的帧率，用于辅助算法计算符合物理规律的运动周期。
*   **seed (随机种子)**：决定多组频率叠加的初始形态，不同种子对应不同的平滑轨迹组合。

### 📥 安装方法
1.  **Git Clone (推荐)**：
    进入 ComfyUI 的 `custom_nodes` 文件夹，打开终端运行：
    `git clone https://github.com/Derryyyyyy/ComfyUI-DNode.git`
2.  **手动安装**：
    在 `custom_nodes` 下新建名为 **`ComfyUI-DNode`** 的文件夹，将本仓库的 `__init__.py` 放入其中。

### 💡 使用方法
1.  右键菜单路径：**`DNode`** -> **`🎥 Lissajous Camera Shake (V1)`**。
2.  输入端：连接视频帧序列（IMAGE 批次）。
3.  输出端：输出平滑抖动后的帧序列，可直接接入视频合并节点。

---

## 🇬🇧 English Documentation

### 💡 Background
Current Digital Human and AI video generation technologies produce highly realistic characters, but the outputs often feel "stiff" or "artificial" due to overly static or perfect camera movements.

**Lissajous Camera Shake** is designed to solve this specific problem. By simulating the subtle muscle tremors of a real handheld camera, it injects a sense of "authenticity" and "presence" into virtual videos, significantly enhancing their realism.

### 🌟 Core Features
*   **Smooth Motion**: Unlike common random noise shakes, this node generates trajectories by superimposing multiple low-frequency sine waves using the Lissajous algorithm.
*   **Center Aligned**: The algorithm ensures the camera always drifts around the absolute center of the frame, preventing the "drifting away" issue common in noise-based methods.
*   **High Fidelity**: Provides smooth, organic camera movement that simulates natural human muscle control, perfect for handheld simulation.

### ⚙️ Parameters
*   **intensity**: Controls the shake magnitude. Default **0.40** is the optimal balance for realistic handheld simulation.
*   **zoom_factor**: Protection mechanism against edge clipping. Default **1.05** (5% zoom) works perfectly with 0.4 intensity.
*   **fps**: Frame rate of the video, used to calculate correct physical motion cycles.
*   **seed**: Determines the initial state of frequency superposition. Each seed provides a unique smooth trajectory.

### 📥 Installation
1.  **Git Clone (Recommended)**:
    Navigate to your ComfyUI `custom_nodes` folder and run:
    `git clone https://github.com/Derryyyyyy/ComfyUI-DNode.git`
2.  **Manual Installation**:
    Create a folder named **`ComfyUI-DNode`** in your `custom_nodes` directory and place the `__init__.py` file inside.

### 💡 Usage
1.  Menu Path: **`DNode`** -> **`🎥 Lissajous Camera Shake (V1)`**.
2.  Input: Connect your image batch (IMAGE).
3.  Output: Outputs the shaken image batch, ready for video encoding nodes.
