# CIL-via-FSC

1. Guide to run our code  
<p> Run the experiment on CIFAR 100 in the order of three different classes with the initial 50 classes:
  ```bash
  bash exp_cifar_cwd_fsc.sh
  ```  
Run the experiment on ImageNet 100 in the order of three different classes with the initial 50 classes:  
  ```bash
  bash exp_im100_cwd_fsc.sh
  ```  
The device of Our experiments is TITAN-V GPU.     
If the device is different, the results may be different. </p>

2. customizing code  
To use FSC loss for individual projects, you can use the code implemented in /src/approach/fcs_loss.py

3. citation  
Not yet

4. acknowledgment  
Not yet

Our code base on [FACIL](https://github.com/mmasana/FACIL), and [CwD](https://github.com/Yujun-Shi/CwD) 
