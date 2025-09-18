# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 15:30:58 2025

@author: mdial
"""

import numpy as np
from spicy.stat import norm

def get_d1(S,K,T,r,sigma):
    return (np.log(S/K)+(r+sigma**2/2)*T)/sigma*np.sqrt(T)

def black_scholes_price(S,K,T,r,sigma,option_type):
    
    d1= get_d1(S, K, T, r, sigma)
    d2=d1-sigma*np.sqrt(T)
    
    if option_type.lower()=='call':
        return S*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
    if option_type.lower()=='put':
        return K*np.exp(-r*T)*norm.cdf(-d2)-S*norm.cdf(-d1)
    else:
        raise ValueError("Error: The option type should be call or put.")
        
def get_delta(S,K,T,r,sigma,option_type):
    
    d1=get_d1(S, K, T, r, sigma)
    
    if option_type.lower()=='call':
        return norm.cdf(d1)
    if option_type.lower()=='put':
        return norm.cdf(d1)-1
    else:
        raise ValueError("Error: The option type should be call or put.")
        
def get_gamma(S,K,T,r,sigma):
    d1=get_d1(S, K, T, r, sigma)
    return norm.pdf(d1)/(S*sigma*np.sqrt(T))



    
print(get_d1(10,5,6,0.05,5))