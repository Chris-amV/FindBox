## Formula Insertion

1. Open the `model.py` file.
2. Insert the formula in the same format as the existing examples. For instance:

   ```python
   phi1 = r"(always[1,2] (eventually[3,4] (x1 >= 3 and x1 <= 10)) -> (x1 >= 0 and x1 <= 10)) and (always (x1 >= -20 and x1 <= 20))"
   ```
   
3. After writing the formula, place the variable inside the following function:

   ```python
   specification = RTAMTDense(phi1, {"x1":0})
   ```

   Replace `phi1` with the variable name of the formula. For example:

   ```python
   phi2 = r"(always[0,1] (eventually[7,8] (x1 >= 3 and x1 <= 10)) -> (always[0,1] (eventually[14,15] (x1 >= 0 and x1 <= 10)))) and (always (x1 >= -20 and x1 <= 20))"
   specification = RTAMTDense(phi2, {"x1":0})
   ```

## Reconstruction

1. Open the `LanguageBoxGeneral.py` file.
2. Make necessary modifications based on the chosen formula. This might include adjustments to sample size and other parameters.
3. run the code.