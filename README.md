# Digit Plotting with Linear and Cubic Splines

## Overview

This project focuses on plotting four distinct digits using linear and cubic splines. The digits are selected randomly and are displayed separately in the top-right area (Area I) of the coordinate system. The spline equations are manually determined and then used for plotting in Python with Matplotlib.

## Features
Manual Spline Calculation: Spline points for each digit are selected manually, and corresponding equations are derived.

Linear and Cubic Splines: Two different spline methods are implemented for comparison.

Matplotlib Visualization: The digits are plotted using only the calculated spline equations, without using raw spline points.

Python-Only Implementation: The project is entirely written in Python, without any external computational tools.

## Implementation Details

The digits are constructed using key points in the top-right quadrant.

Linear Spline: Connects selected points with straight-line segments.

Cubic Spline: Creates smooth curves using cubic polynomial interpolation.

The equations for each spline are precomputed and used in Matplotlib for plotting.
