# ComfyUI AYS 30+ Scheduler

为 ComfyUI 的公共调度器列表添加 `ays_30+`，可在普通 KSampler 和
KSampler (Efficient) 的 `scheduler` 下拉框中选择，无需添加独立节点。

## 安装

在 ComfyUI 的 `custom_nodes` 目录执行：

```sh
git clone https://github.com/linjian-ufo/comfyui-ays_30plus-scheduler.git
```

私有仓库需要先登录有访问权限的 GitHub 账号。安装后重启 ComfyUI，
保存工作流并刷新浏览器，即可选择 `ays_30+`。不需要额外安装 Python 依赖。

本地文件夹可命名为 `comfyui-ays_30+-scheduler`；仓库名使用 `30plus`
以兼容 GitHub 的命名规则。

## 实现与兼容性

本扩展仅注册 `ays_30+`，使用原作者的 SDXL_30 时间点和
`force_sigma_min=True`。现有调度器保持可用。它不是标准
`AlignYourStepsScheduler` 节点的别名。

需要提供 `SchedulerHandler`、`SCHEDULER_HANDLERS` 的新版 ComfyUI，
以及内置 `nodes_align_your_steps`、`nodes_gits` 模块。
已验证调度器注册、普通/高效 KSampler 后端列表，以及多个步数的噪声序列计算；
未进行完整出图质量评估。FLUX、SD3、Wan 等模型专用调度尚未验证。

## 卸载

将本扩展文件夹移出 `ComfyUI/custom_nodes`，然后重启 ComfyUI。

## Upstream attribution

Adds `ays_30+` to the shared ComfyUI scheduler list used by KSampler and
Efficiency Nodes. No extra Python dependencies are installed.

`upstream_schedulers.py` is an unmodified copy from:
https://github.com/pamparamm/ComfyUI-ppm/blob/99165b6eb6e13565242abc6b4e79d6134c98bc88/src/schedulers.py

The small registration adapter in `__init__.py` registers only `ays_30+`.
The upstream `inject_schedulers()` function and other PPM hooks are not run.
The algorithm uses SDXL_30 timestep indices with `force_sigma_min=True`.
It is intended for conventional SD/SDXL diffusion sampling; model-specific
flow schedules (FLUX, SD3, Wan, etc.) are not validated by this installation.

License: AGPL-3.0-or-later; see [LICENSE](LICENSE). The registration adapter and
documentation are distributed under the same license. Algorithm attribution to
Extraltodeus and Koitenshin is retained in the upstream source file.
