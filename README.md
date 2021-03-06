# Welcome to Guide RNA design!
This is the first edition of desiging the guide RNA, the main steps of the procedure are listed as follows:
- 1. Generating the possible sequence by some rules
-  2. Filter the sequence by RNAfold software
-  3. Choose the final sequence;

The function of each file is listed here:
 - **result21.1.06_60bp/result21.1.08_76bp(folder)**: The selection results of 40 possible structure; The MEA structure RNA structure could be found in **filter_structure.str**
 - **generate.py**: The programe to generate possible RNA sequence.
 - **filt_structure.py**: The programe to filter the possible structure by RNA fold results
 - **raw_sequence.fa**: The raw sequence generated by **generate.py**.
 - **filter_seq.fa**: The final sequence filtered by  **filt_structure.py**.

# Pipeline

Four steps to filter the sequence:
- 1.  Generating the possible sequence by **generate.py**: `'python generate.py'`
-  2. Filter the sequence by RNAfold software: `'./RNAfold <raw_sequence.fa --noPS > structure.str'`
-  3. Move the **structure.str** into the same folder of two .py files. And choose the final sequence by **filt_structure.py**: `'python filt_structure.py'`
-  4. Get the structure of final sequence: `' ./RNAfold <filter_seq.fa > filter_structure.str  '`

# Reference
Mathews DH, Disney MD, Childs JL, Schroeder SJ, Zuker M, Turner DH. (2004) Incorporating chemical modification constraints into a dynamic programming algorithm for prediction of RNA secondary structure. _Proc Natl Acad Sci U S A_ 101(19):7287-92.
```