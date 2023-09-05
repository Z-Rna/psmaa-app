def smaa2_result_dict(result, alt_names):
    from .color_utils import generate_pastel_colormap
    m, n = result.shape

    colormap = generate_pastel_colormap(n)

    res = dict()
    res_dataset = []


    for j in range(n):
        label = f'Rank {j+1}'
        data = [round(result[i, j], 2) for i in range(m)]
        color = colormap[j]
        res_dataset.append({'label': label, 'data': data, 'backgroundColor': color})

    res['labels'] = alt_names
    res['datasets'] = res_dataset

    return res

def smaatri_result_dict(result, alt_names, cat_names):
    from .color_utils import generate_pastel_colormap
    m, p = result.shape

    colormap = generate_pastel_colormap(p)

    res = dict()
    res_dataset = []


    for j in range(p):
        label = f'{cat_names[j]}'
        data = [round(result[i, j], 2) for i in range(m)]
        color = colormap[j]
        res_dataset.append({'label': label, 'data': data, 'backgroundColor': color})

    res['labels'] = alt_names
    res['datasets'] = res_dataset

    return res
