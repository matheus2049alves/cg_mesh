# AGENTS.md

## Project

MeshAnything V2 inference benchmark — run inference on custom images, compare against baselines (naive tokenization) using the paper's metrics. See `context (1).md` for full plan (in Portuguese).

## Status

Notebook 01 done (image→mesh→pointcloud). Notebooks 02 and 03 created (pending execution on Colab).

## Pipeline

```
Images → TripoSR (ground truth mesh + point cloud) → MeshAnything V2 / baselines → Metrics → Tables
```

- TripoSR generates dense mesh (used as ground truth) and point cloud
- MeshAnything V2 (~350M params, OPT-based) does point-cloud-to-mesh inference
- Baselines: naive tokenization (MeshAnything V1)

## Environment

- **GPU**: Google Colab Pro (L4 22.5GB). Both models run comfortably: TripoSR ~4-6GB, MeshAnything V2 ~2-4GB.
- **Python 3.10+**, PyTorch, Open3D, Trimesh, NumPy, SciPy, Matplotlib, Pandas
- `requirements.txt` covers both TripoSR and MeshAnythingV2 deps.

## Metrics

100K points sampled per mesh. Lower is better unless noted.

| Metric | Direction |
|--------|-----------|
| Chamfer Distance (CD) | ↓ |
| Edge Chamfer Distance (ECD) | ↓ |
| Normal Consistency (NC) | ↑ |
| Vertex/Face counts (#V, #F) | ↓ |
| V_Ratio, F_Ratio | ↓ |

S_Ratio is internal to tokenization — out of scope for evaluation.

## Conventions

- Notebooks: `notebooks/01_image_to_pointcloud.ipynb`, `02_inference.ipynb`, `03_evaluation.ipynb`
- Source: `src/metrics/`, `src/visualization/`, `src/utils/`
- Data: `data/images/`, `data/pointclouds/`, `data/meshes/{ground_truth,meshanything_v2,baselines/naive}/`
- Results: `results/tables/`, `results/figures/`
- I/O helpers: `src/utils/io.py` — `load_mesh()`, `save_mesh()`, `load_point_cloud()`, `save_point_cloud()`, `sample_points()`
- `.gitignore` excludes `data/`, `results/`, `venv/`, model checkpoints

## Repo quirks

- **MeshAnythingV2** repos are cloned into project root during notebook execution (not committed)
- V2 uses `main.py --input_dir <pc_dir> --out_dir <out> --input_type pc_normal`
- V1 uses same API but requires `--pretrained_weights` and `--codebook_size`/`--codebook_dim` args
- Point clouds must be `.npy` with shape `(N, 6)` — xyz + normals (unit vectors)
- V2 max faces: 1600. V1 max faces: 800. Input meshes should be well-shaped for these limits.
- Both repos use Accelerate — run via subprocess from notebooks, not direct import
