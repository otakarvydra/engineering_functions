#This script contains thermodynamic functions to be used in engineering models. 

#This function outputs the boiling temperature of water as a function of pressure.
#Input (bar), Output (K)
def water_boiltemp(P_r):

    P = (0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10) 
    T = (17.51, 24.10, 28.98, 32.90, 36.18, 39.02, 41.53, 43.79, 45.83, 60.09, 69.13, 75.89, 81.35, 85.95, 89.96, 93.51, 96.71, 99.63, 102.32, 104.81, 107.13, 109.32, 111.37, 113.32, 115.17, 116.93, 118.62, 120.23, 123.27, 126.09, 128.73, 131.20, 133.54, 138.87, 143.63, 147.92, 151.85, 155.47, 158.84, 161.99, 164.96, 167.76, 170.42, 172.94, 175.36, 177.67, 179.88)
    
    for i in range(len(P)):
        if P_r < P[i]:
            break

    P_h = P[i]
    P_l = P[i - 1]
    
    T_h = T[i]
    T_l = T[i - 1]

    slope  = (T_h - T_l) / (P_h - P_l)
    T_diff = slope * (P_r - P_l)
    T_r = T_l + T_diff
    T_r = T_r + 273
    return T_r 

#This function outputs the latent heat of vaporization as a function of temperature.
#Input (deg C), Output (kJ/kg)
def water_vapheat(T_r):

    T  = (17.51, 24.10, 28.98, 32.90, 36.18, 39.02, 41.53, 43.79, 45.83, 60.09, 69.13, 75.89, 81.35, 85.95, 89.96, 93.51, 96.71, 99.63, 102.32, 104.81, 107.13, 109.32, 111.37, 113.32, 115.17, 116.93, 118.62, 120.23, 123.27, 126.09, 128.73, 131.20, 133.54, 138.87, 143.63, 147.92, 151.85, 155.47, 158.84, 161.99, 164.96, 167.76, 170.42, 172.94, 175.36, 177.67, 179.88)
    dH = (2460.19, 2444.65, 2433.10, 2423.82, 2416.01, 2409.24, 2403.25, 2397.85, 2392.94, 2358.40, 2336.13, 2319.23, 2305.42, 2293.64, 2283.30, 2274.05, 2265.65, 2257.92, 2250.76, 2244.08, 2237.79, 2231.86, 2226.23, 2220.87, 2215.75, 2210.84, 2206.13, 2201.59, 2192.98, 2184.91, 2177.30, 2170.08, 2163.22, 2147.35, 2132.95, 2119.71, 2107.42, 2095.90, 2085.03, 2074.73, 2064.92, 2055.53, 2046.53, 2037.86, 2029.49, 2021.40, 2013.56)

    for i in range(len(T)):
        if T_r < T[i]:
            break
    
    T_h     = T[i]
    T_l     = T[i - 1]

    dH_h    = dH[i]
    dH_l    = dH[i - 1] 

    slope   = (dH_h - dH_l) / (T_h - T_l)
    dH_diff = slope * (T_r - T_l)
    dH_r    = dH_l + dH_diff
    return dH_r

#This function outputs the sensible heat of gas.
#Input (gas type, T1 (deg C), T2 (deg C), Output (J/mol)
def gas_sensheat(gas, T_1, T_2):

    gas_cp_data = {

    'H20'  : (32.243, 19.238e-4, 10.555e-6, -3.596e-9),
    'N2'   : (31.15, -1.357e-2, 26.796e-6, -1.168e-8),
    '02'   : (28.106, -3.680e-6, 17.459e-6, -1.065e-8),
    'CO2'  : (19.795, 73.436e-3, -5.602e-5, 17.153e-9),
    'CH4'  : (19.251, 52.126e-3, 11.974e-6, -1.132e-8),
    'C2H6' : (5.409, 17.811e-2, -6.938e-5, 87.127e-10),
    'H2'   : (27.143, 92.738e-4, -1.381e-5, 76.451e-10),  

    }

    T_1  = T_1 + 273.15
    T_2  = T_2 + 273.15
    coef = gas_cp_data[gas]
    a    = coef[0]
    b    = coef[1]
    c    = coef[2]
    d    = coef[3]
    Q_1  = a * T_1 + b * T_1 ** 2 / 2 + c * T_1 ** 3 / 3 + d * T_1 ** 4 / 4
    Q_2  = a * T_2 + b * T_2 ** 2 / 2 + c * T_2 ** 3 / 3 + d * T_2 ** 4 / 4
    return (Q_2 - Q_1)