import numpy as np
from psmaa import Alternative, Criterion, CriterionTri, Profile, Category, \
    ProfileMatrix, ImpactMatrix, ImpactMatrixTri, SMAA2, SMAATri

def get_preference(data):
    preference = data.preference
    name = preference.name
    preference_array = [pref['value'] for pref in preference.preferenceArray]
    return name, preference_array

def create_SMAA2_model(data):
    im = create_impact_matrix(data)
    model = SMAA2(im)
    return model

def create_SMAATri_model(data):
    im, pm = create_impact_profie_matrix(data)
    lambda_value = [data.lambda_value.min, data.lambda_value.max]
    model = SMAATri(im, pm, lambda_value)
    return model

def create_impact_profie_matrix(data):
    cri_list = data.criList.data
    alt_list = cri_list[0]['altList']
    pro_list = cri_list[0]['profileList']

    n, m, p = len(cri_list), len(alt_list), len(pro_list)
    raw_data = np.zeros((m, n))
    profile_data = np.zeros((n, p))

    criterions = []
    alternatives = [Alternative(alt['alt']) for alt in alt_list]
    profiles = [Profile(f"{pro['pro']['pro_low']}-{pro['pro']['pro_high']}") for pro in pro_list]
    categories = [Category(pro_list[i]['pro']['pro_low'])
                  if i < len(pro_list) else Category(pro_list[i-1]['pro']['pro_high'])
                  for i in range(len(pro_list)+1)]

    for i, cri in enumerate(cri_list):
        cri_name = cri['cri']
        cri_ascending = cri['ascending']
        cri_alt_list = cri['altList']
        cri_pro_list = cri['profileList']
        cri_q = float(cri['indifrence'])
        cri_p = float(cri['preference'])
        cri_v = float(cri['veto'])
        for j, alt in enumerate(cri_alt_list):
            alt_value = cri_alt_list[j]['value']
            raw_data[j, i] = float(alt_value)
        for j, pro in enumerate(cri_pro_list):
            pro_value = cri_pro_list[j]['value']
            profile_data[i, j] = float(pro_value)
        criterion = CriterionTri(cri_name,cri_q, cri_p, cri_v, cri_ascending)
        criterions.append(criterion)

    im = ImpactMatrix(np.array(alternatives),
                      np.array(criterions),
                      raw_data)

    pm = ProfileMatrix(np.array(profiles),
                       np.array(criterions),
                       np.array(categories),
                       profile_data)
    return im, pm

def create_impact_matrix(data):
    cri_list = data.criList.data
    alt_list = cri_list[0]['altList']

    n, m = len(cri_list), len(alt_list)
    raw_data = np.zeros((m, n))

    criterions = []
    alternatives = [Alternative(alt['alt']) for alt in alt_list]

    for i, cri in enumerate(cri_list):
        cri_name = cri['cri']
        cri_ascending = cri['ascending']
        cri_type = cri['type']
        cri_alt_list = cri['altList']
        for j, alt in enumerate(cri_alt_list):
            alt_value = cri_alt_list[j]['value']
            raw_data[j, i] = float(alt_value)
        criterion = Criterion(cri_name, cri_ascending, cri_type)
        criterions.append(criterion)

    im = ImpactMatrix(np.array(alternatives),
                      np.array(criterions),
                      raw_data)
    return im