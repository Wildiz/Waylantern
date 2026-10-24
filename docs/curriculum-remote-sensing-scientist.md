# Learning curriculum: Remote Sensing Scientist

An editorial study recipe exposing gaps in GIS, sensor physics and specialist image interpretation.

[Home](../README.md) / [Curricula](curricula.md) / [Data, analytics and artificial intelligence](professions-data-ai.md#roles-in-this-group)

**Target profile:** [Remote Sensing Scientist](professions-data-ai.md#remote-sensing-scientist)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Physical geography or relevant domain science
- Basic Python and array operations
- Statistics
- Familiarity with spatial coordinates

**What you will produce:** A small documented spatial experiment whose sensor, coordinate and validation assumptions are explicit.

**Resource coverage:** 0 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Identify the sensor and physical measurement](#stage-1)
2. [Inspect arrays without losing meaning](#stage-2)
3. [Establish spatial alignment and validation](#stage-3)
4. [Capstone - report a small bounded spatial comparison](#stage-4)

<a id="stage-1"></a>
## 1. Identify the sensor and physical measurement

**Learn:**

- Spectral bands and radiometry
- Spatial and temporal resolution
- Measurement and atmospheric limitations

**Resource still needed:** No verified remote-sensing physics or sensor-specific curriculum is currently catalogued.

**Practise:** Select a permitted teaching image and prepare a metadata sheet explaining what the measurements represent.

**Advance when:** Distinguish a sensor observation from a derived environmental interpretation and identify the relevant resolution limits.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Inspect arrays without losing meaning

**Learn:**

- Array dimensions and masks
- Missing pixels and data types
- Descriptive image statistics

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [NumPy Tutorials](https://numpy.org/numpy-tutorials/) — intermediate in this topic; free access. [Details](area-data.md#resource-numpy-tutorials).
- [100 NumPy Exercises](https://github.com/rougier/numpy-100) — intermediate in this topic; free access. [Details](area-data.md#resource-numpy-100-exercises).

**Resource still needed:** NumPy supports array handling but does not teach geospatial formats or radiometric corrections.

**Practise:** Use a synthetic multiband array to practice masking and summary calculations before applying an approved image-reading procedure.

**Advance when:** Preserve shape and mask semantics and explain why missing pixels must not be treated as zero observations.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Establish spatial alignment and validation

**Learn:**

- Coordinate reference systems
- Resampling and spatial dependence
- Ground reference and uncertainty

**Resource still needed:** No verified GIS, georeferencing or ground-validation practical is currently catalogued; obtain specialist guidance before spatial conclusions.

**Practise:** Design an alignment and validation checklist for two observations of the same area, explicitly recording unresolved transformations.

**Advance when:** Demonstrate with a reviewed example that corresponding locations align and that validation observations are independent where required.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Capstone - report a small bounded spatial comparison

**Learn:**

- Change interpretation
- Reproducible spatial processing
- Sensor and validation limitations

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [OpenIntro Statistics](https://www.openintro.org/book/os/) — beginner in this topic; free access. [Details](area-data.md#resource-openintro-statistics).

**Resource still needed:** Statistical foundations do not replace a verified end-to-end remote-sensing workflow; specialist review remains required.

**Practise:** Complete one supervised teaching comparison with metadata, processing parameters, a map or image and validation evidence.

**Advance when:** Explain the coordinate and measurement assumptions, reproduce the processing and avoid attributing sensor artefacts to environmental change.

## After this recipe

Add a verified GIS stack and domain-specific remote-sensing training before extending the analysis to operational decisions.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [ACM Computing Curricula Recommendations](profession-references.md#reference-acm-curricula)

[Back to roles in this group](professions-data-ai.md#roles-in-this-group) · [Find a specific resource](catalogue.md)
