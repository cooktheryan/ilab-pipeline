from kfp import compiler
from pipeline import ilab_pipeline

if __name__ == '__main__':
    compiler.Compiler().compile(ilab_pipeline, 'ilab_pipeline.yaml')

