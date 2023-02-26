# CIL-via-FSC

1. Guide to run our code  
    Requirements should be installed at Python 3.7.
    ```python
    pip install -r requirements.txt
    ```
    Pytorch installation is required, https://pytorch.org/ 
    In our case, pip install torch==1.10.0+cu111 torchvision==0.11.0+cu111 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
    Run the experiment on CIFAR 100 in the order of three different classes with the initial 50 classes:  
    ```bash
    bash exp_cifar_cwd_fsc.sh
    ```  
    In the same way, run the experiment on ImageNet 100 in the order of three different classes with the initial 50 classes:  
    ```bash
    bash exp_im100_cwd_fsc.sh
    ```  
    The device of our experiments is TITAN-V GPU.  
    If the device is different, the results may be slightly different.   

2. Customizing code  
To use FSC loss for individual projects, you can use the code implemented in /src/approach/fcs_loss.py

3. Contact   
Jeonghoon Kim, naon710@gmail.com

Our code is base on [FACIL](https://github.com/mmasana/FACIL), and [CwD](https://github.com/Yujun-Shi/CwD). 
