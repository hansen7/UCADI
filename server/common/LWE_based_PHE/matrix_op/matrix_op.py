# -*- coding: utf-8 -*-

#  Copyright (c) 2021. Jiefeng, Ziwei and Hanchen
#  jiefenggan@gmail.com, ziwei@hust.edu.cn, hc.wang96@gmail.com

import torch
import matrix_op_cuda

def matmul(matA, matB):
    output = matrix_op_cuda.matmul(matA, matB, torch.zeros(matA.size(0), matB.size(1)).long().cuda())
    return output

def vecmul(vec, mat):
    output = matrix_op_cuda.vecmul(vec, mat, torch.zeros(mat.size(1)).long().cuda())
    return output
