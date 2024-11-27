# Automatic intensity-based tagger of facial gestures
This repository contains a full workflow for automatic, intensity-based annotation of facial gestures. This allows for larger datasets than before and for reliable, between-subjects annotation with computer-vision and calibration. This full work-flow requires Live Link and provides post-processing for integration with ELAN.

This work flow allows for quantification intensity information from Live Link, but also allows for chosen threshold parameters for automatic annotation of activation of gestures over chosen threshold value.
It also re-formats the raw data from Live Link so the tags can be imported into ELAN as tiers so it can be aligned to the video recording.


For integration with ELAN:
1. zero_timestamping_LiveLinkOutput.py is the first step. This re-formats the Live Link output for interoperable column names between files and adds a 'Time Elapsed' column which is starts as 0 hours, 0 minutes, 0 seconds, 0 frames, 0 milliseconds. This timestamping step is necessary for integrating the automatic tags as annotations onto ELAN tiers.
