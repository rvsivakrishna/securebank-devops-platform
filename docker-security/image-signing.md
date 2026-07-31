# Container Image Signing

## Tool

Cosign


## Purpose

Ensure container image integrity and verify that images are created from trusted sources.


## Signing Flow


Docker Build

        |

Generate Image Digest

        |

Cosign Sign

        |

Registry


## Verification

Example:

cosign verify IMAGE_NAME

