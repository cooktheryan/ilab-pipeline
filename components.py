from kfp import dsl

@dsl.component
def ilab_init_op():
    return dsl.ContainerOp(
        name='ilab-init',
        image='quay.io/rcook/nvidia1:2',
        command=['/usr/local/bin/ilab', 'config', 'init', '--non-interactive'],
        file_outputs={},
        pvolumes={'/instructlab': dsl.PipelineVolume(pvc='taxonomy')},
        gpu_limit=1,
    )

@dsl.component
def ilab_model_op():
    return dsl.ContainerOp(
        name='ilab-model',
        image='quay.io/rcook/nvidia1:2',
        command=['/usr/local/bin/ilab', 'model', 'download'],
        file_outputs={},
        pvolumes={'/instructlab': dsl.PipelineVolume(pvc='taxonomy')},
        gpu_limit=1,
    )

@dsl.component
def ilab_taxonomy_fork_clone_op():
    return dsl.ContainerOp(
        name='ilab-taxonomy-fork-clone',
        image='quay.io/rcook/nvidia1:2',
        command=['git', 'clone', 'https://github.com/cooktheryan/taxonomy.git', '/instructlab/my-taxonomy'],
        file_outputs={},
        pvolumes={'/instructlab': dsl.PipelineVolume(pvc='taxonomy')},
        gpu_limit=1,
    )

@dsl.component
def ilab_taxonomy_sed_op():
    return dsl.ContainerOp(
        name='ilab-taxonomy-sed',
        image='quay.io/rcook/nvidia1:2',
        command=['sed', '-i', 's/three/four/g', 'my-taxonomy/compositional_skills/extraction/inference/qualitative/e2e-siblings/qna.yaml'],
        file_outputs={},
        pvolumes={'/instructlab': dsl.PipelineVolume(pvc='taxonomy')},
        gpu_limit=1,
    )

@dsl.component
def ilab_taxonomy_validate_op():
    return dsl.ContainerOp(
        name='ilab-taxonomy-validate',
        image='quay.io/rcook/nvidia1:2',
        command=['/usr/local/bin/ilab', 'taxonomy', 'diff', '--taxonomy-path=/instructlab/my-taxonomy'],
        file_outputs={},
        pvolumes={'/instructlab': dsl.PipelineVolume(pvc='taxonomy')},
        gpu_limit=1,
    )

@dsl.component
def ilab_train_op():
    return dsl.ContainerOp(
        name='ilab-train',
        image='quay.io/rcook/nvidia1:2',
        command=['/usr/local/bin/ilab', 'data', 'generate', '--taxonomy-path=/instructlab/my-taxonomy'],
        file_outputs={},
        pvolumes={'/instructlab': dsl.PipelineVolume(pvc='taxonomy')},
        gpu_limit=1,
    )

