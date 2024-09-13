"""Constants for the Analyzer class."""

import dataclasses

@dataclasses.dataclass(frozen=True)
class AnalyzeConstants:
    """Dataclass for constants used in the analyze_data module."""

    # Maximum memory in bytes for each image and mask pair.
    MAX_MEMORY_PER_IMAGE_MASK_PAIR_BYTES = 2e9

    # The amount that we multiply each component of the target spacing
    # vector if an image mask pair exceeds the
    # MAX_MEMORY_PER_IMAGE_MASK_PAIR_BYTES value.
    COARSEN_TARGET_SPACING_FACTOR = 1.25

    # Minimum average volume reduction expressed as a fraction after cropping
    # each image to its foreground.
    MIN_AVERAGE_VOLUME_REDUCTION_FRACTION = 0.2

    # Minimum sparsity expressed as a fraction.
    MIN_SPARSITY_FRACTION = 0.2

    # Maximum ratio of the maximum and minimum components of the target spacing
    # for an image to be considered anisotropic.
    MAX_DIVIDED_BY_MIN_SPACING_THRESHOLD = 3.0

    # If the median target spacing of a dataset is anisotropic, then we
    # take this percentile of the coarsest axis and replace that value with
    # the resulting percentile value.
    ANISOTROPIC_LOW_RESOLUTION_AXIS_PERCENTILE = 10

    # For CT images only. We gather every i-th voxel in the image where the
    # ground truth mask is non-zero. We use the resulting list of values
    # to compute the mean and standard deviation for z-score normalization.
    CT_GATHER_EVERY_ITH_VOXEL_VALUE = 10

    # For CT images only. We clip according to the 0.5 and 99.5 percentiles of
    # the voxels corresponding to the non-zero regions in the ground truth masks
    # over the entire dataset.
    CT_GLOBAL_CLIP_MIN_PERCENTILE = 0.5
    CT_GLOBAL_CLIP_MAX_PERCENTILE = 99.5

    # How many digits are printed for floating point numbers.
    PRINT_FLOATING_POINT_PRECISION = 4