from fastapi.responses import JSONResponse
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
import models
import utils

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {
        'app info': 'implemented endpoints',
        'endpoints' : {
            'get output of SMAA2 method': {
                'endpoint': f'/smaa2results',
                'method': 'POST'
            },
            'get output of SMAATri method': {
                'endpoint': '/smaatriresults',
                'method': 'POST'
            },
        }
    }

@app.post("/smaa2results")
async def results_smaa2(item: models.DataSMAA2):
    from psmaa import no_preference, cardinal_preference, ordinal_preference
    model = utils.create_SMAA2_model(item)
    pref_name, pref_array = utils.get_preference(item)

    if pref_name == 'ordinal':
        pref = ordinal_preference
        pref_array = [pref-1 for pref in pref_array]
    elif pref_name == 'cardinal':
        pref = cardinal_preference
    else:
        pref = no_preference

    try:
        model.compute_w_c_and_b(pref, pref_array)
    except Exception as e:
        print(f"\033[91mException: {e}\033[00m")
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": str(e)})

    alt_names = model.impact_matrix.get_alternatives_names()

    smaa2_res = (utils.smaa2_result_dict(model.b, alt_names))

    return smaa2_res

@app.post("/smaatriresults")
async def results_smaatri(item: models.DataSMAATri):
    print(item)
    from psmaa import no_preference, cardinal_preference, ordinal_preference
    model = utils.create_SMAATri_model(item)

    pref_name, pref_array = utils.get_preference(item)

    if pref_name == 'ordinal':
       pref = ordinal_preference
       pref_array = [pref - 1 for pref in pref_array]
    elif pref_name == 'cardinal':
       pref = cardinal_preference
    else:
       pref = no_preference

    try:
        model.compute_pi(pref, pref_array)
    except Exception as e:
        print(f"\033[91mException: {e}\033[00m")
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": str(e)})


    alt_names = model.impact_matrix.get_alternatives_names()
    cat_names = model.profile_matrix.get_categories_names()

    smaatri_res = utils.smaatri_result_dict(model.pi, alt_names, cat_names)
    print(smaatri_res)
    return smaatri_res