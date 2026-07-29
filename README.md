# CEDAR
Computational Engine for Designing Architecture Rasters (CEDAR) is a physics simulation written in Python, meant for simulating thermal and electrical inefficiency within computational substrates. Meant for my research paper.

## DEODARA
Differentiable Efficiency Optimisation of Discrete Architectures Recursive Algorithm (DEODARA) is the Pareto DARTS-like optimisation algorithm to be applied to the discrete hardware rasters. It explores a landscape of already optimised models. It trains the model first, before measuring inefficiencies and changing the model (the architecture raster holding it) accordingly. It executes supervised learning.

## LIBANI
Lower Inefficiencies By Architecture, Non-Intrusively (LIBANI) is the non-bilevel optimisation counterpart to DEODARA. It does not 'intrude' the process by interleaving model alterations with pretraining, rather, it optimises the cost vector directly and immediately.