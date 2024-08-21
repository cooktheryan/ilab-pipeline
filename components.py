from kfp import dsl

@dsl.container_component
def ilab_init_op():
    return dsl.ContainerSpec(
        image='quay.io/rcook/nvidia1:2',
        command=['/usr/local/bin/ilab', 'config', 'init', '--non-interactive'],
        resources={'limits': {'nvidia.com/gpu': '1'}},
        volume_mounts=[dsl.VolumeMount(volume=dsl.PipelineVolume(pvc='taxonomy'), mount_path='/instructlab')]
    )

@dsl.container_component
def ilab_model_op():
    return dsl.ContainerSpec(
        image='quay.io/rcook/nvidia1:2',
        command=['/usr/local/bin/ilab', 'model', 'download'],
        resources={'limits': {'nvidia.com/gpu': '1'}},
        volume_mounts=[dsl.VolumeMount(volume=dsl.PipelineVolume(pvc='taxonomy'), mount_path='/instructlab')]
    )

@dsl.container_component
def ilab_taxonomy_fork_clone_op():
    return dsl.ContainerSpec(
        image='quay.io/rcook/nvidia1:2',
        command=['git', 'clone', 'https://github.com/cooktheryan/taxonomy.git', '/instructlab/my-taxonomy'],
        resources={'limits': {'nvidia.com/gpu': '1'}},
        volume_mounts=[dsl.VolumeMount(volume=dsl.PipelineVolume(pvc='taxonomy'), mount_path='/instructlab')]
    )

@dsl.container_component
def ilab_taxonomy_sed_op():
    return dsl.ContainerSpec(
        image='quay.io/rcook/nvidia1:2',
        command=['sed', '-i', 's/three/four/g', 'my-taxonomy/compositional_skills/extraction/inference/qualitative/e2e-siblings/qna.yaml'],
        resources={'limits': {'nvidia.com/gpu': '1'}},
        volume_mounts=[dsl.VolumeMount(volume=dsl.PipelineVolume(pvc='taxonomy'), mount_path='/instructlab')]
    )

@dsl.container_component
def ilab_taxonomy_validate_op():
    return dsl.ContainerSpec(
        image='quay.io/rcook/nvidia1:2',
        command=['/usr/local/bin/ilab', 'taxonomy', 'diff', '--taxonomy-path=/instructlab/my-taxonomy'],
        resources={'limits': {'nvidia.com/gpu': '1'}},
        volume_mounts=[dsl.VolumeMount(volume=dsl.PipelineVolume(pvc='taxonomy'), mount_path='/instructlab')]
    )

@dsl.container_component
def ilab_train_op():
    return dsl.ContainerSpec(
        image='quay.io/rcook/nvidia1:2',
        command=['/usr/local/bin/ilab', 'data', 'generate', '--taxonomy-path=/instructlab/my-taxonomy', 'num-epochs=1'],
        resources={'limits': {'nvidia.com/gpu': '1'}},
        volume_mounts=[dsl.VolumeMount(volume=dsl.PipelineVolume(pvc='taxonomy'), mount_path='/instructlab')]
    )