# MeshAnything V2 Benchmark

Benchmark repository for comparing **MeshAnything V2** with tokenization baselines using custom images and the geometric metrics reported in the original paper.

The main workflow for this project was executed in **Google Colab**, in the notebook [notebooks/meshAnything_comparison_full_process.ipynb](notebooks/meshAnything_comparison_full_process.ipynb). That notebook contains the complete generation, comparison, and evaluation pipeline.

The rest of the code in this repository consists of implementation variations of the pipeline, using **TripoSR** instead of **Rodin** to generate dense meshes that serve as reference/input for the next stages.

## Goal

Evaluate the quality of meshes produced by MeshAnything V2 against a naive baseline using metrics such as:

- CD (Chamfer Distance)
- ECD (Edge Chamfer Distance)
- NC (Normal Consistency)
- number of vertices and faces
- V_Ratio and F_Ratio

## Pipeline

1. Custom images enter the pipeline.
2. **TripoSR** generates a dense mesh.
3. The mesh is converted into a point cloud.
4. **MeshAnything V2** and the naive baseline generate meshes from that input.
5. The outputs are evaluated with the paper metrics.
6. The final results are consolidated into tables and visualizations.

## Project Structure

- `notebooks/01_image_to_pointcloud.ipynb`: image → dense mesh → point cloud conversion stage.
- `notebooks/02_inference.ipynb`: inference with MeshAnything V2 and baselines.
- `notebooks/03_evaluation.ipynb`: metric computation, tables, and figures.
- `notebooks/meshAnything_comparison_full_process.ipynb`: main notebook, with the full workflow executed in Colab.
- `src/metrics/`: metric implementations.
- `src/utils/io.py`: mesh and point cloud read/write helpers.
- `src/visualization/`: result visualization routines.
- `data/`: pipeline inputs and outputs.
- `results/`: tables and figures generated during analysis.

## Models Used

- **TripoSR**: dense mesh generation from images.
- **MeshAnything V2**: main model under evaluation.
- **MeshAnything V1**: used as the naive baseline.

All models are used for inference only.

## Environment

The project was designed to run with GPU support in Colab Pro, but the code and repository layout also work for local development.

## Expected Outcome

The final goal is to produce comparison tables in the style of the original paper, highlighting the performance of MeshAnything V2 against the naive baseline.
