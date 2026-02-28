# ==============================================================================
# 本节点由 心寸 开发
# Author: 心寸
# Description: 基于 Lissajous 曲线的 ComfyUI 手持镜头运镜模拟节点
# ==============================================================================

import torch
import torch.nn.functional as F
import numpy as np
import json

def ease_out_quadratic(t: float) -> float:
    return 1 - (1 - t) ** 2

def generate_lissajous_trajectory(
    frame_count: int,
    fps: float,
    width: int,
    height: int,
    intensity: float = 1.0,
    seed: int = 42
) -> dict:
    np_random = np.random.RandomState(seed)
    dx_total = np.zeros(frame_count)
    dy_total = np.zeros(frame_count)
    frequencies =[0.033, 0.1, 0.2, 0.3]
    
    for freq in frequencies:
        t = np.arange(frame_count) / fps
        phase = 2 * np.pi * t * freq
        amp = np_random.uniform(5.2, 15.6)
        
        if np_random.random() < 0.64:
            angle_deg = np_random.uniform(0, 45)
        else:
            angle_deg = np_random.uniform(45, 90)
            
        if np_random.random() < 0.5:
            angle_deg = -angle_deg
        if np_random.random() < 0.5:
            angle_deg = 180 - angle_deg
            
        angle_rad = np.deg2rad(angle_deg)
        phase_normalized = (phase % (2 * np.pi)) / (2 * np.pi)
        envelope = np.array([ease_out_quadratic(min(p, 1.0)) for p in phase_normalized])
        
        base_motion = np.sin(phase) * envelope * amp
        arc_offset = np.sin(phase) * np.deg2rad(np_random.uniform(15, 30))
        
        dx_total += base_motion * np.cos(angle_rad + arc_offset)
        dy_total += base_motion * np.sin(angle_rad + arc_offset)
    
    dx_total = dx_total * intensity
    dy_total = dy_total * intensity
    dtheta = np.zeros(frame_count)
    
    return {
        "dx": dx_total.tolist(),
        "dy": dy_total.tolist(),
        "dtheta": dtheta.tolist(),
        "frame_count": frame_count,
        "fps": fps,
        "width": width,
        "height": height,
        "intensity": intensity
    }


class DNode_CameraShakeLissajous:
    DESCRIPTION = """🎥 Lissajous Camera Shake (V1)

【核心特性】
基于利萨茹曲线(Lissajous)算法，通过叠加多组低频正弦波，确保镜头始终围绕画面绝对中心点进行平滑的呼吸感往复漂移，从根本上解决传统噪波抖动带来的画面偏离问题。

【参数说明】
- intensity (强度): 控制晃动剧烈程度。0.40为最佳手持平衡点。
- zoom_factor (缩放): 边缘防穿帮保护。1.05为默认安全区。
- fps (帧速率): 用于计算正确的物理运动周期。
- seed (随机种子): 决定频率叠加的初始形态。

--------------------------------------------------[Core Features]
Based on the Lissajous curve algorithm, this node superimposes multiple low-frequency sine waves to ensure the camera smoothly and rhythmically drifts around the absolute center of the frame. This fundamentally solves the frame deviation problem caused by traditional noise-based shakes.

[Parameters]
- intensity: Controls the intensity of the shake. 0.40 is the optimal balance for handheld camera simulation.
- zoom_factor: Edge protection to prevent clipping. 1.05 is the default safe zone.
- fps: Frame rate, used to calculate the correct physical motion cycle.
- seed: Determines the initial state of the frequency superposition.
"""

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
                "intensity": ("FLOAT", {"default": 0.40, "min": 0.0, "max": 5.0, "step": 0.01}),
                "zoom_factor": ("FLOAT", {"default": 1.05, "min": 1.0, "max": 2.0, "step": 0.01}),
                "fps": ("FLOAT", {"default": 30.0, "min": 1.0, "max": 120.0, "step": 1.0}),
                "seed": ("INT", {"default": 42, "min": 0, "max": 0xffffffff}),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("IMAGE", "trajectory_json")
    FUNCTION = "apply_shake"
    CATEGORY = "DNode"

    def apply_shake(self, images, intensity, zoom_factor, fps, seed):
        B, H, W, C = images.shape
        trajectory = generate_lissajous_trajectory(B, fps, W, H, intensity, seed)
        dx_arr = trajectory["dx"]
        dy_arr = trajectory["dy"]
        
        images_pt = images.permute(0, 3, 1, 2)
        device = images_pt.device
        theta = torch.zeros((B, 2, 3), dtype=torch.float32, device=device)
        z = 1.0 / zoom_factor
        
        for i in range(B):
            tx = (dx_arr[i]) / (W / 2)
            ty = (dy_arr[i]) / (H / 2)
            theta[i, 0, 0] = z     
            theta[i, 1, 1] = z     
            theta[i, 0, 2] = tx    
            theta[i, 1, 2] = ty    

        grid = F.affine_grid(theta, images_pt.size(), align_corners=False)
        shaken_images = F.grid_sample(
            images_pt, grid, mode='bilinear', padding_mode='border', align_corners=False
        )
        
        shaken_images_out = shaken_images.permute(0, 2, 3, 1)
        json_output = json.dumps(trajectory, indent=2, ensure_ascii=False)
        
        return (shaken_images_out, json_output)

NODE_CLASS_MAPPINGS = {
    "DNode_CameraShakeLissajous": DNode_CameraShakeLissajous
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DNode_CameraShakeLissajous": "🎥 Lissajous Camera Shake (V1)"
}