"""I/O utilities for loading and saving meshes and point clouds."""

import numpy as np
import trimesh
import open3d as o3d


def load_mesh(path: str) -> trimesh.Trimesh:
    """Load a mesh from file and return as Trimesh object."""
    return trimesh.load(path, force="mesh")


def save_mesh(mesh: trimesh.Trimesh, path: str) -> None:
    """Save a Trimesh mesh to file."""
    mesh.export(path)


def load_point_cloud(path: str) -> np.ndarray:
    """Load a point cloud from file and return as (N, 3) numpy array."""
    pcd = o3d.io.read_point_cloud(path)
    return np.asarray(pcd.points)


def save_point_cloud(points: np.ndarray, path: str) -> None:
    """Save an (N, 3) numpy array as a point cloud file."""
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    o3d.io.write_point_cloud(path, pcd)


def sample_points(mesh: trimesh.Trimesh, n_samples: int = 100_000) -> np.ndarray:
    """Sample n_samples points uniformly from mesh surface."""
    points, _ = trimesh.sample.sample_surface(mesh, n_samples)
    return points
