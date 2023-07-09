from datetime import datetime
import numpy as np

# returns vaccination rate and dose delay
def get_vaccine_rate(t):
    day0 = datetime.strptime('1-jan-2020', '%d-%b-%Y')
    t_vac0 = (datetime.strptime('14-dec-2020', '%d-%b-%Y') - day0).days
    t_delay = (datetime.strptime('31-may-2021', '%d-%b-%Y') - day0).days
    t_vac_peak = (datetime.strptime('30-jun-2021', '%d-%b-%Y') - day0).days

    fraction_first_dose = 0.6
    peak_vac_rate = 220*5e-5
    ss_vac_rate = 10*5e-5

    eps_PZ = 0.95
    eps_AZ = 0.05

    if t < t_vac0:
        vr1 = np.array([0, 0])
        vr2 = np.array([0, 0])
    elif t < t_delay:
        curr_vac_rate = peak_vac_rate * (t - t_vac0) / (t_vac_peak - t_vac0)
        vr1 = curr_vac_rate * np.array([eps_PZ, eps_AZ])
        vr2 = np.array([1/(16*7), 1/(16*7)])
    elif t < t_vac_peak:
        curr_vac_rate = peak_vac_rate * (t - t_vac0) / (t_vac_peak - t_vac0)
        vr1 = curr_vac_rate * np.array([eps_PZ, eps_AZ])
        vr2 = np.array([1/28, 1/(8*7)])
    else:
        curr_vac_rate = (peak_vac_rate - ss_vac_rate) * np.exp(-3e-2 * (t - t_vac_peak)) + ss_vac_rate
        vr1 = curr_vac_rate * np.array([eps_PZ, eps_AZ])
        vr2 = np.array([1/28, 1/(8*7)])

    return vr1, vr2
