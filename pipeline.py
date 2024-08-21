import kfp
from kfp import dsl
from components import ilab_init_op, ilab_model_op, ilab_taxonomy_fork_clone_op, ilab_taxonomy_sed_op, ilab_taxonomy_validate_op, ilab_train_op

@dsl.pipeline(
    name='Ilab Training Pipeline',
    description='Instructlab training workflow'
)
def ilab_pipeline():
    taxonomy_volume = dsl.Volume(name='taxonomy', pvc='taxonomy')

    ilab_init = ilab_init_op().add_volume(taxonomy_volume)
    ilab_model = ilab_model_op().after(ilab_init).add_volume(taxonomy_volume)
    ilab_taxonomy_fork_clone = ilab_taxonomy_fork_clone_op().after(ilab_model).add_volume(taxonomy_volume)
    ilab_taxonomy_sed = ilab_taxonomy_sed_op().after(ilab_taxonomy_fork_clone).add_volume(taxonomy_volume)
    ilab_taxonomy_validate = ilab_taxonomy_validate_op().after(ilab_taxonomy_sed).add_volume(taxonomy_volume)
    ilab_train = ilab_train_op().after(ilab_model, ilab_taxonomy_validate).add_volume(taxonomy_volume)

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(ilab_pipeline, 'ilab_pipeline.yaml')