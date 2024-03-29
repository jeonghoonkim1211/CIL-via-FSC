for tk in 6  
do 
    for sd in 0 
    do
        device_id=3
        SEED=$sd
        bz=128
        lr=0.1
        mom=0.9
        wd=5e-4
        data=cifar100_icarl
        network=resnet18_cifar
        nepochs=160
        n_exemplar=20
 
        appr=lucir_cwd
        lamb=5.0
        nc_first=50
        ntask=$tk
        aux_coef=0.75
        coef_2i=7.0
        rej_thresh=1
        first_task_lr=0.1
        first_task_bz=128

        CUDA_VISIBLE_DEVICES=$device_id python3 main_incremental.py --exp-name nc_first_${nc_first}_ntask_${ntask} \
            --datasets $data --num-tasks $ntask --nc-first-task $nc_first --network $network --seed $SEED \
            --nepochs $nepochs --batch-size $bz --lr $lr --momentum $mom --weight-decay $wd --decay-mile-stone 80 120 \
            --clipping -1 --results-path results --save-models \
            --approach $appr --lamb $lamb --num-exemplars-per-class $n_exemplar --exemplar-selection herding \
            --aux-coef $aux_coef --coef-2i $coef_2i --reject-threshold $rej_thresh \
            --first-task-lr $first_task_lr --first-task-bz $first_task_bz
    done
done
