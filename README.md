# MatAgent
A generative framework for interpretable and targeted inorganic materials design using diffusion-based generation, property prediction, and LLM-driven reasoning.

## Requirements
- Python 3.12

## Installation
### Install PyTorch
First, install PyTorch. For example, with CUDA 12.4, you can install PyTorch as follows:
```
$ pip install torch==2.5.1 --index-url https://download.pytorch.org/whl/cu124
```

### Install PyG
Install PyTorch Geometric and its dependencies:
```
$ pip install torch_geometric
$ pip install torch_scatter torch_sparse -f https://data.pyg.org/whl/torch-2.5.0+cu124.html
```

### Intall other dependencies
Install all other required packages with:
```
$ pip install -e .
```

## Setup OpenAI API Key
Set your OpenAI API Key as an environment variable:
```
$ export OPENAI_API_KEY="YOUR_API_KEY"
```

## Running the code
### Running the inference script
After installation, run the inference script:
```
$ matagent-inference --use_planning --data_path "./data/mp_20/train.csv" --n_init 1 --n_iterations 16 --target_value -3.8
```
Here, the `--data_path` parameter should be set to the path containing data used for sampling initial compositions.

### Generate with additional constraints
To impose additional constraints, use the `--additional_prompt` parameter.
```
$ matagent-inference --use_planning --data_path "./data/mp_20/train.csv" --n_init 1 --n_iterations 16 --target_value -3.8 --additional_prompt "ADDITIONAL PROMPT"
```
## Citation
```
@article{takahara2025accelerated,
  title={Accelerated Inorganic Materials Design with Generative AI Agents}, 
  author={Izumi Takahara and Teruyasu Mizoguchi and Bang Liu},
  journal={arXiv preprint arXiv:2504.00741},
  year={2025},
}
```

## Acknowledgement
This project was primarily built upon [CDVAE](https://github.com/txie-93/cdvae), [DiffCSP](https://github.com/jiaor17/DiffCSP), [ComFormer](https://github.com/divelab/AIRS/tree/main/OpenMat/ComFormer), and [MatExpert](https://github.com/BangLab-UdeM-Mila/MatExpert).