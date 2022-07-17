import numpy as np
import open3d as o3d

from typing import List
from annotators.AnnotatorPointCloud import AnnotatorPointCloud
from Camera import Camera
from dto.Pcd import Pcd
from pcdBuilders.PcdBuilder import PcdBuilder


class PcdBuilderPointcloud(PcdBuilder):
    def __init__(self, camera: Camera, annot: AnnotatorPointCloud):
        super().__init__(camera, annot)

    def _get_points(self, depth_image_path):
        pc = o3d.io.read_point_cloud(depth_image_path)
        # if image_number > 50:
        #     o3d.visualization.draw_geometries([pc])

        return Pcd(np.asarray(pc.points) / 1000)
